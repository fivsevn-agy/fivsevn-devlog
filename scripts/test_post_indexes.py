"""Protect publication discovery and links when articles move into bundles."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import update_module_indexes as indexes


class PostIndexesTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.root_patch = patch.object(indexes, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def article(self, path, *, module="posts", title="Article", status="active"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            f"---\nmodule: {module}\ntitle: {title}\nstatus: {status}\n"
            "created: '2026-10-13'\ntype: note\n"
            "original_url: https://fivsevn.com/old-post/\n---\nBody\n"
        )

    def test_nested_posts_link_locally_and_keep_nonpublic_files_out(self):
        self.article("posts/2026/10/published/index.md")
        self.article("posts/2026/10/hidden/index.md", status="hidden")
        self.article("posts/_drafts/draft.md")
        self.article("posts/2026/10/published/assets/README.md")
        self.article("posts/index.md")
        notes, warnings = indexes.collect_notes("posts", indexes.MODULES["posts"])
        self.assertEqual(warnings, [])
        self.assertEqual([note.link for note in notes], ["2026/10/published/index.md"])

    def test_other_modules_keep_external_link_behavior(self):
        self.article("netcom/example.md", module="netcom")
        self.article("netcom/2026/10/unused/index.md", module="netcom")
        notes, warnings = indexes.collect_notes("netcom", indexes.MODULES["netcom"])
        self.assertEqual(warnings, [])
        self.assertEqual([note.link for note in notes], ["https://fivsevn.com/old-post/"])

    def test_ai_directory_excludes_its_authoring_protocol(self):
        self.article("posts/ai-discourse-analysis/2026/03/001-case/index.md")
        self.article("posts/ai-discourse-analysis/ai-posts-boot-protocol.md")
        notes, warnings = indexes.collect_notes(
            "ai-discourse-analysis", indexes.MODULES["ai-discourse-analysis"]
        )
        self.assertEqual(warnings, [])
        self.assertEqual([note.link for note in notes], ["2026/03/001-case/index.md"])

    def test_same_day_handbook_installments_keep_latest_first(self):
        self.article("posts/2026/10/posts-2026-umwelt-game-development-handbook-001/index.md", title="Z first installment")
        self.article("posts/2026/10/posts-2026-umwelt-game-development-handbook-002/index.md", title="A second installment")
        notes, _ = indexes.collect_notes("posts", indexes.MODULES["posts"])
        self.assertIn("-002/", notes[0].source_path)
        self.assertIn("-001/", notes[1].source_path)


if __name__ == "__main__":
    unittest.main()
