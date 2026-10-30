"""Exercise real upload commits, saved edits, and failed batches without network."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from io import BytesIO

from PIL import Image
import yaml

from import_fieldlog_triggers import CONTENT, INBOX, STATE_PATH, ingest, initialize, read_state


class FieldlogUploadTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Fieldlog test')
        self.git('config', 'user.email', 'fieldlog-test@example.invalid')
        (self.root / 'seed.txt').write_text('seed\n')
        self.commit('Initialize repository')
        initialize(self.root)
        self.commit('Initialize upload state')

    def git(self, *arguments, **kwargs):
        return subprocess.check_output(['git', '-C', str(self.root), *arguments], stderr=subprocess.PIPE, **kwargs)

    def commit(self, message, date='2026-10-30T09:00:00+00:00'):
        self.git('add', '.')
        env = dict(os.environ, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
        self.git('commit', '-m', message, env=env)
        return self.git('rev-parse', 'HEAD').decode().strip()

    def upload(self, name='photo.jpg', color='red'):
        path = self.root / INBOX / name
        path.parent.mkdir(parents=True, exist_ok=True)
        image = BytesIO()
        Image.new('RGB', (24, 18), color).save(image, 'JPEG')
        path.write_bytes(image.getvalue())
        return path

    def posts(self):
        return sorted((self.root / CONTENT).glob('*/*/*/index.md'))

    def metadata(self, path):
        _, head, body = path.read_text().split('---', 2)
        return yaml.safe_load(head), body.strip()

    def test_caption_timezone_retry_and_saved_hidden_edit(self):
        original = self.upload('山间/IMG_0001.JPG')
        self.commit('Upload photo\n\n**山间发现**\n\n[记录](https://example.com/)')
        self.assertEqual(ingest(self.root), 1)
        post = self.posts()[0]
        metadata, body = self.metadata(post)
        self.assertEqual(metadata['date'], '2026-10-30T17:00:00+08:00')
        self.assertEqual(metadata['observation_id'], '261030170000')
        self.assertEqual(metadata['annotation_date'], '30 Oct, 2026 17:00')
        self.assertFalse(metadata['published'])
        self.assertEqual(body, '**山间发现**\n\n[记录](https://example.com/)')
        self.assertTrue(original.exists())
        self.assertEqual(ingest(self.root), 0)
        post.write_text(post.read_text().replace('status: published', 'status: hidden').replace('山间发现', '已修订'))
        self.commit('Edit saved caption and hide post')
        self.assertEqual(ingest(self.root), 0)
        self.assertIn('已修订', post.read_text())
        self.assertEqual(self.metadata(post)[0]['status'], 'hidden')
        self.assertEqual(len(self.posts()), 1)

    def test_reusing_phone_filename_creates_new_entry(self):
        self.upload()
        self.commit('First upload')
        self.assertEqual(ingest(self.root), 1)
        self.commit('Save first post and cursor')
        self.upload(color='blue')
        self.commit('Second upload', '2026-10-30T09:02:00+00:00')
        self.assertEqual(ingest(self.root), 1)
        posts = self.posts()
        self.assertEqual(len(posts), 2)
        self.assertNotEqual(posts[0].parent.name, posts[1].parent.name)
        self.assertEqual(len(read_state(self.root)['events']), 2)

    def test_invalid_batch_does_not_install_valid_sibling_or_advance_cursor(self):
        self.upload('good.jpg')
        bad = self.root / INBOX / 'invalid.jpg'
        bad.write_bytes(b'not an image')
        self.commit('Upload valid and damaged images together')
        state = (self.root / STATE_PATH).read_bytes()
        with self.assertRaises(ValueError):
            ingest(self.root)
        self.assertEqual(self.posts(), [])
        self.assertEqual((self.root / STATE_PATH).read_bytes(), state)

    def test_superseded_invalid_upload_can_be_repaired(self):
        path = self.root / INBOX / 'fixed.jpg'
        path.parent.mkdir(parents=True)
        path.write_bytes(b'damaged upload')
        self.commit('Damaged upload')
        self.upload('fixed.jpg')
        self.commit('Repair uploaded photo', '2026-10-30T09:01:00+00:00')
        self.assertEqual(ingest(self.root), 1)
        self.assertEqual(len(self.posts()), 1)

    def test_draft_and_cursor_protection(self):
        self.upload()
        self.commit('Save a draft\n\nPrivate draft label')
        self.assertEqual(ingest(self.root, status='draft'), 1)
        self.assertEqual(self.metadata(self.posts()[0])[0]['status'], 'draft')
        self.assertFalse(self.metadata(self.posts()[0])[0]['published'])
        with self.assertRaisesRegex(ValueError, 'refusing to reset'):
            initialize(self.root)
        path = self.root / STATE_PATH
        state = json.loads(path.read_text())
        state['cursor'] = 'f' * 40
        path.write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError, 'missing from Git history'):
            ingest(self.root)

    def test_symlink_upload_is_rejected(self):
        target = self.root / 'outside.jpg'
        target.write_bytes(b'data')
        inbox = self.root / INBOX
        inbox.mkdir(parents=True)
        (inbox / 'photo.jpg').symlink_to(target)
        self.commit('Symlink upload')
        with self.assertRaisesRegex(ValueError, 'regular image file'):
            ingest(self.root)
        self.assertEqual(self.posts(), [])


if __name__ == '__main__':
    unittest.main()
