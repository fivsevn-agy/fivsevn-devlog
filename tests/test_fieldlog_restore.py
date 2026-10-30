"""Exercise one-time migration restoration without accessing the network."""
import hashlib
from io import BytesIO
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import restore_fieldlog_media as media


class Response(BytesIO):
    def __init__(self, data, url):
        super().__init__(data)
        self.url = url


class MediaRestoreTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.folder = self.root / "natsci/fieldlog"
        self.migration = self.folder / "migration"
        self.migration.mkdir(parents=True)
        self.data = [b"first original image", b"second original image"]
        self.entries = [{
            "image_path": f"2026/07/entry-{i}/assets/photo.jpg",
            "download_url": f"https://raw.githubusercontent.com/fivsevn/fivsevn-assets/main/natsci/fieldlog/photo-{i}.jpg",
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
        } for i, data in enumerate(self.data)]
        self.save_manifest()
        (self.migration / "ui-resources.json").write_text("[]")
        self.flag = self.folder / ".publishing/media-restored.json"

    def save_manifest(self):
        (self.migration / "manifest.json").write_text(json.dumps({"entries": self.entries}))

    def download(self, request, **kwargs):
        i = next(i for i, e in enumerate(self.entries) if e["download_url"] == request.full_url)
        return Response(self.data[i], request.full_url)

    def test_completed_restore_never_redownloads_or_reverts_later_edits_and_deletions(self):
        with patch.object(media, "urlopen", side_effect=self.download) as download:
            self.assertEqual(media.restore(self.root), 2)
            self.assertEqual(download.call_count, 2)
        first, second = [self.folder / e["image_path"] for e in self.entries]
        first.write_bytes(b"intentionally replaced")
        second.unlink()
        with patch.object(media, "urlopen") as download:
            self.assertEqual(media.restore(self.root), 0)
            download.assert_not_called()
        self.assertEqual(first.read_bytes(), b"intentionally replaced")
        self.assertFalse(second.exists())

    def test_checksum_failure_installs_none_of_the_batch(self):
        self.data[1] = b"wrong original image"
        with patch.object(media, "urlopen", side_effect=self.download):
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                media.restore(self.root)
        self.assertFalse(self.flag.exists())
        self.assertTrue(all(not (self.folder / e["image_path"]).exists() for e in self.entries))

    def test_existing_different_image_is_preserved_and_rejected_before_completion(self):
        target = self.folder / self.entries[0]["image_path"]
        target.parent.mkdir(parents=True)
        target.write_bytes(b"existing replacement")
        with patch.object(media, "urlopen", side_effect=self.download):
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                media.restore(self.root)
        self.assertEqual(target.read_bytes(), b"existing replacement")
        self.assertFalse(self.flag.exists())

    def test_unsafe_paths_and_source_urls_are_rejected_without_downloads(self):
        original = dict(self.entries[0])
        for field, values in {
            "image_path": ["../outside.jpg", "/tmp/outside.jpg"],
            "download_url": ["http://raw.githubusercontent.com/file.jpg", "https://example.com/file.jpg",
                             "https://user@raw.githubusercontent.com/file.jpg",
                             "https://raw.githubusercontent.com:443/file.jpg",
                             "https://raw.githubusercontent.com/file.jpg#fragment"],
        }.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.entries[0] = {**original, field: value}
                    self.save_manifest()
                    with patch.object(media, "urlopen") as download:
                        with self.assertRaisesRegex(ValueError, "Unsafe"):
                            media.restore(self.root)
                        download.assert_not_called()
        self.entries[0] = original

    def test_redirect_cannot_downgrade_https(self):
        def redirect(request, **kwargs):
            return Response(self.data[0], "http://raw.githubusercontent.com/file.jpg")
        with patch.object(media, "urlopen", side_effect=redirect):
            with self.assertRaisesRegex(ValueError, "Unexpected media redirect"):
                media.restore(self.root)
        self.assertFalse(self.flag.exists())

    def test_completion_directory_cannot_follow_a_symlink(self):
        outside = self.root / "outside"
        outside.mkdir()
        self.flag.parent.symlink_to(outside)
        with patch.object(media, "urlopen") as download:
            with self.assertRaisesRegex(ValueError, "completion path"):
                media.restore(self.root)
            download.assert_not_called()
        self.assertEqual(list(outside.iterdir()), [])

    def test_marker_install_failure_rolls_back_new_images_and_removes_temporary_files(self):
        replace = os.replace
        def fail_marker(source, destination):
            if destination == self.flag:
                raise OSError("simulated full disk")
            return replace(source, destination)
        with patch.object(media, "urlopen", side_effect=self.download), patch.object(media.os, "replace", side_effect=fail_marker):
            with self.assertRaisesRegex(OSError, "simulated full disk"):
                media.restore(self.root)
        self.assertFalse(self.flag.exists())
        self.assertTrue(all(not (self.folder / e["image_path"]).exists() for e in self.entries))
        self.assertEqual(list(self.folder.rglob(".fieldlog-media-*")), [])


if __name__ == "__main__":
    unittest.main()
