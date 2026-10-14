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

class HandbookOrderTests(unittest.TestCase):
    def note(self, number, title, day='2026-10-13', status='active'):
        path=f'2026/posts-2026-umwelt-game-development-handbook-{number}.md'
        return index.Note(title, day, status, 'note', path, path)

    def ordinary(self, title, day='2026-10-13'):
        path=f'2026/{title}.md'
        return index.Note(title, day, 'active', 'note', path, path)

    def test_current_two_handbooks_show_newest_first(self):
        titles=['游戏开发术语与流程手册', '游戏开发软件地图手册']
        notes=[self.note(f'{i:03}', title) for i,title in enumerate(titles,1)]
        shuffled=[notes[i] for i in [0,1]]
        before=list(shuffled)
        result=index.sort_notes(shuffled,'posts')
        self.assertEqual(result,list(reversed(notes)))
        self.assertEqual(shuffled,before)
        self.assertEqual(index.sort_notes(result,'posts'),result)

    def test_new_installments_sort_numerically_not_lexically(self):
        notes=[self.note(n,'Same title') for n in ['10','2','001','1000','999','008']]
        self.assertEqual([n.source_path for n in index.sort_notes(notes,'posts')],
                         [self.note(n,'Same title').source_path for n in ['1000','999','10','008','2','001']])

    def test_titles_do_not_determine_installment_order(self):
        first=self.note('001','Z renamed title')
        last=self.note('007','A renamed title')
        self.assertEqual(index.sort_notes([first,last],'posts'),[last,first])

    def test_publication_date_takes_precedence_over_installment_number(self):
        newer=self.note('001','Newer date','2026-10-14')
        older=self.note('007','Older date','2026-10-13')
        self.assertEqual(index.sort_notes([older,newer],'posts'),[newer,older])

    def test_dates_remain_primary_and_unrelated_posts_keep_order(self):
        notes=[self.ordinary('new','2026-10-14'),self.note('001','A'),
               self.ordinary('M'),self.note('002','Z'),self.ordinary('B'),
               self.note('003','Later installment','2026-10-14'),
               self.ordinary('old','2026-10-12')]
        baseline=sorted(notes,key=lambda n:(n.date,n.title,n.source_path),reverse=True)
        result=index.sort_notes(notes,'posts')
        self.assertEqual([n.date for n in result],sorted([n.date for n in notes],reverse=True))
        ordinary=lambda items:[n for n in items if 'handbook-' not in n.source_path]
        self.assertEqual(ordinary(result),ordinary(baseline))
        same_day=[n for n in result if n.date=='2026-10-13']
        self.assertEqual(same_day,[notes[3],notes[1],notes[2],notes[4]])
        self.assertCountEqual(result,notes)

    def test_unrelated_numbered_articles_and_other_modules_unchanged(self):
        notes=[self.ordinary('other-series-001'),self.ordinary('other-series-002')]
        baseline=sorted(notes,key=lambda n:(n.date,n.title,n.source_path),reverse=True)
        self.assertEqual(index.sort_notes(notes,'posts'),baseline)
        handbooks=[self.note('001','A'),self.note('002','Z')]
        for module in ['natsci','netcom']:
            self.assertEqual(index.sort_notes(handbooks,module),list(reversed(handbooks)))
        self.assertEqual(index.sort_notes([],'posts'),[])

    def test_collection_filters_and_index_regeneration_are_preserved(self):
        from tempfile import TemporaryDirectory
        from unittest.mock import patch
        with TemporaryDirectory() as directory:
            root=Path(directory)
            for number,title,status,visibility,folder in [
                ('001','A first','active','public','2026'),
                ('002','Z second','active','public','2026'),
                ('003','Hidden','hidden','public','2026'),
                ('004','Private','private','private','2026'),
                ('005','Draft','active','public','_drafts')]:
                path=root/'posts'/folder/f'posts-2026-umwelt-game-development-handbook-{number}.md'
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text('---\n'+yaml.safe_dump(dict(title=title,created='2026-10-13',
                    updated='2026-10-14',module='posts',status=status,visibility=visibility))+'---\nBody\n')
            config=index.MODULES['posts']
            dest=root/config['index']
            dest.write_text('Header\n<!-- AUTO-INDEX:POSTS_RECENT:START -->\nold\n<!-- AUTO-INDEX:POSTS_RECENT:END -->\nFooter\n')
            original={p:p.read_bytes() for p in (root/'posts').rglob('*.md') if p!=dest}
            with patch.object(index,'ROOT',root):
                notes,warnings=index.collect_notes('posts',config)
                self.assertEqual(warnings,[])
                self.assertEqual([n.title for n in notes],['Z second','A first'])
                self.assertEqual([n.date for n in notes],['2026-10-13']*2)
                self.assertTrue(index.update_index(config,index.render_notes(notes)))
                self.assertFalse(index.update_index(config,index.render_notes(notes)))
            rendered=dest.read_text()
            self.assertTrue(rendered.startswith('Header\n'))
            self.assertTrue(rendered.endswith('Footer\n'))
            for note in notes:
                self.assertIn(f'[{note.title}]({note.link})',rendered)
            self.assertEqual({p:p.read_bytes() for p in original},original)

if __name__=='__main__':unittest.main()
