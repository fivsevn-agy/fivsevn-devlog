"""Verify archive publication, withdrawal, and preserved observation metadata."""
from datetime import datetime
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

from PIL import Image
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_fieldlog as fieldlog
from normalize_fieldlog_images import normalize
from site_post_metadata import dump_frontmatter, normalize_metadata, read_frontmatter


class FieldlogBuildTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.folder = self.root / "natsci/fieldlog"
        shutil.copytree(ROOT / "scripts/fieldlog_templates", self.root / "scripts/fieldlog_templates")
        (self.folder / "ui").mkdir(parents=True)
        (self.folder / "ui/fieldlog.css").write_text("body{background:#131415}\n")
        shutil.copyfile(ROOT / "natsci/fieldlog/ui/navigation.js", self.folder / "ui/navigation.js")
        (self.folder / "ui/homepage20251105bio.webp").write_bytes(b"hero")
        self.output=self.root / "_site/natsci/fieldlog"

    def post(self, ident, *, date="2026-07-15T09:08:24+08:00", body="", status="published", **values):
        timestamp = datetime.fromisoformat(date)
        directory = self.folder / timestamp.strftime("%Y/%m") / ident
        (directory / "assets").mkdir(parents=True)
        image = directory / "assets/山间 image.webp"
        Image.new("RGB", (24, 18), "green").save(image,"WEBP")
        metadata = {
            "id": ident, "observation_id": timestamp.strftime("%y%m%d%H%M%S"),
            "date": date, "annotation_date": "15 Jul, 2026 10:07", "title": "Observation",
            "status": status, "image": "assets/山间 image.webp",
            "alt": 'A specimen <in the field> "close up"', "archive_status": "Archived",
        }
        metadata.update(values)
        source = directory / "index.md"
        self.write(source, metadata, body)
        return source

    @staticmethod
    def write(path, metadata, body=""):
        canonical=normalize_metadata(metadata,site="fieldlog")
        path.write_text(dump_frontmatter(canonical)+"\n"+body+"\n",encoding="utf-8")

    def test_attached_markdown_only_appears_in_detail_and_images_use_local_encoded_urls(self):
        source = self.post("captioned", body="**发现马陆**\n\n[资料](https://example.com/note)")
        fieldlog.build(self.root)
        archive = (self.output / "index.html").read_text()
        detail = (self.output/source.parent.relative_to(self.folder)/"index.html").read_text()
        self.assertNotIn("发现马陆", archive)
        self.assertIn("<strong>发现马陆</strong>", detail)
        self.assertIn('href="https://example.com/note"', detail)
        self.assertIn('/natsci/fieldlog/2026/07/captioned/assets/%E5%B1%B1%E9%97%B4%20image.webp', detail)
        self.assertIn('alt="A specimen &lt;in the field&gt; &quot;close up&quot;"', detail)
        self.assertIn('href="/natsci/fieldlog/2026/07/captioned/"', archive)
        self.assertNotIn("No comments", archive + detail)

    def test_withdrawal_removes_artifacts_without_writing_into_content_sources(self):
        posts = [self.post(f"post-{number:02d}") for number in range(12)]
        first = fieldlog.build(self.root)
        self.assertEqual((first["posts"], first["archive_pages"]), (12, 2))
        page_two = self.output / "page/2/index.html"
        self.assertTrue(page_two.is_file())
        manual = self.folder / "manual.html"
        manual.write_text("A hand-maintained page")
        source = posts[0]
        source.write_text(source.read_text().replace("status: published", "status: hidden"))
        fieldlog.build(self.root)
        self.assertFalse((self.output/source.parent.relative_to(self.folder)/"index.html").exists())
        self.assertFalse(page_two.exists())
        self.assertEqual(manual.read_text(), "A hand-maintained page")
        self.assertEqual(fieldlog.build(self.root, check=True)["posts"], 11)

    def test_private_draft_and_hidden_posts_are_excluded(self):
        live=self.post("live",status="active")
        draft=self.post("unfinished",status="draft",image="assets/not-uploaded-yet.jpg")
        self.post("private",visibility="private")
        self.post("hidden",status="hidden")
        result=fieldlog.build(self.root)
        self.assertEqual(result["posts"],1)
        self.assertTrue((self.output/live.parent.relative_to(self.folder)/"index.html").is_file())
        self.assertFalse((self.output/draft.parent.relative_to(self.folder)/"index.html").exists())
        self.assertEqual(list(self.folder.rglob("*.html")),[])

    def test_exact_eleven_post_pagination_and_old_anchor_routes(self):
        for number in range(43):self.post(f"post-{number:02d}")
        result=fieldlog.build(self.root)
        self.assertEqual((result['posts'],result['pages']),(43,4))
        for number,count in [(1,11),(2,11),(3,11),(4,10)]:
            source=self.output/('index.html' if number==1 else f'page/{number}/index.html')
            soup=BeautifulSoup(source.read_text(),'html.parser')
            self.assertEqual(len(soup.select('article.specimen')),count)
            self.assertEqual(len(soup.select('header.archive-intro')),1)
            routes=json.loads(soup.select_one('#fieldlog-archive-map').string)
            self.assertEqual(len(routes),43)
            self.assertEqual(len({value.split('#')[0] for value in routes.values()}),4)
            for anchor,target in routes.items():
                self.assertIsNotNone(soup.find(id=anchor))
                if target.split('#')[0] != (fieldlog.BASE if number==1 else f'{fieldlog.BASE}page/{number}/'):
                    self.assertEqual(soup.find(id=anchor)['href'],target)
        source=self.folder/'2026/07/post-00/index.md'
        detail=BeautifulSoup((self.output/source.parent.relative_to(self.folder)/'index.html').read_text(),'html.parser')
        self.assertEqual(detail.select_one('[data-fieldlog-return]')['href'],routes['obs-post-00'])

    def test_schema_rejects_noncanonical_metadata(self):
        source=self.post('invalid')
        source.write_text(source.read_text().replace('id: invalid\n',"id: invalid\ndate: '2026-07-15T09:08:24+08:00'\n"))
        with self.assertRaises(ValueError):fieldlog.build(self.root)

    def test_equal_timestamps_keep_original_order_and_sort_by_actual_instant(self):
        self.post("same-b", date="2026-06-06T07:06:58+08:00")
        self.post("same-a", date="2026-06-06T07:06:58+08:00")
        self.post("newest", date="2026-06-05T23:07:00+00:00")
        history=self.folder/"site-data";history.mkdir()
        (history/"history.json").write_text(json.dumps({"order":["same-b","same-a"]}))
        self.assertEqual([entry.meta["id"] for entry in fieldlog.read_entries(self.folder)],
                         ["newest", "same-b", "same-a"])

    def test_exif_rotation_preserves_displayed_aspect_ratio(self):
        source = self.post("rotated")
        image = source.parent / "assets/山间 image.webp"
        exif = Image.Exif()
        exif[274] = 6
        Image.new("RGB", (24, 18), "blue").save(image, format="JPEG", exif=exif)
        normalize(self.root)
        entry = fieldlog.read_entries(self.folder)[0]
        self.assertEqual((entry.width, entry.height), (18, 24))

    def test_build_rejects_unconverted_saved_images(self):
        source=self.post("unconverted")
        image=source.parent/"assets/山间 image.webp"
        Image.new("RGB",(24,18),"red").save(image,format="JPEG")
        with self.assertRaisesRegex(ValueError,"saved photos must be WebP"):
            fieldlog.build(self.root)

    def test_image_cannot_escape_its_post_package(self):
        self.post("outside", image="../../../../outside.jpg")
        Image.new("RGB", (24, 18), "red").save(self.folder / "outside.jpg")
        with self.assertRaisesRegex(ValueError, "inside this post's folder"):
            fieldlog.build(self.root)

    def test_check_reports_stale_output_without_modifying_it(self):
        source = self.post("edited", body="First caption")
        fieldlog.build(self.root)
        output = (self.output/source.parent.relative_to(self.folder)/"index.html")
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
