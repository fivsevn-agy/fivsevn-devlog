"""Execute real navigation JS against geometry/history mocks in Node or JavaScriptCore."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
JSC = Path("/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc")


class FieldlogNavigationTests(unittest.TestCase):
    def test_frame_top_navigation_and_layout_stabilization(self):
        runtime = shutil.which("node") or (str(JSC) if JSC.is_file() else None)
        if runtime is None:
            if sys.platform.startswith("linux"):
                self.fail("Node is required to execute navigation tests on Linux/Actions")
            self.skipTest("Navigation runtime unavailable: Node or JavaScriptCore required")
        source = (ROOT / "natsci/fieldlog/ui/navigation.js").read_text()
        harness = (ROOT / "tests/fieldlog_navigation_cases.js").read_text()
        program = harness + "\nconst output = typeof print === 'function' ? print : console.log;\n"
        program += "runFieldlogNavigationCases(" + json.dumps(source) + ").then(cases => output(JSON.stringify({passed:cases})), error => { output(String(error.stack || error)); throw error; });"
        result = subprocess.run([runtime, "-e", program], text=True, capture_output=True, timeout=20)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout.strip().splitlines()[-1])
        self.assertEqual(len(report["passed"]), 7)


if __name__ == "__main__":
    unittest.main()
