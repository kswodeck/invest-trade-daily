"""The pipeline's logic must import without the network stack installed.

`.github/workflows/tests.yml` runs `python -m unittest` on a bare runner with
nothing pip-installed, which is deliberate: the suite is stdlib-only and takes
a twentieth of a second. But the assumption was silent, so nothing enforced it,
and a `import market_data` sitting above its try/except in `_current_price`
turned a missing `requests` into two red tests — and, in production, would have
taken down grading for every position including the ones needing no price.

So the property is a test now. `market_data` is the exception that proves it:
it is the network layer, and a module whose entire job is HTTP is allowed to
need an HTTP library.
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / "scripts"

# Everything the daily pipeline runs whose logic should stand up on its own.
# A module here may still *use* requests or gspread — lazily, inside the
# function that needs it, so importing the module costs nothing.
PURE_MODULES = [
    "add_candidate", "build_context", "check_sheets", "dedupe_positions",
    "ensure_report", "exposure", "note_late_run", "odd_lot", "publish_odd_lot",
    "publish_sheets", "refresh_prices", "report_runs", "report_state",
    "schedule_gate", "step_summary", "validate_report", "watchlist",
    "weekly_digest",
]

# Modules that legitimately need the network stack at import time.
NETWORK_MODULES = ["market_data", "check_sources"]

# Kept free of `.format` placeholders: the source below is full of braces of
# its own, and escaping them all is how this harness grew a bug that made every
# module look broken. The dynamic half is appended with repr() instead.
BLOCKER = """
import sys

BLOCKED = {"requests", "gspread", "google", "jsonschema", "urllib3"}


class Blocker:
    def find_spec(self, name, path=None, target=None):
        root = name.split(".")[0]
        if root in BLOCKED:
            raise ModuleNotFoundError("No module named " + repr(root), name=name)
        return None


sys.meta_path.insert(0, Blocker())
"""


def import_without_dependencies(module: str) -> subprocess.CompletedProcess:
    """Import one module in a subprocess with third-party packages unavailable.

    A subprocess rather than a `sys.modules` patch, because the modules under
    test are already imported by the rest of the suite and a cached import
    would prove nothing.
    """
    source = (BLOCKER
              + f"sys.path.insert(0, {str(SCRIPTS)!r})\n"
              + f"import {module}\n")
    return subprocess.run([sys.executable, "-c", source],
                          capture_output=True, text=True, timeout=60)


class ImportsWithoutThirdPartyPackages(unittest.TestCase):
    def test_every_pipeline_module_imports_on_a_bare_runner(self):
        for module in PURE_MODULES:
            with self.subTest(module=module):
                result = import_without_dependencies(module)
                self.assertEqual(
                    result.returncode, 0,
                    f"{module} needs a third-party package at import time:\\n"
                    f"{result.stderr.strip()[-400:]}")

    def test_the_blocker_actually_blocks(self):
        """A test that cannot fail proves nothing; check the harness bites."""
        result = import_without_dependencies("market_data")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("No module named 'requests'", result.stderr)

    def test_the_network_modules_are_the_only_exceptions(self):
        found = sorted(path.stem for path in SCRIPTS.glob("*.py"))
        self.assertEqual(found, sorted(PURE_MODULES + NETWORK_MODULES),
                         "a script was added or renamed — decide which list it "
                         "belongs in rather than leaving it uncovered")


if __name__ == "__main__":
    unittest.main()
