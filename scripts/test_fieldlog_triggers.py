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
from site_post_metadata import validate_metadata

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

    def test_merge_preserves_second_parent_cursor_and_imports_new_upload_once(self):
        self.git('branch', 'phone')
        self.upload('main.jpg')
        main_upload = self.commit('Main observation')
        self.assertEqual(ingest(self.root), 1)
        self.commit('Save published package and cursor')
        self.git('checkout', 'phone')
        self.upload('phone.jpg', 'blue')
        phone_upload = self.commit('Phone observation', '2026-10-29T01:02:03+00:00')
        self.git('merge', '--no-ff', 'main', '-m', 'Merge published main')
        self.assertEqual(read_state(self.root)['cursor'], main_upload)
        self.assertEqual(ingest(self.root), 1)
        self.assertEqual({event['commit'] for event in read_state(self.root)['events'].values()}, {main_upload, phone_upload})
        self.assertEqual(len(self.posts()), 2)
        self.assertEqual(ingest(self.root), 0)

    def test_caption_timezone_retry_and_saved_hidden_edit(self):
        original = self.upload('山间/IMG_0001.JPG')
        self.commit('Upload photo\n\n**山间发现**\n\n[记录](https://example.com/)')
        self.assertEqual(ingest(self.root), 1)
        post = self.posts()[0]
        metadata, body = self.metadata(post)
        self.assertEqual(metadata['extra']['published_at'], '2026-10-30T17:00:00+08:00')
        self.assertEqual(metadata['extra']['observation_id'], '261030170000')
        self.assertEqual(metadata['title'], '30 Oct, 2026 17:00')
        validate_metadata(metadata,site='fieldlog')
        self.assertNotIn('published',metadata)
        self.assertEqual(metadata['visibility'],'public')
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
        good = self.upload('good.jpg')
        bad = self.root / INBOX / 'invalid.jpg'
        bad.write_bytes(b'not an image')
        self.commit('Upload valid and damaged images together')
        state = (self.root / STATE_PATH).read_bytes()
        originals = {path: path.read_bytes() for path in [good, bad]}
        with self.assertRaises(ValueError):
            ingest(self.root)
        self.assertEqual(self.posts(), [])
        self.assertEqual((self.root / STATE_PATH).read_bytes(), state)
        self.assertEqual({path: path.read_bytes() for path in originals}, originals)

    def test_mixed_uploads_archive_webp_without_losing_image_properties_or_originals(self):
        def encoded(image, fmt, **options):
            stream = BytesIO()
            image.save(stream, fmt, **options)
            return stream.getvalue()

        transparent = Image.new('RGBA', (3, 1))
        transparent.putdata([(255, 0, 0, 255), (11, 22, 33, 127), (90, 80, 70, 0)])
        photo = Image.new('RGB', (24, 18), 'red')
        exif = photo.getexif()
        exif[274] = 6
        exif[315] = 'Fieldlog'
        uploads = {
            '透明.PNG': encoded(transparent, 'PNG'),
            'animation.gif': encoded(Image.new('RGB', (4, 3), 'red'), 'GIF', save_all=True,
                                     append_images=[Image.new('RGB', (4, 3), 'blue')],
                                     duration=[100, 240], loop=2),
            'phone.JPG': encoded(photo, 'JPEG', exif=exif, icc_profile=b'Fieldlog ICC profile'),
            'existing.webp': encoded(Image.new('RGB', (17, 11), 'green'), 'WEBP', quality=91),
        }
        inbox = self.root / INBOX
        inbox.mkdir(parents=True)
        for name, data in uploads.items():
            (inbox / name).write_bytes(data)
        self.commit('Upload mixed formats together')
        self.assertEqual(ingest(self.root), len(uploads))
        events = {Path(event['upload_path']).name: event for event in read_state(self.root)['events'].values()}
        self.assertEqual(set(events), set(uploads))
        for name, event in events.items():
            saved = self.root / event['image_path']
            self.assertEqual(saved.suffix, '.webp')
            self.assertEqual((inbox / name).read_bytes(), uploads[name])
            with Image.open(saved) as image:
                self.assertEqual(image.format, 'WEBP')
                if name == '透明.PNG':
                    self.assertEqual(image.size, (3, 1))
                    self.assertEqual(image.convert('RGBA').tobytes(), transparent.tobytes())
                elif name == 'animation.gif':
                    self.assertEqual(image.size, (4, 3))
                    self.assertEqual(image.n_frames, 2)
                    self.assertEqual(image.info['loop'], 3)
                    for frame, duration in enumerate([100, 240]):
                        image.seek(frame)
                        image.load()
                        self.assertEqual(image.info['duration'], duration)
                elif name == 'phone.JPG':
                    self.assertEqual(image.size, (18, 24))
                    self.assertIsNone(image.getexif().get(274))
                    self.assertEqual(image.getexif().get(315), 'Fieldlog')
                    self.assertEqual(image.info['icc_profile'], b'Fieldlog ICC profile')
                else:
                    self.assertEqual(image.size, (17, 11))
                    self.assertEqual(saved.read_bytes(), uploads[name])
        self.assertEqual(ingest(self.root), 0)
        self.assertEqual(len(self.posts()), len(uploads))

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
        self.assertNotIn('published',self.metadata(self.posts()[0])[0])
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
