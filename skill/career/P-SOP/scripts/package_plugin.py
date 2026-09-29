#!/usr/bin/env python3
"""Bundle the two maintained skills as a p-sop plugin; never generate dashboards."""

import argparse
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


SOP_ROOT = Path(__file__).resolve().parents[1]
BOARD_ROOT = SOP_ROOT.parent / "p-sop-build-pp"
PROJECT_ROOT = SOP_ROOT.parents[2]
MANIFEST = {
    "name": "p-sop",
    "version": "0.2.0",
    "description": "项目开发 SOP 与可独立使用的项目进度看板。",
    "author": {"name": "Auhyuan"},
    "skills": "./skills/",
    "interface": {
        "displayName": "P-SOP",
        "shortDescription": "规范项目开发，并按需独立构建项目进度看板。",
        "longDescription": "包含 p-sop 项目开发流程与 build-pp 项目进度看板两项 Skill；复用现有资料，保持状态、证据与文件入口易读。",
        "developerName": "Auhyuan",
        "category": "Productivity",
        "capabilities": [],
        "defaultPrompt": [
            "使用 P-SOP 接续当前项目的开发流程。",
            "仅使用 build-pp，根据现有资料更新项目进度看板。",
        ],
    },
}


def skill_files(root):
    yield root / "SKILL.md"
    for folder in ("agents", "references", "assets"):
        for path in sorted((root / folder).rglob("*")):
            if path.is_file() and not any(part.startswith(".") for part in path.relative_to(root).parts):
                yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="tmp/p-sop.zip", help="ZIP path inside this repository's tmp/")
    args = parser.parse_args()
    output = (PROJECT_ROOT / args.output).resolve()
    if not output.is_relative_to((PROJECT_ROOT / "tmp").resolve()) or output.suffix != ".zip":
        parser.error("output must be a .zip file inside the repository's tmp/ directory")

    entries = {}
    for root, name in ((SOP_ROOT, "p-sop"), (BOARD_ROOT, "build-pp")):
        if not (root / "SKILL.md").is_file():
            parser.error(f"missing skill entry: {root / 'SKILL.md'}")
        for source in skill_files(root):
            relative = source.relative_to(root).as_posix()
            data = source.read_bytes()
            if name == "p-sop" and relative == "SKILL.md":
                data = data.decode("utf-8").replace("../p-sop-build-pp/SKILL.md", "../build-pp/SKILL.md").encode("utf-8")
            elif name == "build-pp" and relative == "SKILL.md":
                text, count = re.subn(r"(?m)^name: p-sop-build-pp$", "name: build-pp", data.decode("utf-8"), count=1)
                if count != 1:
                    parser.error("dashboard skill name changed; check plugin packaging before release")
                data = text.encode("utf-8")
            elif name == "build-pp" and relative == "agents/openai.yaml":
                data = data.decode("utf-8").replace("$p-sop-build-pp", "$build-pp").encode("utf-8")
            entries[f"p-sop/skills/{name}/{relative}"] = data

    entries["p-sop/.codex-plugin/plugin.json"] = (json.dumps(MANIFEST, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for path, data in sorted(entries.items()):
            archive.writestr(path, data)
    print(f"Plugin archive: {output}")


if __name__ == "__main__":
    main()
