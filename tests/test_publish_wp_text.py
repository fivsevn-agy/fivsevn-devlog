import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('trigger',Path(__file__).resolve().parents[1]/'scripts/publish_wp_text.py')
trigger=importlib.util.module_from_spec(spec)
spec.loader.exec_module(trigger)

class TriggerValidationTests(unittest.TestCase):
    def test_markdown_and_frontmatter(self):
        html=trigger.validate('---\nwp_status: publish\n---\n[链接](https://example.com)\n第二行')
        self.assertIn('<a href="https://example.com">链接</a>',html)
        self.assertIn('<br',html)
        self.assertNotIn('wp_status',html)
    def test_bad_frontmatter(self):
        for text in ['---\nunclosed','---\n- list\n---\nbody','---\nwp_status: future\n---\nbody']:
            with self.assertRaises(ValueError):trigger.validate(text)
    def test_empty_is_allowed(self):
        self.assertEqual(trigger.validate('---\nwp_status: publish\n---\n'),'')
    def test_flux_fields_and_path(self):
        self.assertTrue(str(trigger.SOURCE_FILE).endswith('posts/_flux/trigger.md'))
        html=trigger.validate('---\nstatus: published\ntitle: "我的标题"\n---\n正文')
        self.assertEqual(html,'<p>正文</p>')
        for raw in ['---\nstatus: future\n---\nbody','---\ntitle: [bad]\n---\nbody']:
            with self.assertRaises(ValueError):trigger.validate(raw)

if __name__=='__main__': unittest.main()
