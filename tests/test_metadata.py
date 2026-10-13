"""Offline regression checks for metadata and content helpers."""
from pathlib import Path
import sys, unittest
import yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import apply_draft_frontmatter as draft
import update_module_indexes as index

class DraftTests(unittest.TestCase):
    def test_title_punctuation_roundtrips(self):
        for title in ['QA: 游戏测试','游戏 QA # 测试笔记','It\'s "fine"',r'\LaTeX','[list]','true','2026-02-31','空行\n第二行']:
            with self.subTest(title=title):
                raw=draft.make_frontmatter('posts','posts-draft-001',title,'2026-10-13')
                self.assertEqual(yaml.safe_load(raw.split('---')[1])['title'],title)
    def test_existing_metadata_not_renamed(self):
        self.assertTrue(draft.should_skip(Path('note.md'),'---\nid: fixed\n---\nText'))

class IndexTests(unittest.TestCase):
    def test_real_yaml_title_and_date(self):
        fm=index.parse_frontmatter('---\ntitle: "QA: # 测试"\ncreated: 2026-10-13\n---\n')
        self.assertEqual(fm['title'],'QA: # 测试');self.assertEqual(fm['created'],'2026-10-13')
    def test_folded_title(self):
        self.assertEqual(index.parse_frontmatter('---\ntitle: >-\n  folded\n  title\n---\n')['title'],'folded title')
    def test_literal_replacement(self):
        original='<!-- AUTO-INDEX:X:START -->\nold\n<!-- AUTO-INDEX:X:END -->'
        body=r'- title \LaTeX \1'
        result,found=index.replace_between_markers(original,'X',body)
        self.assertTrue(found);self.assertIn(body,result)
        self.assertEqual(index.replace_between_markers(result,'X',body)[0],result)
    def test_calendar_validation(self):
        for text in ['2026-02-31','2026-13-01','2025-02-29']:self.assertIsNone(index.normalize_date(text))
        self.assertEqual(index.normalize_date('2024.02.29'),'2024-02-29')
    def test_publish_control_path_is_not_an_article(self):
        root=ROOT/'posts'
        self.assertTrue(index.should_skip_path(root/'_wordpress/trigger.md',root,index.MODULES['posts']['exclude_dirs']))
    def test_readme_excluded(self):
        root=ROOT/'posts';self.assertTrue(index.should_skip_path(root/'README.md',root,set()))
    def test_date_precedence_unchanged(self):
        self.assertEqual(index.get_note_date({'created':'2025-01-01','updated':'2026-10-13'}),'2025-01-01')
    def test_status_rules_unchanged(self):
        for value in ['hidden','private','archived']:self.assertEqual(index.status_mode(value),'hide')
        for value in ['active','publish','published']:self.assertEqual(index.status_mode(value),'link')
        self.assertEqual(index.status_mode('draft'),'text')
if __name__=='__main__':unittest.main()
