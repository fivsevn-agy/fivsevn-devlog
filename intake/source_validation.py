"""Structural checks and a review queue, never automatic source re-rating."""
from __future__ import annotations

from collections import defaultdict
from datetime import date
from typing import Any

import yaml

from item_quality import http_url, article_key

ENUMS = {
    "source_type": set("wire_service public_broadcaster newspaper_magazine institutional journal specialist_media trade_publication culture_magazine reference_tool aggregator community personal_site data_source preprint video_channel manual".split()),
    "authority_level": set("primary specialist generalist aggregator commentary community".split()),
    "use_role": set("baseline signal reference counterpoint culture_probe archive tool".split()),
}


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def audit_blocks(blocks: list[tuple[str, dict[str, Any]]]) -> dict[str, Any]:
    errors: list[str] = []
    sources = [b for kind, b in blocks if kind == "source"]
    sections = [b.get("id") for kind, b in blocks if kind == "section"]
    catalogs = [b for kind, b in blocks if kind == "categories"]
    if len(catalogs) != 1:
        errors.append("Exactly one categories block is required")
    if len(sections) != len(set(sections)) or not all(sections):
        errors.append("Section IDs must be nonempty and unique")
    listed = [key for c in catalogs for category in c.values() for key in category.get("sections", [])]
    if set(listed) != set(sections) or len(listed) != len(set(listed)):
        errors.append("Each declared section must belong to exactly one first-level category")
    seen = set()
    groups = defaultdict(list)
    pending = []
    for src in sources:
        label = f"{src.get('name')} [{src.get('section')}]"
        if not isinstance(src.get("name"), str) or not src["name"].strip():
            errors.append(f"{label}: missing name")
        if src.get("section") not in sections:
            errors.append(f"{label}: unknown section")
        for field, allowed in ENUMS.items():
            if not isinstance(src.get(field), str) or src[field] not in allowed:
                errors.append(f"{label}: invalid {field}")
        for field in ("reliability_score", "professional_value"):
            value = src.get(field)
            if type(value) is not int or not 1 <= value <= 5:
                errors.append(f"{label}: {field} must be an integer from 1 to 5")
        cap = src.get("source_cap")
        if type(cap) is not int or cap < 0:
            errors.append(f"{label}: source_cap must be a nonnegative integer")
        for field in ("site_url", "feed_url"):
            value = src.get(field)
            if not isinstance(value, str) or (not value and field == "site_url") or (value and not http_url(value)):
                errors.append(f"{label}: invalid {field}")
        if not src.get("feed_url") and cap != 0:
            errors.append(f"{label}: URL-only sources require source_cap: 0")
        key = (src.get("name"), src.get("section"))
        if key in seen:
            errors.append(f"{label}: duplicate source placement")
        seen.add(key)
        review = src.get("review")
        if review is not None:
            if not isinstance(review, dict):
                errors.append(f"{label}: review must be a mapping")
            else:
                required = ("scope", "identity", "reliability", "professional_value", "limitations", "access")
                if review.get("status") not in {"reviewed", "partial"}:
                    errors.append(f"{label}: invalid review status")
                for field in required:
                    if not isinstance(review.get(field), str) or not review[field].strip():
                        errors.append(f"{label}: missing review.{field}")
                try:
                    date.fromisoformat(review.get("checked", ""))
                except (ValueError, TypeError):
                    errors.append(f"{label}: review.checked must be an ISO date string")
                evidence = review.get("evidence")
                if not isinstance(evidence, list) or not evidence or not all(isinstance(url, str) and http_url(url) for url in evidence):
                    errors.append(f"{label}: review.evidence requires HTTP(S) URLs")
        if not isinstance(review, dict) or review.get("status") != "reviewed":
            pending.append({"name": src.get("name"), "section": src.get("section"), "status": (review or {}).get("status", "unreviewed") if isinstance(review, dict) else "unreviewed"})
        if http_url(src.get("site_url")):
            # A shared homepage is a review candidate, not proof of identity.
            groups[article_key(src["site_url"]).rstrip("/")].append(src)
    conflicts = []
    for url, rows in groups.items():
        fields = [field for field in ("source_type", "authority_level", "reliability_score") if len({row.get(field) for row in rows}) > 1]
        if fields:
            conflicts.append({"site_url": url, "fields": fields, "sources": [{k: r.get(k) for k in ("name", "section", *fields)} for r in rows]})
    return {"source_count": len(sources), "section_count": len(sections), "errors": errors,
            "cross_section_conflicts": conflicts, "pending_reviews": pending}


def validate_blocks(blocks):
    result = audit_blocks(blocks)
    if result["errors"]:
        raise ValueError("Invalid intake registry:\n" + "\n".join(result["errors"]))
    return result
