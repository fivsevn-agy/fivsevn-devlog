"""Check saved translation openings and image exclusions without fetching sources."""
from __future__ import annotations

import argparse
from datetime import date, datetime
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
MODULES = ("posts", "natsci", "netcom")
TRANSLATION_TYPES = {"translation", "traslation"}
IMAGE_SUFFIXES = {
    ".apng", ".avif", ".bmp", ".gif", ".heic", ".heif", ".ico", ".jfif",
    ".jp2", ".jpeg", ".jpg", ".jxl", ".png", ".psd", ".svg", ".svgz",
    ".tif", ".tiff", ".webp",
}
IMAGE_TAGS = {"img", "picture", "svg", "image", "canvas", "object", "embed"}
IMAGE_HOSTS = {"images.aeonmedia.co", "images.unsplash.com", "images.squarespace-cdn.com"}


def visible_markup(text: str) -> str:
    """Remove fenced and inline code examples, retaining other Markdown and HTML."""
    lines = []
    fence = None
    for line in text.splitlines():
        if fence is not None:
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*", line):
                fence = None
            lines.append("")
            continue
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if match and (match[1][0] != "`" or "`" not in match[2]):
            fence = match[1]
            lines.append("")
        else:
            lines.append(line)
    return re.sub(r"(?<!`)(`+)(?!`)(.*?)\1(?!`)", "", "\n".join(lines), flags=re.S)


def image_resource(target: str) -> bool:
    value = unescape(unquote(target)).strip().strip("<>")
    if value.lower().startswith("data:image/"):
        return True
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    if Path(parsed.path).suffix.lower() in IMAGE_SUFFIXES:
        return True
    if (parsed.hostname or "").lower() in IMAGE_HOSTS:
        return True
    # These are image-rendering query parameters, including extensionless CDNs.
    return bool(re.search(r"(?:^|&)(?:format|fm)=(?:png|jpe?g|gif|webp|avif|svg)(?:&|$)", parsed.query, re.I))


class ImageMarkup(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.targets = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if (
            tag.split(":")[-1] in IMAGE_TAGS
            or (tag == "input" and values.get("type", "").lower() == "image")
            or (tag == "link" and values.get("as", "").lower() == "image")
            or values.get("poster")
            or (tag == "source" and values.get("srcset"))
        ):
            self.tags.append(tag)
        for key, value in attrs:
            if value and key in {"src", "href", "data", "poster", "srcset"}:
                self.targets.extend(value.split() if key == "srcset" else [value])


def image_errors(markup: str) -> list[str]:
    errors = []
    if re.search(r"(?<!\\)!\[", markup):
        errors.append("Markdown image embedding is not allowed")
    parser = ImageMarkup()
    parser.feed(markup)
    if parser.tags:
        errors.append("HTML image embedding is not allowed: " + ", ".join(sorted(set(parser.tags))))
    if re.search(r"\b(?:background(?:-image)?|content|mask(?:-image)?|border-image(?:-source)?|shape-outside)\s*:[^;{}]*url\(", markup, re.I):
        errors.append("CSS image embedding is not allowed")
    targets = list(parser.targets)
    targets += re.findall(r"https?://[^\s<>\"']+", markup)
    targets += re.findall(r"\[[^\]\n]*\]\(([^\n]*?)\)", markup)
    targets += [a or b for a, b in re.findall(r"(?m)^ {0,3}\[[^\]\n]+\]:\s*(?:<([^>]+)>|(\S+))", markup)]
    targets += re.findall(r"url\(\s*[\"']?([^\s\"')]+)", markup, re.I)
    if "data:image/" in markup.lower() or any(image_resource(t.rstrip(").,;")) for t in targets):
        errors.append("Direct image-resource links are not allowed; link to the source article")
    return errors


def image_file(path: Path) -> bool:
    if path.suffix.lower() in IMAGE_SUFFIXES:
        return True
    with path.open("rb") as stream:
        header = stream.read(512)
    return (
        header.startswith((b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff", b"GIF87a", b"GIF89a", b"BM", b"II*\x00", b"MM\x00*", b"\x00\x00\x01\x00", b"8BPS"))
        or (header[:4] == b"RIFF" and header[8:12] == b"WEBP")
        or (header[4:8] == b"ftyp" and header[8:12] in {b"avif", b"avis", b"heic", b"heix", b"mif1"})
        or bool(re.search(rb"<svg(?:\s|>)", header, re.I))
    )


def display_date(value) -> str | None:
    if value is None:
        return "未标注"
    if isinstance(value, date) and not isinstance(value, datetime):
        return value.strftime("%Y.%m.%d")
    if isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        try:
            return date.fromisoformat(value).strftime("%Y.%m.%d")
        except ValueError:
            pass
    return None


def check_page(path: Path, meta: dict, body: str) -> list[str]:
    markup = visible_markup(body)
    errors = image_errors(markup)
    lines = markup.splitlines()
    labels = {}
    for label in ("SOURCE", "NOTE"):
        positions = [i for i, line in enumerate(lines) if re.fullmatch(r"(?:#{1,6}\s+)?(?:\*\*)?" + label + r"(?:\*\*)?", line.strip(), re.I)]
        if len(positions) != 1 or lines[positions[0]].strip() != label:
            errors.append(f"{label} must occur once as a plain uppercase text line")
        else:
            labels[label] = positions[0]

    extra = meta.get("extra")
    if not isinstance(extra, dict):
        extra = {}
    author = extra.get("original_author")
    if not isinstance(author, str) or not author.strip() or "\n" in author:
        errors.append("extra.original_author must be a nonempty single-line string")
    published = display_date(extra.get("original_published"))
    if "original_published" not in extra or published is None:
        errors.append("extra.original_published must be an ISO date or explicit null")
    for field in ("original_title", "original_source", "original_url"):
        if not isinstance(meta.get(field), str) or not meta[field].strip():
            errors.append(f"{field} must be a nonempty string")

    if len(labels) == 2:
        if labels["SOURCE"] >= labels["NOTE"]:
            errors.append("SOURCE must precede NOTE")
        else:
            source_lines = [line.strip() for line in lines[labels["SOURCE"] + 1:labels["NOTE"]] if line.strip()]
            # Keep existing fragment links without making them visible SOURCE content.
            source_lines = [line for line in source_lines if not re.fullmatch(r'<a\s+(?:id|name)=["\'][^"\']+["\']\s*></a>', line)]
            if len(source_lines) != 2:
                errors.append("SOURCE must contain exactly the original-title link and one author/source/date line")
            else:
                link = re.fullmatch(r"\[((?:\\.|[^\]\\])*)\]\((.+)\)", source_lines[0])
                if not link:
                    errors.append("SOURCE must start with the original-title Markdown link")
                else:
                    title = unescape(re.sub(r"\\([\\`*_{}\[\]()#+\-.!|>])", r"\1", link[1]))
                    if title != meta.get("original_title"):
                        errors.append("SOURCE title does not match original_title")
                    if unescape(link[2]).strip("<>") != meta.get("original_url"):
                        errors.append("SOURCE link does not match original_url")
                expected = f"作者：{author} · 来源：{meta.get('original_source')} · 日期：{published}"
                if source_lines[1] != expected:
                    errors.append("SOURCE author/source/date line does not match metadata")
    if path.name == "index.md":
        assets = path.parent / "assets"
        for resource in sorted(assets.rglob("*")) if assets.exists() else []:
            if resource.is_file() and image_file(resource):
                errors.append("Translation package retains an image file: " + resource.relative_to(path.parent).as_posix())
    return errors


def check_repository(root: Path) -> dict:
    checked = 0
    errors = []
    for module in MODULES:
        for path in sorted((root / module).rglob("*.md")):
            text = path.read_text(encoding="utf-8-sig")
            match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", text, re.S)
            if not match:
                continue
            try:
                meta = yaml.safe_load(match[1])
            except yaml.YAMLError:
                if re.search(r"(?m)^type:\s*[\"']?(?:translation|traslation)\b", match[1]):
                    errors.append(f"{path.relative_to(root)}: invalid translation frontmatter")
                continue
            if not isinstance(meta, dict) or str(meta.get("type", "")).strip().lower() not in TRANSLATION_TYPES:
                continue
            checked += 1
            errors.extend(f"{path.relative_to(root)}: {error}" for error in check_page(path, meta, match[2]))
    return {"translations": checked, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    result = check_repository(args.root.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
