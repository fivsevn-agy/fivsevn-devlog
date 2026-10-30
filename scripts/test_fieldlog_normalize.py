"""Verify saved-image conversion, safe replacement, and publication-state protection."""
import hashlib
from io import BytesIO
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image

from normalize_fieldlog_images import normalize
from site_post_metadata import dump_frontmatter, normalize_metadata, read_frontmatter


def image_bytes(fmt='PNG', color='red'):
    stream=BytesIO()
    Image.new('RGBA' if fmt=='PNG' else 'RGB',(32,24),color).save(stream,format=fmt)
    return stream.getvalue()


def sha(data):
    return hashlib.sha256(data).hexdigest()


class FieldlogNormalizeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)

    def post(self,number=0,suffix='png',status='published',visibility='public',data=None):
        ident=f'2026-10-30-1200{number:02d}-test{number}'
        package=self.root/'natsci/fieldlog/2026/10'/ident
        photo=package/f'assets/photo.{suffix}';photo.parent.mkdir(parents=True)
        photo.write_bytes(data if data is not None else image_bytes('JPEG' if suffix.lower() in {'jpg','jpeg'} else 'PNG'))
        meta=normalize_metadata(dict(id=ident,date=f'2026-10-30T12:00:{number:02d}+08:00',title='山间发现',
             status=status,visibility=visibility,image='assets/'+photo.name,alt='自己填写的说明'),site='fieldlog')
        body='\n测试 **正文**。\n\n[资料](https://example.com/)\n'
        source=package/'index.md';source.write_text(dump_frontmatter(meta)+body)
        return source,photo

    def snapshot(self):
        return {p.relative_to(self.root).as_posix():p.read_bytes() for p in self.root.rglob('*') if p.is_file() and not p.is_symlink()}

    def test_replaces_original_and_only_changes_image_reference(self):
        source,photo=self.post(suffix='JPEG')
        before,body=read_frontmatter(source)
        self.assertEqual(normalize(self.root)['count'],1)
        self.assertFalse(photo.exists());self.assertTrue(photo.with_suffix('.webp').exists())
        after,new_body=read_frontmatter(source)
        expected=dict(before);expected['extra']=dict(before['extra'],image='assets/photo.webp')
        expected['metadata_updated']=after['metadata_updated']
        self.assertEqual(after,expected);self.assertEqual(new_body,body)
        self.assertEqual(list(source.parent.rglob('*.JPEG')),[])

    def test_existing_webp_and_repeat_runs_keep_all_bytes(self):
        payload=image_bytes('WEBP')
        _,photo=self.post(suffix='WEBP',data=payload)
        before=self.snapshot();result=normalize(self.root)
        self.assertEqual(result['count'],0);self.assertEqual(photo.read_bytes(),payload)
        self.assertEqual(self.snapshot(),before)
        self.post(number=1)
        normalize(self.root);before=self.snapshot()
        self.assertEqual(normalize(self.root)['count'],0);self.assertEqual(self.snapshot(),before)

    def test_hidden_draft_and_private_images_are_normalized(self):
        packages=[self.post(number=number,status=status,visibility=visibility)
                  for number,(status,visibility) in enumerate([('published','public'),('hidden','public'),('draft','public'),('published','private')])]
        self.assertEqual(normalize(self.root)['count'],4)
        for source,photo in packages:
            self.assertFalse(photo.exists());self.assertEqual(read_frontmatter(source)[0]['extra']['image'],'assets/photo.webp')

    def test_unreferenced_package_image_does_not_leave_a_raw_copy(self):
        source,_=self.post()
        spare=source.parent/'assets/spare.JPG';spare.write_bytes(image_bytes('JPEG','blue'))
        self.assertEqual(normalize(self.root)['count'],2)
        self.assertFalse(spare.exists());self.assertTrue(spare.with_suffix('.webp').is_file())

    def test_bad_sibling_keeps_entire_batch_untouched(self):
        self.post();self.post(number=1,data=b'damaged image')
        before=self.snapshot()
        with self.assertRaises(ValueError):normalize(self.root)
        self.assertEqual(self.snapshot(),before)
        self.assertFalse(list(self.root.glob('.fieldlog-normalize-*')))

    def test_existing_webp_destination_is_not_overwritten(self):
        _,photo=self.post();photo.with_suffix('.webp').write_bytes(image_bytes('WEBP','blue'))
        before=self.snapshot()
        with self.assertRaisesRegex(ValueError,'overwrite'):normalize(self.root)
        self.assertEqual(self.snapshot(),before)

    def test_metadata_failure_rolls_back_images_and_sources(self):
        source,_=self.post();before=self.snapshot();original=os.replace;failed=False
        def fail_once(src,dst):
            nonlocal failed
            if Path(dst).resolve()==source.resolve() and not failed:
                failed=True;raise OSError('simulated metadata failure')
            return original(src,dst)
        with patch('normalize_fieldlog_images.os.replace',side_effect=fail_once):
            with self.assertRaisesRegex(OSError,'metadata failure'):normalize(self.root)
        self.assertTrue(failed);self.assertEqual(self.snapshot(),before)

    def test_symlink_is_rejected(self):
        _,photo=self.post();target=self.root/'outside.png';target.write_bytes(photo.read_bytes())
        photo.unlink();photo.symlink_to(target)
        with self.assertRaisesRegex(ValueError,'symlink'):normalize(self.root)
        self.assertTrue(photo.is_symlink())

    def state(self,photo,saved_hash):
        path=self.root/'natsci/fieldlog/.publishing/state.json';path.parent.mkdir(parents=True)
        state={'version':1,'cursor':'keep-cursor','events':{'event':{'image_path':photo.relative_to(self.root).as_posix(),
               'sha256':saved_hash,'file_sha256':saved_hash,'route':'keep-route','id':'keep-id'}}}
        path.write_text(json.dumps(state));return path,state

    def test_state_preserves_source_hash_route_and_updates_saved_digest(self):
        _,photo=self.post();before=photo.read_bytes();path,state=self.state(photo,sha(before))
        normalize(self.root);updated=json.loads(path.read_text());event=updated['events']['event']
        self.assertEqual(updated['cursor'],state['cursor'])
        self.assertEqual(event['sha256'],sha(before));self.assertEqual(event['route'],'keep-route');self.assertEqual(event['id'],'keep-id')
        self.assertEqual(event['file_sha256'],sha(photo.with_suffix('.webp').read_bytes()))
        self.assertEqual(event['image_path'],photo.with_suffix('.webp').relative_to(self.root).as_posix())

    def test_manual_image_change_keeps_cleanup_guard(self):
        _,photo=self.post(suffix='webp',data=image_bytes('WEBP'))
        path,state=self.state(photo,sha(photo.read_bytes()))
        photo.write_bytes(image_bytes('JPEG','blue'))
        normalize(self.root)
        self.assertEqual(json.loads(path.read_text()),state)
        with Image.open(photo) as im:self.assertEqual(im.format,'WEBP')


if __name__=='__main__':unittest.main()
