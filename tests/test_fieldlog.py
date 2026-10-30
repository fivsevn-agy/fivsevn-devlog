"""Verify archive publication, withdrawal, and preserved observation metadata."""
from datetime import datetime
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_fieldlog as fieldlog


class FieldlogBuildTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.folder = self.root / "natsci/fieldlog"
        shutil.copytree(ROOT / "scripts/fieldlog_templates", self.root / "scripts/fieldlog_templates")
        (self.folder / "ui").mkdir(parents=True)
        (self.folder / "ui/fieldlog.css").write_text("body{background:#131415}\n")

    def post(self, ident, *, date="2026-07-15T09:08:24+08:00", body="", status="published", **values):
        timestamp = datetime.fromisoformat(date)
        directory = self.folder / timestamp.strftime("%Y/%m") / ident
        (directory / "assets").mkdir(parents=True)
        image = directory / "assets/山间 image.jpg"
        Image.new("RGB", (24, 18), "green").save(image)
        metadata = {
            "id": ident, "observation_id": timestamp.strftime("%y%m%d%H%M%S"),
            "date": date, "annotation_date": "15 Jul, 2026 10:07", "title": "Observation",
            "status": status, "published": False, "image": "assets/山间 image.jpg",
            "alt": 'A specimen <in the field> "close up"', "archive_status": "Archived",
        }
        metadata.update(values)
        source = directory / "index.md"
        self.write(source, metadata, body)
        return source

    @staticmethod
    def write(path, metadata, body=""):
        path.write_text("---\n" + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False)
                        + "---\n\n" + body + "\n", encoding="utf-8")

    def test_attached_markdown_only_appears_in_detail_and_images_use_local_encoded_urls(self):
        source = self.post("captioned", body="**发现马陆**\n\n[资料](https://example.com/note)")
        fieldlog.build(self.root)
        archive = (self.folder / "index.html").read_text()
        detail = source.with_suffix(".html").read_text()
        self.assertNotIn("发现马陆", archive)
        self.assertIn("<strong>发现马陆</strong>", detail)
        self.assertIn('href="https://example.com/note"', detail)
        self.assertIn('/natsci/fieldlog/2026/07/captioned/assets/%E5%B1%B1%E9%97%B4%20image.jpg', detail)
        self.assertIn('alt="A specimen &lt;in the field&gt; &quot;close up&quot;"', detail)
        self.assertIn('href="/natsci/fieldlog/2026/07/captioned/"', archive)
        self.assertNotIn("No comments", archive + detail)

    def test_withdrawal_removes_detail_and_obsolete_pagination_but_preserves_manual_html(self):
        posts = [self.post(f"post-{number:02d}") for number in range(18)]
        first = fieldlog.build(self.root)
        self.assertEqual((first["posts"], first["archive_pages"]), (18, 2))
        page_two = self.folder / "page/2/index.html"
        self.assertTrue(page_two.is_file())
        manual = self.folder / "manual.html"
        manual.write_text("A hand-maintained page")
        source = posts[0]
        source.write_text(source.read_text().replace("status: published", "status: hidden"))
        fieldlog.build(self.root)
        self.assertFalse(source.with_suffix(".html").exists())
        self.assertFalse(page_two.exists())
        self.assertEqual(manual.read_text(), "A hand-maintained page")
        self.assertEqual(fieldlog.build(self.root, check=True)["posts"], 17)

    def test_jekyll_suppression_flag_is_independent_of_publication_status(self):
        live = self.post("live")
        draft = self.post("unfinished", status="draft", image="assets/not-uploaded-yet.jpg")
        result = fieldlog.build(self.root)
        self.assertEqual(result["posts"], 1)
        self.assertTrue(live.with_suffix(".html").is_file())
        self.assertFalse(draft.with_suffix(".html").exists())
        live.write_text(live.read_text().replace("published: false", "published: true"))
        with self.assertRaisesRegex(ValueError, "published: false"):
            fieldlog.build(self.root)

    def test_equal_timestamps_keep_original_order_and_sort_by_actual_instant(self):
        self.post("same-b", date="2026-06-06T07:06:58+08:00")
        self.post("same-a", date="2026-06-06T07:06:58+08:00")
        self.post("newest", date="2026-06-05T23:07:00+00:00")
        migration = self.folder / "migration"
        migration.mkdir()
        (migration / "manifest.json").write_text(json.dumps({"entries": [{"id": "same-b"}, {"id": "same-a"}]}))
        self.assertEqual([entry.meta["id"] for entry in fieldlog.read_entries(self.folder)],
                         ["newest", "same-b", "same-a"])

    def test_exif_rotation_preserves_displayed_aspect_ratio(self):
        source = self.post("rotated")
        image = source.parent / "assets/山间 image.jpg"
        exif = Image.Exif()
        exif[274] = 6
        Image.new("RGB", (24, 18), "blue").save(image, exif=exif)
        entry = fieldlog.read_entries(self.folder)[0]
        self.assertEqual((entry.width, entry.height), (18, 24))

    def test_image_cannot_escape_its_post_package(self):
        self.post("outside", image="../../../../outside.jpg")
        Image.new("RGB", (24, 18), "red").save(self.folder / "outside.jpg")
        with self.assertRaisesRegex(ValueError, "inside this post's folder"):
            fieldlog.build(self.root)

    def test_check_reports_stale_output_without_modifying_it(self):
        source = self.post("edited", body="First caption")
        fieldlog.build(self.root)
        output = source.with_suffix(".html")
        before = output.read_bytes()
        source.write_text(source.read_text().replace("First caption", "Revised caption"))
        with self.assertRaisesRegex(ValueError, "Generated pages are stale"):
            fieldlog.build(self.root, check=True)
        self.assertEqual(output.read_bytes(), before)
        fieldlog.build(self.root)
        self.assertIn("Revised caption", output.read_text())
        self.assertEqual(fieldlog.build(self.root, check=True)["changed"], 0)


if __name__ == "__main__":
    unittest.main()
