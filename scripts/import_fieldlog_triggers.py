#!/usr/bin/env python3
"""Turn committed image-inbox uploads into independent fieldlog post packages.

Git history is the upload queue. A commit/path pair is a publishing event, so
retrying a run cannot overwrite a saved post and deliberately uploading the
same phone filename in a later commit creates a new post. The workflow commits
the packages and state together; this module never deletes inbox originals.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
from datetime import datetime
from zoneinfo import ZoneInfo

from fieldlog_image_codec import convert_image, validate_image, register_heif_opener
from site_post_metadata import dump_frontmatter, normalize_metadata, validate_metadata

ROOT = Path(__file__).resolve().parents[1]
CONTENT = "natsci/fieldlog"
INBOX = CONTENT + "/trigger_imgs"
STATE_PATH = Path(CONTENT + "/.publishing/state.json")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic", ".heif"}
IGNORED_NAMES = {"README.md", ".keep", ".gitkeep"}
OID = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})\Z")
IDENT = re.compile(r"\d{4}-\d{2}-\d{2}-\d{6}-[0-9a-f]{12}\Z")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def git(root: Path, *arguments: str) -> bytes:
    result = subprocess.run(["git", "-C", str(root), *arguments], capture_output=True)
    if result.returncode:
        error = result.stderr.decode("utf-8", "replace").strip()
        raise ValueError(f"Git history could not be read: {error}")
    return result.stdout


def relative_path(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise ValueError("Unsafe publishing path")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or value != path.as_posix():
        raise ValueError(f"Unsafe publishing path: {value}")
    return path


def safe_destination(root: Path, value: str) -> Path:
    relative = relative_path(value)
    destination = root.joinpath(*relative.parts)
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Publishing path follows a symlink: {value}")
    if not destination.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Publishing path leaves the repository: {value}")
    return destination


def read_state(root: Path = ROOT) -> dict:
    root = Path(root).resolve()
    path = safe_destination(root, STATE_PATH.as_posix())
    if not path.is_file():
        raise ValueError("Publishing state is missing; initialize its cursor before importing uploads")
    state = json.loads(path.read_text(encoding="utf-8"))
    if (not isinstance(state, dict) or state.get("version") != 1
            or not isinstance(state.get("cursor"), str) or not OID.fullmatch(state["cursor"])
            or not isinstance(state.get("events"), dict)):
        raise ValueError("Invalid publishing state")
    for key, event in state["events"].items():
        fields = ("id", "commit", "upload_path", "blob_sha", "sha256", "image_path", "route")
        if not isinstance(event, dict) or any(not isinstance(event.get(field), str) for field in fields):
            raise ValueError(f"Invalid publishing event: {key}")
        upload = relative_path(event["upload_path"])
        image = relative_path(event["image_path"])
        if (not OID.fullmatch(event["commit"]) or not OID.fullmatch(event["blob_sha"])
                or not re.fullmatch(r"[0-9a-f]{64}", event["sha256"])
                or ("file_sha256" in event and (not isinstance(event["file_sha256"], str)
                                               or not re.fullmatch(r"[0-9a-f]{64}", event["file_sha256"])))
                or not IDENT.fullmatch(event["id"])
                or len(upload.parts) < 4 or upload.parts[:3] != tuple(PurePosixPath(INBOX).parts)
                or upload.name in IGNORED_NAMES or upload.suffix.lower() not in EXTENSIONS
                or len(image.parts) != 7 or image.parts[:2] != ("natsci", "fieldlog") or image.parts[5] != "assets"
                or image.parts[4] != event["id"]
                or image.parts[2] != event["id"][:4] or image.parts[3] != event["id"][5:7]
                or image.suffix.lower() not in EXTENSIONS
                or key != event["commit"] + ":" + event["upload_path"]
                or event["route"] != f"{CONTENT}/{image.parts[2]}/{image.parts[3]}/{event['id']}/"):
            raise ValueError(f"Invalid publishing event: {key}")
    return state


def pending_commits(root: Path, cursor: str, head: str) -> list[str]:
    """Refuse a missing or rewritten cursor rather than replaying old uploads."""
    try:
        resolved = git(root, "rev-parse", "--verify", cursor + "^{commit}").decode().strip()
    except ValueError as error:
        raise ValueError("Publishing cursor is missing from Git history; restore history before importing") from error
    history = git(root, "rev-list", "--first-parent", head).decode().splitlines()
    if resolved not in history:
        raise ValueError("Publishing cursor is not on HEAD's first-parent history; review the branch before importing")
    return list(reversed(history[:history.index(resolved)]))


def changed_files(root: Path, commit: str) -> list[dict]:
    parent = git(root, "rev-parse", commit + "^1").decode().strip()
    raw = git(root, "diff-tree", "--no-commit-id", "--raw", "-r", "-z", "--no-renames",
              "--diff-filter=AMTD", "--no-abbrev", parent, commit, "--", INBOX + "/")
    chunks = raw.split(b"\0")
    if chunks[-1:] == [b""]:
        chunks.pop()
    if len(chunks) % 2:
        raise ValueError("Unexpected Git change listing")
    files = []
    for offset in range(0, len(chunks), 2):
        header = chunks[offset].decode("ascii").split()
        try:
            filename = chunks[offset + 1].decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValueError("Image upload paths must use UTF-8 filenames") from error
        path = relative_path(filename)
        if path.parts[:3] != tuple(PurePosixPath(INBOX).parts) or len(path.parts) < 4:
            raise ValueError(f"Upload is outside the image inbox: {filename}")
        if path.name in IGNORED_NAMES:
            continue
        if len(header) != 5 or not header[0].startswith(":") or header[4] not in {"A", "M", "T", "D"}:
            raise ValueError("Unexpected Git image change")
        files.append({"path": filename, "blob_sha": header[3], "mode": header[1], "status": header[4]})
    return sorted(files, key=lambda item: item["path"])


def commit_details(root: Path, commit: str) -> tuple[datetime, str]:
    raw = git(root, "show", "-s", "--format=%cI%x00%B", commit).decode("utf-8")
    timestamp, separator, message = raw.partition("\x00")
    if not separator:
        raise ValueError("Missing Git commit timestamp")
    date = datetime.fromisoformat(timestamp.strip()).astimezone(ZoneInfo("Asia/Shanghai"))
    caption = message.partition("\n")[2].strip()
    return date, caption



def ingest(root: Path = ROOT, status: str = "published") -> int:
    if status not in {"published", "draft", "hidden"}:
        raise ValueError("Unknown publication status")
    root = Path(root).resolve()
    state = read_state(root)
    updated = copy.deepcopy(state)
    head = git(root, "rev-parse", "--verify", "HEAD^{commit}").decode().strip()
    commits = pending_commits(root, state["cursor"], head)
    if not commits:
        return 0
    batches = [(commit, changed_files(root, commit)) for commit in commits]
    last_change = {upload["path"]: index for index, (_, files) in enumerate(batches) for upload in files}
    prepared = []
    with tempfile.TemporaryDirectory(prefix=".fieldlog-ingest-", dir=root) as temporary:
        staging = Path(temporary)
        for index, (commit, files) in enumerate(batches):
            date, caption = commit_details(root, commit)
            uploads = [upload for upload in files if upload["status"] != "D"]
            for number, upload in enumerate(uploads, start=1):
                key = commit + ":" + upload["path"]
                if key in updated["events"]:
                    continue
                superseded = last_change[upload["path"]] > index
                if upload["mode"] not in {"100644", "100755"} or not OID.fullmatch(upload["blob_sha"]):
                    if superseded:
                        print(f"Skipped a replaced or removed nonregular upload: {upload['path']}")
                        continue
                    raise ValueError(f"Upload must be a regular image file, not a symlink or submodule: {upload['path']}")
                if PurePosixPath(upload["path"]).suffix.lower() not in EXTENSIONS:
                    if superseded:
                        print(f"Skipped a replaced or removed unsupported upload: {upload['path']}")
                        continue
                    raise ValueError(f"Unsupported upload: {upload['path']}; use JPG/JPEG, PNG, WebP, GIF or HEIC/HEIF")
                data = git(root, "cat-file", "blob", upload["blob_sha"])
                try:
                    converted = convert_image(data, upload["path"])
                except ValueError:
                    if not superseded:
                        raise
                    print(f"Skipped a replaced or removed invalid upload: {upload['path']}")
                    continue
                suffix = hashlib.sha256(key.encode("utf-8")).hexdigest()[:12]
                ident = date.strftime("%Y-%m-%d-%H%M%S") + "-" + suffix
                package = f"{CONTENT}/{date:%Y/%m}/{ident}"
                target = safe_destination(root, package)
                if target.exists() or any(item[1] == target for item in prepared):
                    raise ValueError(f"Post package already exists and will not be overwritten: {package}")
                filename = date.strftime("%Y%m%d-%H%M%S") + f"-{number:02d}" + ".webp"
                pending = staging / ident
                (pending / "assets").mkdir(parents=True)
                (pending / "assets" / filename).write_bytes(converted)
                label = f"{date.day} {MONTHS[date.month - 1]}, {date.year} {date:%H:%M}"
                meta = {"id": ident, "observation_id": date.strftime("%y%m%d%H%M%S"),
                        "date": date.isoformat(timespec="seconds"), "title": label,
                        "archive_status": "Archived",
                        "status": status, "image": "assets/" + filename,
                        "alt": "五月七日的自然观察影像"}
                meta = normalize_metadata(meta, site="fieldlog")
                validate_metadata(meta, site="fieldlog", schema_dir=ROOT / "schemas")
                (pending / "index.md").write_text(dump_frontmatter(meta) + "\n" + caption + "\n", encoding="utf-8")
                updated["events"][key] = {"id": ident, "commit": commit, "upload_path": upload["path"],
                                           "blob_sha": upload["blob_sha"], "sha256": hashlib.sha256(data).hexdigest(),
                                           "file_sha256": hashlib.sha256(converted).hexdigest(),
                                           "image_path": package + "/assets/" + filename,
                                           "route": f"{CONTENT}/{date:%Y/%m}/{ident}/"}
                prepared.append((pending, target))
        updated["cursor"] = head
        # All images and destinations are valid before any post or state changes.
        installed = []
        created_parents = []
        try:
            for pending, target in prepared:
                absent = []
                parent = target.parent
                while parent != root and not parent.exists():
                    absent.append(parent)
                    parent = parent.parent
                target.parent.mkdir(parents=True, exist_ok=True)
                created_parents.extend(reversed(absent))
                pending.rename(target)
                installed.append((pending, target))
            state_path = safe_destination(root, STATE_PATH.as_posix())
            temporary_state = None
            try:
                with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", prefix=".state-", dir=state_path.parent, delete=False) as handle:
                    temporary_state = Path(handle.name)
                    json.dump(updated, handle, ensure_ascii=False, indent=2)
                    handle.write("\n")
                os.replace(temporary_state, state_path)
            finally:
                if temporary_state is not None:
                    temporary_state.unlink(missing_ok=True)
        except BaseException:
            for pending, target in reversed(installed):
                target.rename(pending)
            for parent in reversed(created_parents):
                if parent.exists() and not any(parent.iterdir()):
                    parent.rmdir()
            raise
    return len(prepared)


def initialize(root: Path = ROOT, cursor: str = "HEAD") -> str:
    """Explicitly establish the initial queue boundary; never reset saved state."""
    root = Path(root).resolve()
    path = safe_destination(root, STATE_PATH.as_posix())
    if path.exists():
        raise ValueError("Publishing state already exists; refusing to reset its upload cursor")
    commit = git(root, "rev-parse", "--verify", cursor + "^{commit}").decode().strip()
    head = git(root, "rev-parse", "--verify", "HEAD^{commit}").decode().strip()
    pending_commits(root, commit, head)
    path.parent.mkdir(parents=True, exist_ok=True)
    state = {"version": 1, "cursor": commit, "events": {}}
    with path.open("x", encoding="utf-8") as handle:
        json.dump(state, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    return commit


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--status", choices=["published", "hidden", "draft"], default="published")
    parser.add_argument("--initialize-cursor", metavar="COMMIT",
                        help="Initialize the queue at a reviewed existing commit (once only)")
    arguments = parser.parse_args()
    if arguments.initialize_cursor:
        cursor = initialize(arguments.root, arguments.initialize_cursor)
        print(f"Initialized fieldlog upload cursor at {cursor}; commit the state file before importing uploads.")
    else:
        count = ingest(arguments.root, arguments.status)
        print(f"Imported {count} fieldlog images. Inbox originals retained.")

