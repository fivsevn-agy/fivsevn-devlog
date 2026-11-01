#!/usr/bin/env python3
"""Offline metadata contract for the fivsevn publication boards.

Canonical files use the shared core schema plus site-post-v1. Compatibility
views are transient dictionaries: never write metadata_view() back to disk.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import date, datetime
import json
from pathlib import Path
import re
from typing import Any
from zoneinfo import ZoneInfo

import yaml

PROFILE = "site-post-v1"
PUBLISHED_STATUSES = frozenset({"active", "publish", "published"})
SITES = ("flux", "savour", "fieldlog", "stills", "motion", "sys", "cctv")
TZ = ZoneInfo("Asia/Shanghai")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
CORE_FIELDS = frozenset({
    "id", "title", "module", "submodule", "topic", "type", "status", "canonical", "summary",
    "parents", "related", "tags", "audience", "languages", "maturity", "confidence", "visibility",
    "source_of_truth", "created", "updated", "metadata_updated", "filename_policy", "note", "aliases",
    "subtitle", "references", "rights", "archive_url", "original_title", "original_source",
    "original_publisher", "original_url", "translation_note", "layout", "lang", "description",
    "canonical_url", "permalink", "legacy", "extra",
})
RUNTIME_FIELDS = frozenset({
    "author", "image", "alt", "observation_id", "annotation_date", "source", "sync", "upload",
    "source_hash", "source_key", "publish_slug", "wp_slug", "wp_post_id", "wp_id", "wp_url",
    "source_wp_id", "source_url", "source_image",
})
GROUPS = (
    ("id", "title"), ("module", "submodule", "topic"), ("type", "status", "canonical"),
    ("summary",), ("parents", "related"), ("tags",), ("audience", "languages"),
    ("maturity", "confidence"), ("visibility", "source_of_truth"),
    ("original_title", "original_source", "original_publisher", "original_url", "translation_note"),
    ("subtitle", "references", "rights", "archive_url", "aliases", "note", "filename_policy"),
    ("layout", "lang", "description", "canonical_url", "permalink"),
    ("created", "updated", "metadata_updated"), ("extra",), ("legacy",),
)


class UniqueLoader(yaml.SafeLoader):
    """A repeated key is an error rather than a silently discarded value."""


def _unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _unique_mapping)


def _plain(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_plain(item) for item in value]
    return value


def read_frontmatter(value: str | Path) -> tuple[dict, str]:
    """Read a Path or parse a string; preserve the complete body after the fence.

    A file without a fence is a free-form trigger, returned as ({}, original).
    A starting fence that is malformed, repeated keys, or nonmapping YAML fails.
    """
    text = value.read_text(encoding="utf-8") if isinstance(value, Path) else value
    if not isinstance(text, str):
        raise ValueError("Frontmatter input must be text or a pathlib.Path")
    content = text.lstrip("\ufeff")
    if not re.match(r"\A---(?:\r?\n|$)", content):
        return {}, text
    match = re.match(r"\A---\r?\n(?:(.*?)\r?\n)?---(?:\r?\n|$)(.*)\Z", content, re.S)
    if not match:
        raise ValueError("missing or unclosed frontmatter")
    try:
        meta = yaml.load(match[1] or "", Loader=UniqueLoader) or {}
    except yaml.YAMLError as error:
        raise ValueError(f"Invalid YAML frontmatter: {error}") from error
    if not isinstance(meta, dict):
        raise ValueError("frontmatter must be a mapping")
    return _plain(meta), match[2]


parse_frontmatter = read_frontmatter


def _datetime(value: Any) -> datetime:
    if isinstance(value, datetime):
        result = value
    elif isinstance(value, str):
        try:
            result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError as error:
            raise ValueError(f"Invalid publication timestamp: {value!r}") from error
    else:
        raise ValueError("A publication timestamp with an explicit timezone is required")
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError("Publication timestamp requires an explicit timezone")
    return result


def published_datetime(meta: dict) -> datetime:
    """Return the precise instant; old date is supported only for input adapters."""
    extra = meta.get("extra", {})
    if isinstance(extra, dict) and "published_at" in extra:
        return _datetime(extra["published_at"])
    return _datetime(meta.get("date"))


def is_published(meta: dict) -> bool:
    return meta.get("visibility") == "public" and meta.get("status") in PUBLISHED_STATUSES


def _content_date(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, (date, datetime)):
        return value.date().isoformat() if isinstance(value, datetime) else value.isoformat()
    if not isinstance(value, str):
        raise ValueError("Content dates must use YYYY-MM-DD or null")
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as error:
        raise ValueError(f"Content date must use YYYY-MM-DD: {value!r}") from error


def normalize_metadata(raw: dict, *, site: str, post_id=None, published_at=None) -> dict:
    """Fill missing defaults, retain deliberate controls, and preserve old facts.

    post_id and published_at are source-derived fallbacks, never substitutes for
    an existing ID or timestamp. This function does not infer a time from mtime.
    Existing canonical metadata is idempotent, including on a subsequent day.
    """
    if site not in SITES:
        raise ValueError(f"Unknown site: {site!r}")
    if not isinstance(raw, dict):
        raise ValueError("Metadata must be a mapping")
    original = _plain(deepcopy(raw))
    extra = deepcopy(original.get("extra") or {})
    legacy = deepcopy(original.get("legacy") or {})
    if not isinstance(extra, dict) or not isinstance(legacy, dict):
        raise ValueError("extra and legacy must be mappings")
    legacy_metadata = deepcopy(legacy.get("metadata") or {})
    if not isinstance(legacy_metadata, dict):
        raise ValueError("legacy.metadata must be a mapping")
    ident = original.get("id", post_id)
    if ident is None or str(ident).strip() == "":
        raise ValueError("A stable post id or post_id fallback is required")
    ident = str(ident)
    if post_id is not None and ident != str(post_id):
        raise ValueError("Existing post id differs from its package; refusing to rename it")
    timestamp_value = extra.get("published_at", original.get("date", published_at))
    timestamp = _datetime(timestamp_value)
    stamp = timestamp.isoformat()
    local = timestamp.astimezone(TZ)
    default_title = f"{local.day} {MONTHS[local.month - 1]}, {local.year} {local:%H:%M}"
    title = str(original.get("title") or "").strip() or default_title
    module, submodule, truth = {
        "flux": ("posts", "flux", "site"),
        "savour": ("savour", str(local.year), "site"),
        "fieldlog": ("natsci", "fieldlog", "devlog"),
        "stills": ("stills", "roll", "site"),
        "motion": ("motion", "roll", "site"),
        "sys": ("57store", "sys", "site"),
        "cctv": ("57store", "cctv", "site"),
    }[site]
    defaults = {
        "id": ident, "title": title, "module": module, "submodule": submodule, "topic": None,
        "type": "log", "status": "published", "canonical": True, "summary": None,
        "parents": [], "related": [], "tags": [], "audience": ["public"], "languages": ["zh"],
        "maturity": "evolving", "confidence": None, "visibility": "public", "source_of_truth": truth,
        "filename_policy": "entrypoint",
    }
    meta = {key: deepcopy(original.get(key, value)) for key, value in defaults.items()}
    # Site identity and a package's fixed index filename are structural facts.
    for key, value in {"id": ident, "title": title, "module": module, "submodule": submodule,
                       "filename_policy": "entrypoint"}.items():
        if key in original and original[key] != value:
            legacy_metadata.setdefault(key, deepcopy(original[key]))
        meta[key] = value
    for key, value in original.items():
        if key in CORE_FIELDS and key not in meta and key not in {"extra", "legacy", "created", "updated", "metadata_updated"}:
            meta[key] = deepcopy(value)
    for key in ("status", "visibility"):
        if isinstance(meta[key], str):
            meta[key] = meta[key].strip().lower()
    content_day = local.date().isoformat()
    meta["created"] = _content_date(original.get("created", content_day))
    meta["updated"] = _content_date(original.get("updated", meta["created"]))
    for key, value in original.items():
        if key in RUNTIME_FIELDS or key.startswith("wp_") or (key.startswith("source_") and key != "source_of_truth"):
            if key in extra and extra[key] != value:
                legacy_metadata.setdefault(key, deepcopy(value))
            else:
                extra[key] = deepcopy(value)
        elif key not in CORE_FIELDS and key not in {"date", "archive_status"}:
            legacy_metadata.setdefault(key, deepcopy(value))
    if "date" in original and "published_at" in extra and _plain(original["date"]) != extra["published_at"]:
        legacy_metadata.setdefault("date", original["date"])
    if "profile" in extra and extra["profile"] != PROFILE:
        legacy_metadata.setdefault("extra.profile", extra["profile"])
    extra["profile"] = PROFILE
    extra["published_at"] = stamp
    if not str(extra.get("author") or "").strip():
        extra["author"] = "五月七日"
    if "image" in extra and extra["image"] is None:
        extra.pop("image")
    extra.setdefault("alt", title)
    if site == "fieldlog":
        extra.setdefault("observation_id", local.strftime("%y%m%d%H%M%S"))
        extra.setdefault("display_status", original.get("archive_status", "Archived"))
    elif "archive_status" in original:
        extra.setdefault("display_status", original["archive_status"])
    meta["extra"] = extra
    if legacy_metadata:
        legacy["metadata"] = legacy_metadata
    if legacy:
        meta["legacy"] = legacy
    old_updated = original.get("metadata_updated")
    # Compare complete dictionaries apart from the bookkeeping date itself.
    comparable = {key: value for key, value in original.items() if key != "metadata_updated"}
    meta["metadata_updated"] = (_content_date(old_updated) if meta == comparable and old_updated
                                else datetime.now(TZ).date().isoformat())
    return meta


def metadata_view(meta: dict) -> dict:
    """Expose legacy rendering/ingest keys without changing canonical storage."""
    view = {}
    legacy = meta.get("legacy")
    if isinstance(legacy, dict) and isinstance(legacy.get("metadata"), dict):
        view.update(deepcopy(legacy["metadata"]))
    extra = meta.get("extra")
    if isinstance(extra, dict):
        view.update({key: deepcopy(value) for key, value in extra.items()
                     if key not in {"profile", "published_at", "display_status"}})
        if "published_at" in extra:
            view["date"] = extra["published_at"]
        if "display_status" in extra:
            view["archive_status"] = extra["display_status"]
    view.update(deepcopy(meta))
    return view


def _schema_directory(value=None) -> Path:
    if value is not None:
        return Path(value).resolve()
    root = Path(__file__).resolve().parents[1]
    for candidate in (root / "schemas", root / "content"):
        if (candidate / "content-metadata.schema.json").is_file() and (candidate / "site-post.schema.json").is_file():
            return candidate
    raise ValueError("Local metadata schemas are missing; pass schema_dir explicitly")


def validate_metadata(meta: dict, *, site=None, schema_dir=None) -> None:
    """Validate against local core/profile schemas only; never fetch a remote ref."""
    from jsonschema import Draft202012Validator, FormatChecker
    from referencing import Registry, Resource
    directory = _schema_directory(schema_dir)
    registry = Registry()
    schemas = {}
    for name in ("content-metadata.schema.json", "site-post.schema.json"):
        schema = json.loads((directory / name).read_text(encoding="utf-8"))
        schemas[name] = schema
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    validator = Draft202012Validator(schemas["site-post.schema.json"], registry=registry, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(_plain(meta)), key=lambda e: tuple(map(str, e.absolute_path)))
    if errors:
        raise ValueError("; ".join((".".join(map(str, e.absolute_path)) or "metadata") + ": " + e.message for e in errors))
    if meta.get("created") and meta.get("updated") and str(meta["updated"]) < str(meta["created"]):
        raise ValueError("updated precedes created")
    if site is not None:
        if site not in SITES:
            raise ValueError(f"Unknown site: {site!r}")
        identity = (meta["module"], meta["submodule"])
        expected = {"flux": ("posts", "flux"), "fieldlog": ("natsci", "fieldlog"),
                    "savour": ("savour", str(published_datetime(meta).astimezone(TZ).year)),
                    "stills": ("stills", "roll"), "motion": ("motion", "roll"),
                    "sys": ("57store", "sys"), "cctv": ("57store", "cctv")}[site]
        if identity != expected:
            raise ValueError(f"Site identity must be {expected!r}, got {identity!r}")
    published_datetime(meta)


def dump_frontmatter(meta: dict) -> str:
    """Return canonical, grouped YAML including both --- fences and final newline."""
    unknown = set(meta) - CORE_FIELDS
    if unknown:
        raise ValueError("Only canonical metadata can be serialized: " + ", ".join(sorted(unknown)))
    groups, emitted = [], set()
    for keys in GROUPS:
        values = {key: _plain(meta[key]) for key in keys if key in meta}
        if values:
            groups.append(yaml.safe_dump(values, allow_unicode=True, sort_keys=False, width=100).rstrip())
            emitted.update(values)
    if set(meta) != emitted:
        raise ValueError("Metadata serialization order is missing fields: " + ", ".join(sorted(set(meta)-emitted)))
    return "---\n" + "\n\n".join(groups) + "\n---\n"


def post_paths(root: Path) -> list[Path]:
    """Only saved post packages, never trigger files or ordinary index pages."""
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError(f"Content root does not exist: {root}")
    result = []
    candidates = list(root.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*/index.md"))
    if (root / "bygone/index.md").is_file():
        candidates.append(root / "bygone/index.md")
    for path in sorted(candidates):
        if any(part.startswith((".", "_")) for part in path.relative_to(root).parts):
            continue
        if any(p.is_symlink() for p in [path, *path.parents] if p.is_relative_to(root)):
            raise ValueError(f"Post package follows a symlink: {path}")
        result.append(path)
    return result


def check_packages(root: Path, *, site=None, schema_dir=None) -> dict:
    root = Path(root).resolve()
    result = {"documents": 0, "errors": [], "warnings": [], "pending_drafts": []}
    ids = {}
    for path in post_paths(root):
        result["documents"] += 1
        try:
            meta, _ = read_frontmatter(path)
            validate_metadata(meta, site=site, schema_dir=schema_dir)
            ident = meta["id"]
            local = published_datetime(meta).astimezone(TZ)
            folder = local.strftime("%Y-%m-%d-%H%M%S-") + ident if site == "motion" else ident
            expected = root / local.strftime("%Y/%m") / folder / "index.md"
            if site == "stills" and ident == "bygone":
                expected = root / "bygone/index.md"
                if meta["extra"].get("mode") != "collection":
                    raise ValueError("Bygone must be an independent collection")
            if path != expected:
                raise ValueError("package directory must match its stable id and publication date")
            if ident in ids:
                raise ValueError(f"duplicate id also in {ids[ident]}")
            ids[ident] = str(path.relative_to(root))
        except (ValueError, TypeError, KeyError, OSError) as error:
            result["errors"].append(f"{path.relative_to(root)}: {error}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("normalize", "check"))
    parser.add_argument("--site", choices=SITES, required=True)
    parser.add_argument("--root", type=Path, required=True, help="Content root containing YYYY/MM/id/index.md")
    parser.add_argument("--schema-dir", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == "normalize":
        prepared = []
        for path in post_paths(root):
            raw, body = read_frontmatter(path)
            meta = normalize_metadata(raw, site=args.site, post_id=raw.get("id") if args.site == "motion" else path.parent.name)
            validate_metadata(meta, site=args.site, schema_dir=args.schema_dir)
            prepared.append((path, dump_frontmatter(meta) + body))
        # Validate every package before writing any file; bodies and paths stay intact.
        for path, text in prepared:
            if path.read_text(encoding="utf-8") != text:
                path.write_text(text, encoding="utf-8")
    result = check_packages(root, site=args.site, schema_dir=args.schema_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(result["errors"]))


if __name__ == "__main__":
    raise SystemExit(main())
