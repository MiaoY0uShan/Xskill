from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from .core import (
    SKILL_ORDER,
    add_task,
    build_semantic_tree,
    init_project,
    load_tasks,
    make_brief,
    project_root,
    record_learning,
    select_next_task,
    update_task_status,
)


def cmd_init(args: argparse.Namespace) -> int:
    created = init_project(args.path, force=args.force)
    print(f"Initialized Musk skills runtime at {project_root(args.path) / '.musk'}")
    if args.force:
        print("Force mode: existing templates/state defaults were overwritten where applicable.")
    print(f"Created/ensured {len(created)} paths.")
    return 0


def cmd_task(args: argparse.Namespace) -> int:
    root = project_root(args.path)
    if args.task_cmd == "add":
        task = add_task(root, args.goal, priority=args.priority, risk=args.risk, checks=args.check or [])
        print(json.dumps(task, ensure_ascii=False, indent=2))
        return 0
    if args.task_cmd == "list":
        tasks = load_tasks(root)
        if args.json:
            print(json.dumps({"tasks": tasks}, ensure_ascii=False, indent=2))
        else:
            for t in tasks:
                checks = ", ".join(t.get("checks", [])) or "-"
                print(f"{t.get('id')} [{t.get('status')}] p={t.get('priority')} risk={t.get('risk')} checks={checks} :: {t.get('goal')}")
        return 0
    if args.task_cmd in {"done", "fail", "block"}:
        status = "blocked" if args.task_cmd == "block" else args.task_cmd
        task = update_task_status(root, args.task_id, status=status, note=args.note or "")
        print(json.dumps(task, ensure_ascii=False, indent=2))
        return 0
    raise ValueError(f"Unknown task command: {args.task_cmd}")


def cmd_index(args: argparse.Namespace) -> int:
    root = project_root(args.path)
    graph = build_semantic_tree(root)
    print(f"Indexed {len(graph['nodes'])} nodes and {len(graph['edges'])} extracted edges.")
    print(f"Wrote {root / '.musk/state/semantic_tree.json'}")
    return 0


def cmd_brief(args: argparse.Namespace) -> int:
    root = project_root(args.path)
    print(make_brief(root, args.step, task_text=args.task or "", as_json=args.json))
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    root = project_root(args.path)
    task = select_next_task(root)
    if not task:
        print("No open tasks.")
        return 0
    step = args.step or "question-requirements"
    print(make_brief(root, step, task_text=task.get("goal", ""), as_json=args.json))
    return 0


def cmd_learn(args: argparse.Namespace) -> int:
    root = project_root(args.path)
    row = record_learning(root, args.text, source=args.source)
    print(json.dumps(row, ensure_ascii=False, indent=2))
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    if not args.command:
        print("No verification command provided.", file=sys.stderr)
        return 2
    result = subprocess.run(args.command, cwd=project_root(args.path), shell=True)
    return result.returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="musk", description="Lean Musk 5-Step skill runtime for AI coding agents.")
    parser.add_argument("--path", default=".", help="Project root. Default: current directory")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Install .musk state, kernel, and skills into a project.")
    p_init.add_argument("path", nargs="?", default=".")
    p_init.add_argument("--force", action="store_true", help="Overwrite existing templates and default state files.")
    p_init.set_defaults(func=cmd_init)

    p_task = sub.add_parser("task", help="Manage the local task queue.")
    task_sub = p_task.add_subparsers(dest="task_cmd", required=True)
    p_add = task_sub.add_parser("add", help="Add an atomic task.")
    p_add.add_argument("goal")
    p_add.add_argument("--priority", type=int, default=3)
    p_add.add_argument("--risk", choices=["low", "medium", "high"], default="medium")
    p_add.add_argument("--check", action="append", help="Verification command. Can be repeated.")
    p_list = task_sub.add_parser("list", help="List tasks.")
    p_list.add_argument("--json", action="store_true")
    for name in ["done", "fail", "block"]:
        p_status = task_sub.add_parser(name, help=f"Mark a task as {name}.")
        p_status.add_argument("task_id")
        p_status.add_argument("--note", default="")
    p_task.set_defaults(func=cmd_task)

    p_index = sub.add_parser("index", help="Build a lightweight semantic tree for the project.")
    p_index.set_defaults(func=cmd_index)

    p_brief = sub.add_parser("brief", help="Generate a prompt brief for one skill step.")
    p_brief.add_argument("step", choices=SKILL_ORDER + ["semantic-memory", "question", "delete", "optimize", "iterate", "automate", "memory"])
    p_brief.add_argument("--task", default="")
    p_brief.add_argument("--json", action="store_true")
    p_brief.set_defaults(func=cmd_brief)

    p_next = sub.add_parser("next", help="Select the highest-priority open task and generate the next skill brief.")
    p_next.add_argument("--step", choices=SKILL_ORDER + ["semantic-memory", "question", "delete", "optimize", "iterate", "automate", "memory"], default="question-requirements")
    p_next.add_argument("--json", action="store_true")
    p_next.set_defaults(func=cmd_next)

    p_learn = sub.add_parser("learn", help="Append a learning to progress.jsonl.")
    p_learn.add_argument("text")
    p_learn.add_argument("--source", default="manual")
    p_learn.set_defaults(func=cmd_learn)

    p_verify = sub.add_parser("verify", help="Run a verification command from the project root.")
    p_verify.add_argument("command")
    p_verify.set_defaults(func=cmd_verify)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:  # noqa: BLE001 - CLI boundary
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
