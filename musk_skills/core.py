from __future__ import annotations

import json
import os
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from importlib import resources
from pathlib import Path
from typing import Any, Iterable

STATE_DIR = ".musk/state"
SKILLS_DIR = ".musk/skills"
KERNEL_DIR = ".musk/kernel"

SKILL_ORDER = [
    "question-requirements",
    "delete-scope",
    "optimize-path",
    "shorten-iteration",
    "automate-after-stable",
]

STEP_ALIASES = {
    "question": "question-requirements",
    "requirements": "question-requirements",
    "delete": "delete-scope",
    "scope": "delete-scope",
    "optimize": "optimize-path",
    "simplify": "optimize-path",
    "iterate": "shorten-iteration",
    "accelerate": "shorten-iteration",
    "automate": "automate-after-stable",
    "memory": "semantic-memory",
}

EXCLUDED_DIRS = {
    ".git", ".musk", "node_modules", "dist", "build", ".venv", "venv",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", "coverage",
}
TEXT_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", ".java", ".kt",
    ".rb", ".php", ".swift", ".c", ".h", ".cpp", ".hpp", ".cs",
    ".md", ".mdx", ".txt", ".json", ".yaml", ".yml", ".toml", ".ini",
    ".html", ".css", ".scss", ".sql", ".sh", ".zsh", ".bash",
}

@dataclass(frozen=True)
class Task:
    id: str
    goal: str
    priority: int = 3
    risk: str = "medium"
    status: str = "open"
    checks: tuple[str, ...] = ()
    created_at: str = ""
    updated_at: str = ""


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def project_root(path: str | Path = ".") -> Path:
    return Path(path).expanduser().resolve()


def state_path(root: Path, filename: str) -> Path:
    return root / STATE_DIR / filename


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def copy_resource_tree(package_subdir: str, destination: Path, force: bool = False) -> None:
    src = resources.files("musk_skills") / package_subdir
    destination.mkdir(parents=True, exist_ok=True)
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = destination / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            if target.exists() and not force:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(item.read_bytes())


def init_project(path: str | Path = ".", force: bool = False) -> list[Path]:
    root = project_root(path)
    created: list[Path] = []
    dirs = [root / ".musk", root / STATE_DIR, root / SKILLS_DIR, root / KERNEL_DIR, root / ".musk/runs"]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        created.append(d)

    copy_resource_tree("templates/skills", root / SKILLS_DIR, force=force)
    copy_resource_tree("templates/kernel", root / KERNEL_DIR, force=force)
    copy_resource_tree("templates/state", root / STATE_DIR, force=force)

    for filename, default in {
        "progress.jsonl": None,
        "decisions.jsonl": None,
    }.items():
        p = root / STATE_DIR / filename
        if not p.exists() or force:
            p.write_text("", encoding="utf-8")
            created.append(p)
    return created


def normalize_step(step: str) -> str:
    step = step.strip().lower()
    return STEP_ALIASES.get(step, step)


def load_project_state(root: Path) -> dict[str, Any]:
    return read_json(state_path(root, "project.json"), {})


def load_tasks(root: Path) -> list[dict[str, Any]]:
    data = read_json(state_path(root, "tasks.json"), {"tasks": []})
    return data.get("tasks", [])


def save_tasks(root: Path, tasks: list[dict[str, Any]]) -> None:
    write_json(state_path(root, "tasks.json"), {"tasks": tasks})


def next_task_id(tasks: Iterable[dict[str, Any]]) -> str:
    max_num = 0
    for task in tasks:
        m = re.match(r"T(\d+)$", str(task.get("id", "")))
        if m:
            max_num = max(max_num, int(m.group(1)))
    return f"T{max_num + 1:03d}"


def add_task(root: Path, goal: str, priority: int = 3, risk: str = "medium", checks: list[str] | None = None) -> dict[str, Any]:
    tasks = load_tasks(root)
    t = now_iso()
    task = {
        "id": next_task_id(tasks),
        "goal": goal,
        "priority": priority,
        "risk": risk,
        "status": "open",
        "checks": checks or [],
        "created_at": t,
        "updated_at": t,
    }
    tasks.append(task)
    save_tasks(root, tasks)
    append_jsonl(state_path(root, "progress.jsonl"), {
        "time": t,
        "event": "task_added",
        "task_id": task["id"],
        "goal": goal,
    })
    return task


def update_task_status(root: Path, task_id: str, status: str, note: str = "") -> dict[str, Any]:
    tasks = load_tasks(root)
    t = now_iso()
    for task in tasks:
        if task.get("id") == task_id:
            task["status"] = status
            task["updated_at"] = t
            if note:
                task.setdefault("notes", []).append({"time": t, "note": note})
            save_tasks(root, tasks)
            append_jsonl(state_path(root, "progress.jsonl"), {
                "time": t,
                "event": f"task_{status}",
                "task_id": task_id,
                "note": note,
            })
            return task
    raise ValueError(f"Task not found: {task_id}")


def select_next_task(root: Path) -> dict[str, Any] | None:
    open_tasks = [t for t in load_tasks(root) if t.get("status") == "open"]
    if not open_tasks:
        return None
    return sorted(open_tasks, key=lambda t: (-int(t.get("priority", 3)), t.get("created_at", "")))[0]


def read_skill(root: Path, step: str) -> str:
    skill = normalize_step(step)
    path = root / SKILLS_DIR / skill / "SKILL.md"
    if not path.exists():
        raise ValueError(f"Unknown skill: {step}. Expected one of: {', '.join(SKILL_ORDER + ['semantic-memory'])}")
    return path.read_text(encoding="utf-8")


def detect_tags(text: str, path: Path) -> list[str]:
    haystack = f"{path.as_posix()}\n{text[:5000]}".lower()
    tags = []
    candidates = {
        "auth": ["auth", "login", "session", "jwt", "oauth"],
        "api": ["api", "route", "endpoint", "controller"],
        "test": ["test", "pytest", "unittest", "spec", "describe("],
        "database": ["database", "db", "sql", "migration", "schema"],
        "ui": ["react", "vue", "html", "css", "component", "frontend"],
        "config": ["config", "toml", "yaml", "env", "settings"],
        "docs": ["readme", "docs", "architecture", "guide"],
        "security": ["password", "token", "secret", "csrf", "xss", "permission"],
    }
    for tag, needles in candidates.items():
        if any(n in haystack for n in needles):
            tags.append(tag)
    return sorted(set(tags))


def summarize_text(text: str, path: Path) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return f"Empty {path.suffix or 'text'} file."
    for line in lines[:30]:
        if line.startswith("#"):
            return line.lstrip("# ")[:180]
        if line.startswith(('"""', "'''")) and len(line.strip('"\'')) > 10:
            return line.strip('"\'')[:180]
    return lines[0][:180]


def file_kind(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".md", ".mdx", ".txt"}:
        return "doc"
    if ext in {".json", ".yaml", ".yml", ".toml", ".ini"}:
        return "config"
    if "test" in path.as_posix().lower() or ext in {".spec", ".test"}:
        return "test"
    return "code" if ext in TEXT_EXTENSIONS else "asset"


def scan_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        current = Path(dirpath)
        for filename in filenames:
            path = current / filename
            if path.suffix.lower() in TEXT_EXTENSIONS and path.stat().st_size <= 300_000:
                paths.append(path)
    return sorted(paths)


def build_semantic_tree(root: Path) -> dict[str, Any]:
    nodes = []
    edges = []
    for path in scan_files(root):
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        node_id = rel.replace("/", ":")
        tags = detect_tags(text, path)
        nodes.append({
            "id": node_id,
            "type": file_kind(path),
            "path": rel,
            "summary": summarize_text(text, path),
            "tags": tags,
            "risk": "high" if "security" in tags or "auth" in tags else "medium" if "api" in tags or "database" in tags else "low",
        })
        # Lightweight extracted dependency edges for common import forms.
        for match in re.finditer(r"^\s*(?:from\s+([\w\.]+)\s+import|import\s+([\w\.]+)|import\s+.*?from\s+['\"]([^'\"]+))", text, re.MULTILINE):
            dep = next((g for g in match.groups() if g), None)
            if dep:
                edges.append({
                    "from": node_id,
                    "to": dep,
                    "relation": "imports",
                    "evidence": "EXTRACTED",
                    "confidence": 0.8,
                })
    graph = {
        "schema_version": "0.1",
        "generated_at": now_iso(),
        "root": root.as_posix(),
        "nodes": nodes,
        "edges": edges,
    }
    write_json(state_path(root, "semantic_tree.json"), graph)
    append_jsonl(state_path(root, "progress.jsonl"), {
        "time": now_iso(),
        "event": "semantic_tree_indexed",
        "nodes": len(nodes),
        "edges": len(edges),
    })
    return graph


def related_nodes(root: Path, task_text: str, limit: int = 8) -> list[dict[str, Any]]:
    graph = read_json(state_path(root, "semantic_tree.json"), {"nodes": []})
    terms = {t.lower() for t in re.findall(r"[A-Za-z0-9_\-/\.]+", task_text) if len(t) >= 3}
    scored = []
    for node in graph.get("nodes", []):
        blob = " ".join([
            str(node.get("id", "")), str(node.get("path", "")), str(node.get("summary", "")),
            " ".join(node.get("tags", [])),
        ]).lower()
        score = sum(1 for term in terms if term in blob)
        if score:
            scored.append((score, node))
    return [node for _, node in sorted(scored, key=lambda item: (-item[0], item[1].get("path", "")))[:limit]]


def make_brief(root: Path, step: str, task_text: str = "", as_json: bool = False) -> str:
    skill = normalize_step(step)
    project = load_project_state(root)
    selected_task = select_next_task(root)
    active_task = task_text or (selected_task or {}).get("goal", "")
    nodes = related_nodes(root, active_task) if active_task else []
    payload = {
        "step": skill,
        "task": active_task,
        "project": project,
        "selected_task": selected_task,
        "relevant_nodes": nodes,
        "skill_file": f"{SKILLS_DIR}/{skill}/SKILL.md",
        "output_required": "Follow the skill Output Contract exactly.",
    }
    if as_json:
        return json.dumps(payload, ensure_ascii=False, indent=2)
    lines = [
        f"# Musk Step Brief: {skill}",
        "",
        f"Task: {active_task or '[no task selected]'}",
        "",
        "## Project Constraints",
    ]
    for c in project.get("constraints", []):
        lines.append(f"- {c}")
    if not project.get("constraints"):
        lines.append("- [none recorded]")
    lines.extend(["", "## Relevant Semantic Nodes"])
    if nodes:
        for node in nodes:
            lines.append(f"- `{node.get('path')}` — {node.get('summary')} tags={node.get('tags', [])} risk={node.get('risk')}")
    else:
        lines.append("- [none found; run `musk index` or tighten the task text]")
    lines.extend([
        "",
        "## Skill Invocation",
        f"Read `{SKILLS_DIR}/{skill}/SKILL.md` and execute only that skill.",
        "Return the skill's required output contract. Do not perform later steps unless explicitly requested.",
    ])
    return "\n".join(lines) + "\n"


def record_learning(root: Path, text: str, source: str = "manual") -> dict[str, Any]:
    row = {"time": now_iso(), "event": "learning", "source": source, "text": text}
    append_jsonl(state_path(root, "progress.jsonl"), row)
    return row
