"""Regression checks for source attribution and source-only illustration links."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import yaml

import check_translation_pages as checks


class TranslationPagesTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def article(self, *, content="Text.", published="2026-11-04", note_type="translation", status="active"):
        path = self.root / "posts/2026/11/example/index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        meta = {
            "type": note_type, "status": status, "original_title": "An [original] title",
            "original_url": "https://example.com/article", "original_source": "Example",
            "extra": {"original_author": "A. Author", "original_published": published},
        }
        date = published.replace("-", ".") if published else "未标注"
        body = (
            "# ◇ 主题\n\nSOURCE\n\n[An \\[original\\] title](https://example.com/article)\n\n"
            f"作者：A. Author · 来源：Example · 日期：{date}\n\n"
            '<a id="note"></a>\n\nNOTE\n\nA note.\n\n---\n\n' + content + "\n"
        )
        path.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True) + "---\n\n" + body)
        return path

    def errors(self):
        return checks.check_repository(self.root)["errors"]

    def test_missing_publication_date_and_article_image_link_are_valid(self):
        self.article(published=None, content="图注。[前往原文查看配图](https://example.com/article)")
        self.assertEqual(self.errors(), [])

    def test_attribution_must_match_metadata_and_labels_are_plain(self):
        replacements = [
            ("SOURCE\n", "## SOURCE\n"),
            ("作者：A. Author", "作者：Other"),
            ("来源：Example", "来源：Other"),
            ("日期：2026.11.04", "日期：2026.11.05"),
            ("[An \\[original\\] title]", "[Short title]"),
            ("](https://example.com/article)", "](https://example.com/other)"),
        ]
        for old, new in replacements:
            with self.subTest(new=new):
                path = self.article()
                path.write_text(path.read_text().replace(old, new))
                self.assertTrue(self.errors())

    def test_remote_local_and_reference_image_embeddings_are_rejected(self):
        for content in [
            "![Photo](https://example.com/photo.jpg)",
            "![Photo](assets/photo.png)",
            "![Photo][original]\n\n[original]: https://example.com/photo",
            '<picture><img src="https://example.com/photo"></picture>',
            '<svg><image href="https://example.com/photo"/></svg>',
            '<div style="background-image: url(https://example.com/opaque)"></div>',
        ]:
            with self.subTest(content=content):
                self.article(content=content)
                self.assertTrue(any("embedding" in error for error in self.errors()))

    def test_direct_image_links_are_rejected_but_code_examples_are_not(self):
        for content in [
            "[查看](https://example.com/photo.jpg?width=800)",
            "[查看](assets/photo.webp)",
            '<a href="https://images.aeonmedia.co/images/opaque-id?format=auto">查看</a>',
        ]:
            with self.subTest(content=content):
                self.article(content=content)
                self.assertTrue(any("image-resource" in error for error in self.errors()))
        self.article(content='```markdown\n![Example](https://example.com/photo.jpg)\n```\n\n~~~html\n<img src="photo.png">\n~~~\n\n`![Example](photo.jpg)`')
        self.assertEqual(self.errors(), [])

    def test_hidden_legacy_translation_cannot_keep_unreferenced_image_files(self):
        path = self.article(note_type="traslation", status="hidden")
        assets = path.parent / "assets"
        assets.mkdir()
        (assets / "photo.jpg").write_bytes(b"not downloaded in this test")
        (assets / "disguised.dat").write_bytes(b"\x89PNG\r\n\x1a\n")
        result = checks.check_repository(self.root)
        self.assertEqual(result["translations"], 1)
        self.assertEqual(sum("retains an image file" in error for error in result["errors"]), 2)

    def test_other_article_types_are_outside_this_check(self):
        self.article(note_type="note", content="![An original image](assets/own-photo.jpg)")
        self.assertEqual(checks.check_repository(self.root), {"translations": 0, "errors": []})


if __name__ == "__main__":
    unittest.main()
