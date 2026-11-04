"""Language, head safety and public discovery behavior without network access."""
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_document_metadata import prepare
from site_post_metadata import dump_frontmatter
from web_document import Document, document_metadata, primary_language, visible_text


def html(body='真实正文描述。', head='', lang='en-US'):
    return ('<!doctype html>\n<html lang="' + lang + '"><head>\n<title>中文 &amp; Notes</title>\n'
            + head + '\n<style>.x:before { content: " unchanged "; }</style>\n</head>'
            + '<body>\n' + body + '\n<script>const untouched = "<raw> & text";</script>\n</body></html>')


class WebDocumentTests(unittest.TestCase):
    def test_language_uses_explicit_and_single_language_metadata(self):
        for metadata, prose, expected in (
            ({'lang': 'ja'}, 'English and 中文', 'ja'),
            ({'languages': ['zh']}, 'English annotation label', 'zh-CN'),
            ({'languages': ['en']}, 'A name 五月七日', 'en'),
            ({'languages': ['fr']}, 'Une note française', 'fr'),
            ({'languages': ['zh', 'en']}, '中文内容是这个页面的主要正文。 HTTP API', 'zh-CN'),
            ({'languages': ['zh', 'en']}, 'This is an English page with a short 中文 name.', 'en'),
            ({'languages': ['ja', 'en']}, 'これは日本語の文章です。', 'ja'),
        ):
            with self.subTest(metadata=metadata):
                self.assertEqual(expected, primary_language(metadata, prose))

    def test_scripts_styles_code_and_hidden_text_do_not_drive_language_or_description(self):
        body = ('<script>' + 'English ' * 100 + '</script><style>' + 'English ' * 100 + '</style>'
                + '<pre><code>' + 'English ' * 100 + '</code></pre>'
                + '<p hidden>secret content</p><p aria-hidden="true">secret annotation</p>'
                + '<p>真正的中文正文，包含已经写下的内容。</p>'
                + '<div class="footer border-top">' + 'English boilerplate ' * 100 + '</div>')
        result = document_metadata(html(body), url='https://devlog.fivsevn.com/article.html', metadata={'languages': ['zh', 'en']})
        doc = Document(result)
        self.assertEqual('zh-CN', doc.html_tag[2]['lang'])
        self.assertEqual('真正的中文正文，包含已经写下的内容。', doc.existing(name='description'))
        self.assertEqual('真正的中文正文，包含已经写下的内容。', visible_text(body))

    def test_existing_head_tags_become_unique_and_input_is_safely_escaped(self):
        old = html('<p>A picture.</p>', '<meta name="description" content="old"><meta property="og:title" content="old">'
                   '<link rel="canonical" href="https://devlog.fivsevn.com/saved/">')
        summary = '中文 & "quotes" </head><script>alert(1)</script>'
        result = document_metadata(old, url='https://devlog.fivsevn.com/current/', metadata={'summary': summary})
        doc = Document(result)
        self.assertEqual('https://devlog.fivsevn.com/saved/', doc.canonical())
        self.assertEqual(summary, doc.existing(name='description'))
        self.assertNotIn('</head><script>alert(1)</script>', result)
        for name in ('description', 'twitter:title', 'twitter:description', 'twitter:card'):
            self.assertEqual(1, sum(tag == 'meta' and attrs.get('name') == name for _, _, tag, attrs in doc.tags))
        for name in ('og:title', 'og:description', 'og:url', 'og:type', 'og:locale'):
            self.assertEqual(1, sum(tag == 'meta' and attrs.get('property') == name for _, _, tag, attrs in doc.tags))
        self.assertEqual('中文 & Notes', doc.existing(property='og:title'))

    def test_body_style_script_bytes_and_repeated_generation_are_stable(self):
        original = html('<main data-x=" A &amp; B "><p>中文正文</p><img src="assets/original.jpg"></main>')
        first = document_metadata(original, url='https://devlog.fivsevn.com/saved/', metadata={'languages': ['zh']})
        self.assertEqual(original.split('<body>', 1)[1], first.split('<body>', 1)[1])
        self.assertIn('<style>.x:before { content: " unchanged "; }</style>', first)
        self.assertEqual(first, document_metadata(first, url='https://devlog.fivsevn.com/saved/', metadata={'languages': ['zh']}))
        self.assertEqual('https://devlog.fivsevn.com/saved/assets/original.jpg', Document(first).existing(property='og:image'))

    def test_real_summary_precedes_excerpt_and_empty_image_only_page_uses_existing_title(self):
        result = document_metadata(html('<p>Long body.</p>'), url='https://devlog.fivsevn.com/a/', metadata={'summary': '已存在的摘要。'})
        self.assertEqual('已存在的摘要。', Document(result).existing(name='description'))
        picture = document_metadata(html('<figure><img src="/photo.webp" alt=""></figure>'), url='https://devlog.fivsevn.com/picture/')
        self.assertEqual('中文 & Notes', Document(picture).existing(name='description'))
        self.assertEqual('summary_large_image', Document(picture).existing(name='twitter:card'))

    def test_non_http_images_are_not_promoted_to_share_metadata(self):
        result = document_metadata(html('<img src="data:image/png,raw"><img src="javascript:bad()">'), url='https://devlog.fivsevn.com/a/')
        self.assertEqual('', Document(result).existing(property='og:image'))
        self.assertEqual('summary', Document(result).existing(name='twitter:card'))

    def test_existing_mixed_language_ui_gets_only_language_attributes(self):
        old = html('<p class="title-zh">本日入荷</p><div class="footer border-top">This site is open source.</div>')
        new = document_metadata(old, url='https://devlog.fivsevn.com/intake/')
        self.assertIn('<p class="title-zh" lang="zh-CN">本日入荷</p>', new)
        self.assertIn('<div class="footer border-top" lang="en">This site is open source.</div>', new)
        self.assertEqual(new, document_metadata(new, url='https://devlog.fivsevn.com/intake/'))

    def test_authored_robot_instructions_are_preserved_and_hidden_default_is_idempotent(self):
        for directive in ('noindex, nofollow', 'index, follow'):
            original = html(head='<meta name="robots" content="' + directive + '">')
            result = document_metadata(original, url='https://devlog.fivsevn.com/a/', noindex=True)
            self.assertIn('<meta name="robots" content="' + directive + '">', result)
            self.assertEqual(1, result.count('name="robots"'))
        first = document_metadata(html(), url='https://devlog.fivsevn.com/a/', noindex=True)
        self.assertEqual('noindex, follow', Document(first).existing(name='robots'))
        self.assertEqual(first, document_metadata(first, url='https://devlog.fivsevn.com/a/', noindex=True))


class DocumentSiteTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / '_site').mkdir()

    def save(self, relative, *, status='active', visibility='public', languages=None, permalink=None, head=''):
        source = self.root / relative
        source.parent.mkdir(parents=True, exist_ok=True)
        metadata = {'id': source.stem, 'title': '文档', 'status': status, 'visibility': visibility, 'languages': languages or ['zh']}
        if permalink:
            metadata['permalink'] = permalink
        source.write_text(dump_frontmatter(metadata) + '\n中文文章。\n')
        output = self.root / '_site' / (permalink.lstrip('/') if permalink else str(Path(relative).with_suffix('.html')))
        if str(output).endswith('/') or output.suffix != '.html':
            output /= 'index.html'
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(html('<p>中文文章。</p>', head))
        return output

    def urls(self):
        root = ElementTree.parse(self.root / '_site/sitemap.xml').getroot()
        return [node.text for node in root.findall('{*}url/{*}loc')]

    def test_sitemap_matches_existing_status_and_visibility_rules_without_removing_access(self):
        public = self.save('published.md')
        legacy = self.save('legacy.md', visibility=None)
        hidden = [self.save(name + '.md', status=status, visibility=visibility)
                  for name, status, visibility in [('hidden', 'hidden', 'public'), ('draft', 'draft', 'public'),
                                                    ('private', 'active', 'private'), ('archive', 'archived', 'public'),
                                                    ('unknown', None, 'public')]]
        self.save('robots-excluded.md', head='<meta name="robots" content="noindex, follow">')
        before = {path: path.read_text().split('<body>', 1)[1] for path in [public, legacy, *hidden]}
        result = prepare(self.root)
        self.assertEqual(2, result['sitemap_urls'])
        self.assertEqual(['https://devlog.fivsevn.com/legacy.html', 'https://devlog.fivsevn.com/published.html'], self.urls())
        for path in hidden:
            self.assertTrue(path.exists())
            self.assertEqual('noindex, follow', Document(path.read_text()).existing(name='robots'))
        for path, body in before.items():
            self.assertEqual(body, path.read_text().split('<body>', 1)[1])
        self.assertEqual(0, prepare(self.root, check=True)['changed'])

    def test_permalink_homepage_and_fieldlog_receipt_paths_are_respected(self):
        page = self.save('posts/date/package/index.md', permalink='/permanent/article.html', languages=['en'])
        self.save('index.md')
        fieldlog = self.root / '_site/natsci/fieldlog/index.html'
        fieldlog.parent.mkdir(parents=True)
        fieldlog.write_text(document_metadata(html(), url='https://devlog.fivsevn.com/natsci/fieldlog/', metadata={'languages': ['zh']}))
        original_fieldlog = fieldlog.read_bytes()
        receipt = fieldlog.parent / 'build-receipt.json'
        receipt.write_text('unchanged receipt bytes')
        fragment = self.root / '_site/intake/data/snippet.html'
        fragment.parent.mkdir(parents=True)
        fragment.write_text('<section>Embedded fragment</section>')
        result = prepare(self.root)
        self.assertEqual(3, result['documents'])
        self.assertEqual('en', Document(page.read_text()).html_tag[2]['lang'])
        self.assertEqual(original_fieldlog, fieldlog.read_bytes())
        self.assertEqual('unchanged receipt bytes', receipt.read_text())
        self.assertEqual('<section>Embedded fragment</section>', fragment.read_text())
        self.assertIn('https://devlog.fivsevn.com/', self.urls())
        self.assertIn('https://devlog.fivsevn.com/permanent/article.html', self.urls())
        self.assertIn('https://devlog.fivsevn.com/natsci/fieldlog/', self.urls())

    def test_robots_preserve_directives_and_check_mode_does_not_write(self):
        output = self.save('中文 page.md')
        robots = self.root / '_site/robots.txt'
        robots.write_text('User-agent: ExampleBot\nDisallow: /private/\n')
        old = output.read_bytes()
        with self.assertRaisesRegex(ValueError, 'stale'):
            prepare(self.root, check=True)
        self.assertEqual(old, output.read_bytes())
        self.assertFalse((self.root / '_site/sitemap.xml').exists())
        prepare(self.root)
        self.assertEqual('User-agent: ExampleBot\nDisallow: /private/\nSitemap: https://devlog.fivsevn.com/sitemap.xml\n', robots.read_text())
        self.assertIn('https://devlog.fivsevn.com/%E4%B8%AD%E6%96%87%20page.html', self.urls())
        self.assertEqual(0, prepare(self.root)['changed'])


if __name__ == '__main__':
    unittest.main()
