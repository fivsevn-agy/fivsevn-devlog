"""Offline regression coverage for source integrity and both generated outputs."""
from copy import deepcopy
from datetime import datetime, timezone
import html
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

import feedparser
import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "intake"))
import build
from item_quality import article_key, clean_text, clean_title, deduplicate_sections, entry_date
from source_validation import audit_blocks, validate_blocks

ATOM = b'''<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">
<title>Fixture</title><entry><title>Fish &amp;amp; Chips</title>
<link href="https://example.org/read?id=1&amp;lang=en"/>
<published>2024-12-04T08:30:00+08:00</published>
<updated>2026-10-30T01:00:00Z</updated>
<summary type="html">&lt;p&gt;One&amp;nbsp; &amp;#8212; two&lt;/p&gt;</summary>
</entry><entry><title>Another article</title><link href="https://example.org/read?id=2"/>
<updated>2025-01-02T03:04:00Z</updated></entry></feed>'''


def response(content=ATOM):
    return Mock(content=content, url="https://example.org/feed", headers={"content-type": "application/atom+xml"})


def article(url, source="A", published="2024-01-01T00:00:00+00:00"):
    dt = datetime.fromisoformat(published) if published else None
    return dict(title="Same headline", link=url, source=source, summary="A & B < 3",
                published_dt=dt, published=build.format_datetime(dt),
                source_meta={"reliability_score": 4, "professional_value": 3})


class DateTests(unittest.TestCase):
    def test_atom_prefers_publication_over_update(self):
        entry = feedparser.parse(ATOM).entries[0]
        self.assertEqual(build.parse_entry_date(entry), datetime(2024, 12, 4, 0, 30, tzinfo=timezone.utc))

    def test_update_only_is_not_publication(self):
        entry = feedparser.parse(ATOM).entries[1]
        self.assertIsNone(build.parse_entry_date(entry))
        self.assertEqual(entry_date(dict(entry), "updated").year, 2025)

    def test_rfc_iso_offset_fraction_and_parsed_fallback(self):
        for value in ["Wed, 04 Dec 2024 00:30:00 GMT", "2024-12-04T08:30:00+08:00", "2024-12-04T00:30:00.000Z"]:
            self.assertEqual(build.parse_entry_date({"published": value}), datetime(2024, 12, 4, 0, 30, tzinfo=timezone.utc))
        self.assertEqual(build.parse_entry_date({"published_parsed": (2024, 12, 4, 0, 30, 0, 2, 339, 0)}).year, 2024)

    def test_unknown_dates_never_use_build_time(self):
        for entry in [{}, {"published": "broken"}, {"published": "2024-02-31T00:00:00Z"}, {"published": "2024-12-04"}, {"published": "2024-12-04T00:30:00"}, {"published_parsed": (1,)}]:
            self.assertIsNone(build.parse_entry_date(entry))
        self.assertIn("发布日期未知", build.format_datetime(None))

    def test_homepage_has_observation_time_not_a_fake_fetch_or_publication(self):
        item = build.make_link_source_item("A", "https://example.org")
        self.assertIsNone(item["published_dt"])
        self.assertEqual(item["published"], "")
        self.assertTrue(item["observed_dt"])
        self.assertNotIn("Published:", build.render_gpt_article(item))
        self.assertNotIn("Fetched:", build.render_gpt_article(item))

    def test_feedparser_normalization_does_not_invent_valid_dates(self):
        for value in ["2024-02-31T00:00:00Z", "2024-12-04", "2024-12-04T00:30:00"]:
            entry = feedparser.parse(f'<feed xmlns="http://www.w3.org/2005/Atom"><entry><published>{value}</published></entry></feed>').entries[0]
            self.assertIsNone(build.parse_entry_date(entry))


class TextTests(unittest.TestCase):
    def test_plain_text_title_preserves_code_notation(self):
        self.assertEqual(clean_title({"title": "std::vector&lt;T&gt; &amp; values", "title_detail": {"type": "text/plain"}}), "std::vector<T> & values")
        self.assertEqual(clean_title({"title": "<b>A</b> &amp; B", "title_detail": {"type": "text/html"}}), "A & B")

    def test_entities_markup_scripts_and_spacing(self):
        text = '&lt;p&gt;A&amp;nbsp;&amp;#8212; B&lt;/p&gt;<script>bad()</script><style>bad</style><p>C &amp;amp; D</p>'
        self.assertEqual(clean_text(text), "A — B C & D")
        self.assertEqual(clean_text('left<br>right &lt;3'), "left right <3")
        self.assertEqual(clean_text('x < 5 and y > 2'), "x < 5 and y > 2")

    def test_cleaning_and_escaping_agree_in_both_outputs(self):
        with patch.object(build.requests, "get", return_value=response()):
            items = build.fetch_feed("Fixture", "https://example.org/feed")
        first = next(i for i in items if "id=1" in i["link"])
        self.assertEqual(first["title"], "Fish & Chips")
        self.assertEqual(first["summary"], "One — two")
        rendered = build.render_article(first)
        context = build.render_gpt_article(first)
        self.assertIn("Fish &amp; Chips", rendered)
        self.assertIn("Fish & Chips", context)
        self.assertIn("id=1&amp;lang=en", rendered)
        self.assertIn("id=1&lang=en", context)
        self.assertNotIn("&amp;amp;", rendered)

    def test_unsafe_article_links_are_not_rendered(self):
        feed = Mock(entries=[{"link": "javascript:alert(1)", "title": "bad"}], bozo=False)
        with patch.object(build.requests, "get", return_value=response()), patch.object(build.feedparser, "parse", return_value=feed):
            self.assertEqual(build.fetch_feed("A", "https://example.org/feed"), [])

    def test_summary_cap_preserved(self):
        self.assertLessEqual(len(build.clamp_summary("x " * 2000)), build.SUMMARY_CHAR_CAP + 1)


class DedupTests(unittest.TestCase):
    def test_tracking_only_is_removed(self):
        self.assertEqual(article_key("https://EXAMPLE.org:443/a?id=1&utm_source=x&fbclid=y"), "https://example.org/a?id=1")
        for a, b in [("?id=1", "?id=2"), ("?lang=en", "?lang=zh"), ("?v=1", "?v=2"), ("?ref=a", "?ref=b"), ("#one", "#two"), ("/", ""), ("?a=1&a=2", "?a=2&a=1")]:
            self.assertNotEqual(article_key("https://example.org/a"+a), article_key("https://example.org/a"+b))

    def test_cross_source_merge_preserves_all_placements_and_scores(self):
        a = article("https://example.org/a?utm_source=a", "A")
        b = article("https://example.org/a?utm_source=b", "B")
        b["source_meta"]["reliability_score"] = 3
        data = {"science": [a, b], "ideas": [deepcopy(a)]}
        deduplicate_sections(data)
        self.assertEqual([len(x) for x in data.values()], [1, 1])
        records = data["science"][0]["attributions"]
        self.assertEqual({r["source"] for r in records}, {"A", "B"})
        self.assertEqual({r["section"] for r in records}, {"science", "ideas"})
        for render in (build.render_article, build.render_gpt_article):
            output = render(data["science"][0])
            for value in ("A", "B", "science", "ideas", "R3", "R4"):
                self.assertIn(value, output)

    def test_same_title_different_urls_and_homepages_survive(self):
        data = {"x": [article("https://a.org/?id=1"), article("https://a.org/?id=2"), article("https://b.org/?id=1"), build.make_link_source_item("A", "https://a.org/?id=1")]}
        deduplicate_sections(data)
        self.assertEqual(len(data["x"]), 4)

    def test_regions_and_unknown_dates_survive(self):
        a = article("https://example.org/a", published="")
        b = deepcopy(a)
        a["region"], b["region"] = "global", "europe"
        data = {"x": [a, b]}
        deduplicate_sections(data)
        self.assertEqual(len(data["x"]), 2)

    def test_latest_update_wins_when_duplicate_publication_dates_match(self):
        old = article("https://example.org/a", "A")
        new = deepcopy(old)
        new["summary"] = "Corrected summary"
        new["updated_dt"] = datetime(2026, 1, 1, tzinfo=timezone.utc)
        data = {"x": [old, new]}
        deduplicate_sections(data)
        self.assertEqual(data["x"][0]["summary"], "Corrected summary")

    def test_feed_cap_is_applied_after_dedup_and_keeps_query_ids(self):
        entries = [dict(title="Same", link=url) for url in ["https://e.org/?id=1", "https://e.org/?id=1&utm_source=x", "https://e.org/?id=2", "https://e.org/?id=3"]]
        feed = Mock(entries=entries, bozo=False)
        with patch.object(build.requests, "get", return_value=response()), patch.object(build.feedparser, "parse", return_value=feed):
            items = build.fetch_feed("A", "https://e.org/feed", 2)
        self.assertEqual([i["link"] for i in items], ["https://e.org/?id=1", "https://e.org/?id=2"])
        grouped = {"science": items}
        deduplicate_sections(grouped)
        records = grouped["science"][0]["attributions"]
        self.assertEqual({r["url"] for r in records}, {"https://e.org/?id=1", "https://e.org/?id=1&utm_source=x"})


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.blocks = build.read_yaml_blocks((ROOT / "intake/sources.md").read_text())

    def test_current_registry_and_manuals(self):
        result = validate_blocks(self.blocks)
        self.assertGreaterEqual(result["source_count"], 682)
        self.assertEqual(result["section_count"], 62)
        self.assertEqual(result["cross_section_conflicts"], [])
        sources = [b for k, b in self.blocks if k == "source"]
        manuals = [s for s in sources if s["source_type"] == "manual"]
        self.assertTrue({"SONY PCM-A10 Help Guide", "Suunto Vertical User Guide (ZH)"} <= {s["name"] for s in manuals})
        for name, section in [("NOWFASHION", "fashion_style"), ("Pixabay", "reference_pool")]:
            source = next(s for s in sources if s["name"] == name)
            self.assertEqual(source["section"], section)
            self.assertEqual(source["feed_url"], "")
            self.assertTrue(source["review"]["evidence"])

    def test_duplicate_yaml_keys_fail(self):
        with self.assertRaises(ValueError):
            build.read_yaml_blocks('```source\nname: A\nname: B\n```')

    def test_invalid_source_fields_fail(self):
        for field, value in [("reliability_score", True), ("professional_value", 6), ("source_type", "typo"), ("section", "missing"), ("site_url", "javascript:x"), ("feed_url", "’‘"), ("source_cap", -1)]:
            blocks = deepcopy(self.blocks)
            next(b for k, b in blocks if k == "source")[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_blocks(blocks)

    def test_orphan_or_duplicate_sections_fail(self):
        blocks = deepcopy(self.blocks)
        blocks.append(("section", {"id": "orphan"}))
        with self.assertRaises(ValueError):
            validate_blocks(blocks)
        with self.assertRaises(ValueError):
            validate_blocks(self.blocks + [next(b for b in self.blocks if b[0] == "section")])

    def test_r_conflicts_are_audit_findings_not_automatic_changes(self):
        blocks = deepcopy(self.blocks)
        rows = [b for k, b in blocks if k == "source" and b["name"] == "iFixit News"]
        rows[0]["reliability_score"] = 2
        result = audit_blocks(blocks)
        self.assertEqual(len(result["cross_section_conflicts"]), 1)
        self.assertEqual(rows[0]["reliability_score"], 2)

    def test_incomplete_review_fails(self):
        blocks = deepcopy(self.blocks)
        next(b for k, b in blocks if k == "source")["review"] = {"status": "reviewed"}
        with self.assertRaises(ValueError):
            validate_blocks(blocks)


class BuildTests(unittest.TestCase):
    def test_failed_empty_disabled_and_link_only_sources_remain(self):
        source = dict(name="Keep me", site_url="https://example.org", feed_url="https://example.org/feed", source_cap=6)
        for result in (requests.Timeout("timeout"), [], None):
            config = {"disabled_feeds": ["Keep me"]} if result is None else {}
            with patch.object(build, "fetch_feed", side_effect=result if isinstance(result, Exception) else None, return_value=result or []) as fetch:
                items = build.build_section("x", {"feeds": [source]}, config)
            self.assertEqual(len(items), 1)
            self.assertTrue(items[0]["is_source_link"])
            self.assertEqual(items[0]["link"], source["site_url"])
            if result is None:
                fetch.assert_not_called()
        for feed_url, cap in [("", 0), ("https://example.org/feed", 0)]:
            with patch.object(build, "fetch_feed") as fetch:
                self.assertTrue(build.build_section("x", {"feeds": [dict(source, feed_url=feed_url, source_cap=cap)]}, {})[0]["is_source_link"])
                fetch.assert_not_called()

    def test_full_registry_offline_generation_is_consistent(self):
        base = yaml.safe_load((ROOT / "intake/feeds.yml").read_text())
        config = build.build_config_from_sources_markdown(base, (ROOT / "intake/sources.md").read_text())
        with patch.object(build.requests, "get", return_value=response()), patch("builtins.print"):
            data = {key: build.build_section(key, section, config) for key, section in config["sections"].items()}
        deduplicate_sections(data)
        when = datetime(2026, 10, 30, 4, 59, tzinfo=timezone.utc)
        with patch.object(build, "load_fragment", return_value=""):
            page = build.render_html(config, data, when)
            context = build.render_gpt_markdown(config, data, when)
        self.assertEqual(page.count('<article class="article">'), sum(map(len, data.values())))
        self.assertEqual(context.count("\n### "), sum(map(len, data.values())))
        for value in ("2026-10-30 04:59 UTC", "NOWFASHION", "Pixabay", "发布日期未知"):
            self.assertIn(value, page)
            self.assertIn(value, context)
        for items in data.values():
            for item in items:
                self.assertIn(html.escape(item["link"], quote=True), page)
                self.assertIn(item["link"], context)


if __name__ == "__main__":
    unittest.main()
