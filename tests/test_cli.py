from __future__ import annotations

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from musk_skills.cli import main


class CliTests(unittest.TestCase):
    def test_cli_init_and_task(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.assertEqual(main(["init", str(root)]), 0)
            self.assertTrue((root / ".musk").exists())
            buf = io.StringIO()
            with redirect_stdout(buf):
                self.assertEqual(main(["--path", str(root), "task", "add", "Ship MVP", "--priority", "4"]), 0)
            self.assertIn("Ship MVP", buf.getvalue())
            buf = io.StringIO()
            with redirect_stdout(buf):
                self.assertEqual(main(["--path", str(root), "task", "list"]), 0)
            self.assertIn("T001", buf.getvalue())

    def test_cli_index(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.assertEqual(main(["init", str(root)]), 0)
            (root / "README.md").write_text("# Demo\n", encoding="utf-8")
            buf = io.StringIO()
            with redirect_stdout(buf):
                self.assertEqual(main(["--path", str(root), "index"]), 0)
            self.assertIn("Indexed", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
