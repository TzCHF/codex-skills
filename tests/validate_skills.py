from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "tests", "__pycache__"}
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter")
    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line == "metadata:":
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate_skill_dir(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    readme_file = skill_dir / "README.md"

    if not skill_file.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_dir.name}: {exc}"]

    name = frontmatter.get("name")
    description = frontmatter.get("description")

    if not name:
        errors.append(f"{skill_dir.name}: missing frontmatter name")
    elif name != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name '{name}' does not match folder name")

    if not description:
        errors.append(f"{skill_dir.name}: missing frontmatter description")

    if "# " not in text:
        errors.append(f"{skill_dir.name}: missing markdown title heading")

    if not readme_file.exists():
        errors.append(f"{skill_dir.name}: missing README.md")

    return errors


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(
        path for path in ROOT.iterdir() if path.is_dir() and path.name not in SKIP_DIRS
    )
    if not skill_dirs:
        print("No skill directories found.")
        return 1

    for skill_dir in skill_dirs:
        errors.extend(validate_skill_dir(skill_dir))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skills successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
