import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from urllib.parse import urlparse
from fieldlog_image_inbox import clear_verified
from verify_fieldlog_live import verify
from site_post_metadata import dump_frontmatter, normalize_metadata, read_frontmatter


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.media = b'original photo bytes'
        self.source = self.root / 'natsci/fieldlog/trigger_imgs/photo.jpg'
        self.saved = self.root / 'natsci/fieldlog/2026/10/2026-10-29-120000-test/assets/photo.jpg'
        self.route = '2026/10/2026-10-29-120000-test/'
        for p in [self.source, self.saved]:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(self.media)
        self.meta=normalize_metadata(dict(id=self.saved.parent.parent.name,date='2026-10-29T12:00:00+08:00',
                                        title='Lunch',status='published',image='assets/photo.jpg'),site='fieldlog')
        self.saved.parent.parent.joinpath('index.md').write_text(dump_frontmatter(self.meta))
        state = {'version': 1, 'events': {'event': {
            'upload_path': self.source.relative_to(self.root).as_posix(),
            'image_path': self.saved.relative_to(self.root).as_posix(),
            'sha256': hashlib.sha256(self.media).hexdigest(), 'route': 'natsci/fieldlog/' + self.route}}}
        self.state = state
        (self.root / 'natsci/fieldlog/.publishing').mkdir()
        (self.root / 'natsci/fieldlog/.publishing/state.json').write_text(json.dumps(state))
        self.public = {'index.html': b'home', self.route + 'index.html': b'post',
                       self.route + 'assets/photo.jpg': self.media}
        files = {}
        for path, data in self.public.items():
            p = self.root / '_site/natsci/fieldlog' / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
            files[path] = hashlib.sha256(data).hexdigest()
        receipt = {'posts': 1, 'pages': 1, 'base_path': '', 'files': files}
        data = json.dumps(receipt).encode()
        (self.root / '_site/natsci/fieldlog/build-receipt.json').write_bytes(data)
        self.public['build-receipt.json'] = data

    def fetch(self, url):
        return self.public[urlparse(url).path.lstrip('/')]

    def mark(self):
        return verify(self.root, 'https://example.test', self.fetch, attempts=1)

    def test_clear_only_after_actual_public_byte_verification(self):
        self.mark()
        self.assertEqual(clear_verified(self.root), (1, len(self.media)))
        self.assertFalse(self.source.exists())
        self.assertEqual(self.saved.read_bytes(), self.media)

    def test_unchanged_archive_does_not_download_every_photo_again(self):
        self.mark()
        clear_verified(self.root)
        requested=[]
        def read(url):
            requested.append(urlparse(url).path.lstrip('/'))
            return self.fetch(url)
        verify(self.root,'https://example.test',read,attempts=1)
        self.assertEqual(set(requested),{'build-receipt.json','index.html'})

    def test_uploaded_original_and_saved_webp_can_have_different_bytes(self):
        converted = b'converted WebP bytes'
        self.saved.write_bytes(converted)
        state = copy.deepcopy(self.state)
        state['events']['event']['file_sha256'] = hashlib.sha256(converted).hexdigest()
        (self.root / 'natsci/fieldlog/.publishing/state.json').write_text(json.dumps(state))
        media_path = self.route + 'assets/photo.jpg'
        (self.root / '_site/natsci/fieldlog' / media_path).write_bytes(converted)
        self.public[media_path] = converted
        receipt_path = self.root / '_site/natsci/fieldlog/build-receipt.json'
        receipt = json.loads(receipt_path.read_text())
        receipt['files'][media_path] = hashlib.sha256(converted).hexdigest()
        receipt_path.write_text(json.dumps(receipt))
        self.public['build-receipt.json'] = receipt_path.read_bytes()
        self.mark()
        self.assertEqual(clear_verified(self.root), (1, len(self.media)))
        self.assertFalse(self.source.exists())
        self.assertEqual(self.saved.read_bytes(), converted)

    def test_failed_public_verification_invalidates_old_marker(self):
        self.mark()
        self.public[self.route + 'index.html'] = b'wrong public page'
        with self.assertRaises(ValueError):
            self.mark()
        self.assertFalse((self.root / '_site/natsci/fieldlog/.verified.json').exists())
        with self.assertRaises(FileNotFoundError):
            clear_verified(self.root)
        self.assertTrue(self.source.exists())

    def test_newer_inbox_upload_is_retained(self):
        self.mark()
        self.source.write_bytes(b'new upload')
        self.assertEqual(clear_verified(self.root)[0], 0)
        self.assertEqual(self.source.read_bytes(), b'new upload')

    def test_private_active_post_is_not_cleared(self):
        self.mark()
        self.meta['visibility']='private'
        self.saved.parent.parent.joinpath('index.md').write_text(dump_frontmatter(self.meta))
        self.assertEqual(clear_verified(self.root)[0],0)
        self.assertTrue(self.source.exists())

    def test_public_active_status_is_cleared_after_verification(self):
        self.meta['status']='active'
        self.saved.parent.parent.joinpath('index.md').write_text(dump_frontmatter(self.meta))
        self.mark()
        self.assertEqual(clear_verified(self.root)[0],1)
        self.assertFalse(self.source.exists())

    def test_identical_reupload_is_not_cleared_by_an_older_published_post(self):
        self.mark()
        newer = self.root / 'natsci/fieldlog/2026/10/2026-10-29-120001-new/assets/photo.jpg'
        newer.parent.mkdir(parents=True)
        newer.write_bytes(self.media)
        meta=normalize_metadata(dict(id=newer.parent.parent.name,date='2026-10-29T12:00:01+08:00',
                                    title='Hidden photo',status='hidden',image='assets/photo.jpg'),site='fieldlog')
        newer.parent.parent.joinpath('index.md').write_text(dump_frontmatter(meta))
        state = copy.deepcopy(self.state)
        event = copy.deepcopy(state['events']['event'])
        event['image_path'] = newer.relative_to(self.root).as_posix()
        event['route'] = 'natsci/fieldlog/2026/10/2026-10-29-120001-new/'
        state['events']['newer-event'] = event
        (self.root / 'natsci/fieldlog/.publishing/state.json').write_text(json.dumps(state))
        self.assertEqual(clear_verified(self.root)[0], 0)
        self.assertTrue(self.source.exists())

    def test_changed_saved_photo_is_retained(self):
        self.mark()
        self.saved.write_bytes(b'edited saved photo')
        self.assertEqual(clear_verified(self.root)[0], 0)
        self.assertTrue(self.source.exists())

    def test_mismatched_receipt_prevents_cleanup(self):
        self.mark()
        marker = self.root / 'natsci/fieldlog/.publishing/deployed.json'
        marker.write_text('{}')
        with self.assertRaises(ValueError):
            clear_verified(self.root)
        self.assertTrue(self.source.exists())

    def test_validate_every_path_before_deleting_anything(self):
        self.mark()
        state = copy.deepcopy(self.state)
        bad = copy.deepcopy(state['events']['event'])
        bad['upload_path'] = '../outside.jpg'
        state['events']['unsafe'] = bad
        (self.root / 'natsci/fieldlog/.publishing/state.json').write_text(json.dumps(state))
        with self.assertRaises(ValueError):
            clear_verified(self.root)
        self.assertTrue(self.source.exists())


if __name__ == '__main__':
    unittest.main()
