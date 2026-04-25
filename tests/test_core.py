from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from musk_skills.core import (
    add_task,
    build_semantic_tree,
    init_project,
    load_tasks,
    make_brief,
    update_task_status,
)


class CoreTests(unittest.TestCase):
    def test_init_project_creates_runtime(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            init_project(root)
            self.assertTrue((root / ".musk/kernel/SKILL.md").exists())
            self.assertTrue((root / ".musk/skills/question-requirements/SKILL.md").exists())
            self.assertTrue((root / ".musk/state/project.json").exists())
            self.assertTrue((root / ".musk/state/tasks.json").exists())

    def test_task_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            init_project(root)
            task = add_task(root, "Add login rate limiting", priority=5, risk="high", checks=["pytest"])
            self.assertEqual(task["id"], "T001")
            self.assertEqual(load_tasks(root)[0]["status"], "open")
            updated = update_task_status(root, "T001", "done", note="pytest passed")
            self.assertEqual(updated["status"], "done")
            self.assertEqual(updated["notes"][0]["note"], "pytest passed")

    def test_semantic_tree_index_and_brief(self) -> None:
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            init_project(root)
            src = root / "src"
            src.mkdir()
            (src / "auth.py").write_text('''"""Auth module."""\nimport os\n\ndef login(user):\n    return True\n''', encoding="utf-8")
            graph = build_semantic_tree(root)
            self.assertTrue(graph["nodes"])
            tree_path = root / ".musk/state/semantic_tree.json"
            self.assertTrue(json.loads(tree_path.read_text(encoding="utf-8"))["nodes"])
            brief = make_brief(root, "question", task_text="Fix auth login")
            self.assertIn("question-requirements", brief)
            self.assertIn("src/auth.py", brief)


if __name__ == "__main__":
    unittest.main()
