"""Offline regression tests. All WordPress calls are mocked; no real posts are made."""
from __future__ import annotations

import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch

import requests
import yaml
from scripts import publish_wp_text as pub


class FrontmatterTests(unittest.TestCase):
    def test_plain_markdown_is_still_accepted(self):
        self.assertEqual(pub.split_frontmatter("Hello\n"), ({}, "Hello\n"))

    def test_configuration_stays_out_of_body(self):
        meta, body = pub.split_frontmatter("---\nwp_status: publish\ncategory: posts\n---\n\nHello\n")
        self.assertEqual(meta, {"wp_status": "publish", "category": "posts"})
        self.assertEqual(body, "Hello\n")

    def test_crlf_and_bom(self):
        meta, body = pub.split_frontmatter("\ufeff---\r\ncategory: posts\r\n---\r\nHello")
        self.assertEqual(meta["category"], "posts")
        self.assertEqual(body, "Hello")

    def test_empty_metadata(self):
        self.assertEqual(pub.split_frontmatter("---\n---\nHello"), ({}, "Hello"))

    def test_malformed_or_non_mapping_yaml_rejected(self):
        for raw in ("---\ncategory: [\n---\nHello", "---\n- posts\n---\nHello", "---\nfalse\n---\nHello"):
            with self.subTest(raw=raw), self.assertRaises((ValueError, yaml.YAMLError)):
                pub.split_frontmatter(raw)

    def test_unclosed_frontmatter_never_becomes_post_text(self):
        with self.assertRaises(ValueError):
            pub.split_frontmatter("---\nwp_status: publish\nHello")

    def test_separator_must_be_its_own_line(self):
        with self.assertRaises(ValueError):
            pub.split_frontmatter("---\ncategory: posts\n---not-a-separator\nHello")

    def test_categories_and_typo_still_work(self):
        cases = [({}, ["posts"]), ({"category": "posts"}, ["posts"]),
                 ({"catagory": "posts"}, ["posts"]),
                 ({"categories": ["posts", "other", "posts"]}, ["posts", "other"])]
        for meta, expected in cases:
            with self.subTest(meta=meta):
                self.assertEqual(pub.normalize_category_slugs(meta), expected)


class GitEventTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "posts/_wordpress/trigger.md"
        self.source.parent.mkdir(parents=True)
        self.source.write_text("---\ncategory: posts\n---\nFirst", encoding="utf-8")
        self.run_git("init", "--initial-branch=main")
        self.run_git("config", "user.name", "Offline Test")
        self.run_git("config", "user.email", "test@example.invalid")
        self.first = self.commit("Initial trigger")
        self.addCleanup(patch.stopall)
        patch.object(pub, "ROOT", self.root).start()
        patch.object(pub, "SOURCE_FILE", self.source).start()
        self.event_path = self.root / "event.json"
        patch.dict(os.environ, {"GITHUB_ACTIONS": "true", "GITHUB_REF": "refs/heads/main",
                              "GITHUB_EVENT_PATH": str(self.event_path)}, clear=True).start()

    def run_git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, text=True, check=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.strip()

    def commit(self, message):
        self.run_git("add", "posts")
        if (self.root / "notes.md").exists():
            self.run_git("add", "notes.md")
        self.run_git("commit", "-m", message)
        return self.run_git("rev-parse", "HEAD")

    def event(self, before, after, kind="push", ref="refs/heads/main"):
        self.event_path.write_text(json.dumps({"before": before, "after": after}), encoding="utf-8")
        os.environ.update(GITHUB_EVENT_NAME=kind, GITHUB_SHA=after, GITHUB_REF=ref)

    def edit_trigger(self, body="Second"):
        self.source.write_text("---\ncategory: posts\n---\n" + body, encoding="utf-8")
        return self.commit("Change trigger")

    def maintenance(self):
        (self.root / "notes.md").write_text("Documentation maintenance", encoding="utf-8")
        return self.commit("Maintenance only")

    def test_trigger_push_is_allowed(self):
        current = self.edit_trigger()
        self.event(self.first, current)
        self.assertTrue(pub.publishing_allowed())
        self.assertEqual(pub.source_commit(), current)

    def test_maintenance_push_cannot_publish_old_text(self):
        current = self.maintenance()
        self.event(self.first, current)
        self.assertFalse(pub.publishing_allowed())

    def test_manual_after_maintenance_uses_original_source_identity(self):
        current = self.maintenance()
        self.event(self.first, current, kind="workflow_dispatch")
        self.assertTrue(pub.publishing_allowed())
        self.assertEqual(pub.source_commit(), self.first)

    def test_batched_push_with_later_maintenance_keeps_trigger_identity(self):
        changed = self.edit_trigger()
        current = self.maintenance()
        self.event(self.first, current)
        self.assertTrue(pub.publishing_allowed())
        self.assertEqual(pub.source_commit(), changed)

    def test_identical_text_can_be_posted_in_a_later_distinct_revision(self):
        changed = self.edit_trigger()
        later = self.edit_trigger("First")
        self.event(changed, later)
        self.assertTrue(pub.publishing_allowed())
        self.assertEqual(pub.source_commit(), later)
        self.assertNotEqual(later, self.first)

    def test_pull_request_and_unknown_events_cannot_publish(self):
        for event in ("pull_request", "pull_request_target", "schedule", ""):
            with self.subTest(event=event):
                self.event(self.first, self.first, kind=event)
                self.assertFalse(pub.publishing_allowed())

    def test_non_main_manual_run_cannot_publish(self):
        self.event(self.first, self.first, kind="workflow_dispatch", ref="refs/heads/test")
        self.assertFalse(pub.publishing_allowed())

    def test_wrong_checkout_rejected(self):
        self.event(self.first, "a" * 40)
        with self.assertRaises(ValueError):
            pub.publishing_allowed()

    def test_missing_or_invalid_push_base_rejected(self):
        for before in ("", "0" * 40, "not-a-sha"):
            with self.subTest(before=before):
                self.event(before, self.first)
                with self.assertRaises(ValueError):
                    pub.publishing_allowed()

    def test_shallow_checkout_rejected(self):
        with patch.object(pub, "git", return_value="true"), self.assertRaises(ValueError):
            pub.source_commit()

    def test_deleted_trigger_fails_without_wordpress_calls(self):
        self.source.unlink()
        current = self.commit("Delete trigger")
        self.event(self.first, current)
        with patch.object(pub.requests, "get") as get, patch.object(pub.requests, "post") as post:
            with self.assertRaises(FileNotFoundError):
                pub.main([])
            get.assert_not_called()
            post.assert_not_called()


class PublishingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / "trigger.md"
        self.source.write_text("---\nwp_status: publish\ncategory: posts\n---\nHello", encoding="utf-8")
        self.addCleanup(patch.stopall)
        patch.dict(os.environ, {}, clear=True).start()
        patch.object(pub, "SOURCE_FILE", self.source).start()
        patch.object(pub, "WP_SITE_URL", "https://wordpress.example.invalid").start()
        patch.object(pub, "WP_USERNAME", "offline-test").start()
        patch.object(pub, "WP_APP_PASSWORD", "not-a-real-password").start()
        patch.object(pub, "source_commit", return_value="a" * 40).start()
        self.render = patch.object(pub, "render_body", return_value="<p>Hello</p>").start()
        self.get = patch.object(pub.requests, "get").start()
        self.post = patch.object(pub.requests, "post").start()
        self.get.side_effect = self.get_response
        self.post.return_value = self.response({"id": 123, "link": "https://wordpress.example.invalid/post"})
        self.output = io.StringIO()
        self.redirect = contextlib.redirect_stdout(self.output)
        self.redirect.__enter__()
        self.addCleanup(self.redirect.__exit__, None, None, None)

    @staticmethod
    def response(data):
        response = Mock()
        response.json.return_value = data
        response.raise_for_status.return_value = None
        return response

    def get_response(self, endpoint, **kwargs):
        return self.response([{"id": 7}] if endpoint.endswith("/categories") else [])

    def test_publish_payload_preserves_contract(self):
        self.assertEqual(pub.main([]), 0)
        self.post.assert_called_once()
        payload = self.post.call_args.kwargs["json"]
        self.assertEqual(payload["slug"], "github-text-aaaaaaa")
        self.assertEqual(payload["status"], "publish")
        self.assertEqual(payload["content"], "<p>Hello</p>")
        self.assertEqual(payload["categories"], [7])
        self.assertRegex(payload["title"], r"^\d{1,2} [A-Z][a-z]{2}, \d{4} \d{2}:\d{2}$")
        self.assertEqual(self.post.call_args.kwargs["timeout"], 30)

    def test_explicit_slug_and_draft_status_preserved(self):
        self.source.write_text("---\nslug: custom-slug\nwp_status: draft\ncatagory: posts\n---\nHello", encoding="utf-8")
        pub.main([])
        payload = self.post.call_args.kwargs["json"]
        self.assertEqual((payload["slug"], payload["status"]), ("custom-slug", "draft"))
        pub.source_commit.assert_not_called()

    def test_existing_post_in_each_supported_status_is_not_overwritten(self):
        for existing_status in pub.POST_STATUSES:
            with self.subTest(status=existing_status):
                self.get.reset_mock()
                self.get.side_effect = lambda endpoint, **kw: self.response(
                    [{"id": 123, "link": "existing"}] if kw["params"].get("status") == existing_status else [])
                self.assertEqual(pub.main([]), 0)
                self.post.assert_not_called()
                self.assertFalse(any(call.args[0].endswith("/categories") for call in self.get.call_args_list))

    def test_retry_after_success_skips_second_post(self):
        self.get.side_effect = lambda endpoint, **kw: self.response(
            [{"id": 7}] if endpoint.endswith("/categories") else
            ([{"id": 123, "link": "existing"}] if self.post.call_count else []))
        pub.main([])
        pub.main([])
        self.post.assert_called_once()

    def test_maintenance_exit_does_not_read_source_or_call_wordpress(self):
        self.source.unlink()
        with patch.object(pub, "publishing_allowed", return_value=False):
            self.assertEqual(pub.main([]), 0)
        self.get.assert_not_called()
        self.post.assert_not_called()

    def test_dry_run_needs_no_credentials_and_sends_no_requests(self):
        with patch.object(pub, "WP_USERNAME", ""), patch.object(pub, "WP_APP_PASSWORD", ""):
            self.assertEqual(pub.main(["--dry-run"]), 0)
        self.get.assert_not_called()
        self.post.assert_not_called()
        self.assertIn("Preview only", self.output.getvalue())

    def test_empty_body_sends_no_requests(self):
        for text in ("", "---\nwp_status: publish\n---\n  "):
            with self.subTest(text=text):
                self.source.write_text(text, encoding="utf-8")
                self.assertEqual(pub.main([]), 0)
        self.get.assert_not_called()
        self.post.assert_not_called()

    def test_invalid_frontmatter_and_status_send_no_requests(self):
        for text in ("---\ncategory: posts\nHello", "---\nwp_status: publsh\n---\nHello"):
            with self.subTest(text=text):
                self.source.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    pub.main([])
        self.get.assert_not_called()
        self.post.assert_not_called()

    def test_lookup_failure_never_falls_through_to_create(self):
        self.get.side_effect = requests.Timeout("offline simulated timeout")
        with self.assertRaises(requests.Timeout):
            pub.main([])
        self.post.assert_not_called()

    def test_unexpected_api_shape_never_creates(self):
        self.get.side_effect = None
        self.get.return_value = self.response({"error": "unexpected"})
        with self.assertRaises(ValueError):
            pub.main([])
        self.post.assert_not_called()

    def test_missing_category_prevents_create(self):
        self.get.side_effect = lambda *args, **kwargs: self.response([])
        with self.assertRaises(ValueError):
            pub.main([])
        self.post.assert_not_called()

    def test_post_timeout_is_not_automatically_retried(self):
        self.post.side_effect = requests.Timeout("WordPress may already have saved it")
        with self.assertRaises(requests.Timeout):
            pub.main([])
        self.post.assert_called_once()

    def test_check_event_emits_skip_without_credentials(self):
        output_path = Path(self.temp.name) / "output.txt"
        with patch.dict(os.environ, {"GITHUB_OUTPUT": str(output_path)}), patch.object(pub, "publishing_allowed", return_value=False):
            self.assertEqual(pub.main(["--check-event"]), 0)
        self.assertEqual(output_path.read_text(), "publish=false\n")
        self.get.assert_not_called()
        self.post.assert_not_called()

    def test_check_event_validates_source_before_emit(self):
        output_path = Path(self.temp.name) / "output.txt"
        pub.source_commit.side_effect = ValueError("missing history")
        with patch.dict(os.environ, {"GITHUB_OUTPUT": str(output_path)}), patch.object(pub, "publishing_allowed", return_value=True):
            with self.assertRaises(ValueError):
                pub.main(["--check-event"])
        self.assertFalse(output_path.exists())
        self.post.assert_not_called()


class WorkflowTests(unittest.TestCase):
    def test_secrets_are_only_in_gated_publishing_step(self):
        root = Path(__file__).resolve().parents[1]
        # BaseLoader keeps YAML's `on` key from becoming a YAML 1.1 boolean.
        workflow = yaml.load((root / ".github/workflows/publish-wp-trigger.yml").read_text(), Loader=yaml.BaseLoader)
        self.assertEqual(workflow["permissions"], {"contents": "read"})
        self.assertEqual(workflow["on"]["push"]["branches"], ["main"])
        self.assertIn("pull_request", workflow["on"])
        self.assertEqual(workflow["concurrency"]["queue"], "max")
        self.assertEqual(workflow["concurrency"]["cancel-in-progress"], "false")
        steps = workflow["jobs"]["publish"]["steps"]
        self.assertEqual(steps[0]["with"]["fetch-depth"], "0")
        self.assertEqual(steps[0]["with"]["persist-credentials"], "false")
        secret_steps = [step for step in steps if "secrets." in json.dumps(step)]
        self.assertEqual(len(secret_steps), 1)
        self.assertEqual(secret_steps[0], steps[-1])
        self.assertIn("steps.gate.outputs.publish == 'true'", steps[-1]["if"])
        self.assertIn("github.ref == 'refs/heads/main'", steps[-1]["if"])
        self.assertTrue(any("--dry-run" in step.get("run", "") for step in steps[:-1]))


class RenderingTests(unittest.TestCase):
    def test_real_markdown_rendering_unchanged(self):
        import markdown
        for body in ("first\nsecond", "- one\n- two", "**bold** and [link](https://example.com)", "| A | B |\n|---|---|\n| 1 | 2 |"):
            with self.subTest(body=body):
                expected = markdown.markdown(body, extensions=["extra", "sane_lists", "nl2br"])
                self.assertEqual(pub.render_body(body), expected)


if __name__ == "__main__":
    unittest.main()
