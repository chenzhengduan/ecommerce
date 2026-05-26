from __future__ import annotations

import argparse
import csv
import re
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, List


DATE_SENSITIVE_KEYWORDS = [
    "平台规则",
    "费用",
    "费率",
    "税",
    "VAT",
    "Sales Tax",
    "合规",
    "政策",
    "广告",
    "物流",
    "认证",
    "工具",
    "GDPR",
]


def extract_title(text: str, filename: str) -> str:
    for line in text.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return Path(filename).stem


def extract_headings(text: str, limit: int = 8) -> List[str]:
    headings: List[str] = []
    for line in text.splitlines():
        if re.match(r"^#{1,3}\s+\S", line):
            headings.append(line.strip())
        if len(headings) >= limit:
            break
    return headings


def classify_markdown_file(path: Path) -> str:
    parts = set(path.parts)
    name = path.name.lower()
    if "daily" in parts:
        return "学习日志"
    if name in {"index.md", "overview.md", "progress.md"} or "总览" in path.name or "进度" in path.name:
        return "总览/进度文件"
    if "git" in parts or "notes" in parts:
        return "辅助文件"
    return "正式主题笔记"


def detect_topic_number(relative_path: Path) -> str:
    first = relative_path.parts[0] if relative_path.parts else relative_path.name
    match = re.match(r"^(\d+)", first)
    return match.group(1) if match else ""


def detect_category(relative_path: Path) -> str:
    first = relative_path.parts[0] if relative_path.parts else ""
    if "-" in first:
        return first.split("-", 1)[1]
    return first


def has_date_sensitive_content(text: str) -> bool:
    return any(keyword.lower() in text.lower() for keyword in DATE_SENSITIVE_KEYWORDS)


def scan_markdown_tree(docs_dir: Path) -> List[Dict[str, str]]:
    inventory: List[Dict[str, str]] = []
    for path in sorted(docs_dir.rglob("*.md"), key=lambda item: item.relative_to(docs_dir).as_posix()):
        relative = path.relative_to(docs_dir)
        text = path.read_text(encoding="utf-8")
        stat = path.stat()
        inventory.append(
            {
                "path": relative.as_posix(),
                "title": extract_title(text, path.name),
                "headings": " | ".join(extract_headings(text)),
                "topic_number": detect_topic_number(relative),
                "category": detect_category(relative),
                "file_type": classify_markdown_file(relative),
                "date_sensitive": "是" if has_date_sensitive_content(text) else "否",
                "modified_date": date.fromtimestamp(stat.st_mtime).isoformat(),
            }
        )
    return inventory


def write_inventory_markdown(inventory: Iterable[Dict[str, str]], output_path: Path) -> None:
    rows = list(inventory)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# 知识清单 - {date.today().isoformat()}",
        "",
        f"- 扫描文件数：{len(rows)}",
        "",
        "| 路径 | 标题 | 类型 | 分类 | 时效性 |",
        "|---|---|---|---|---|",
    ]
    for item in rows:
        lines.append(
            f"| `{item['path']}` | {item['title']} | {item['file_type']} | {item['category']} | {item['date_sensitive']} |"
        )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_inventory_csv(inventory: Iterable[Dict[str, str]], output_path: Path) -> None:
    rows = list(inventory)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "path",
                "title",
                "headings",
                "topic_number",
                "category",
                "file_type",
                "date_sensitive",
                "modified_date",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="生成 Markdown 知识库清单")
    parser.add_argument("--docs-dir", default="cross-border-ecommerce")
    parser.add_argument("--out-dir", default="cross-border-ecommerce/00-知识刷新/inventory")
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir)
    out_dir = Path(args.out_dir)
    today = date.today().isoformat()
    inventory = scan_markdown_tree(docs_dir)
    write_inventory_markdown(inventory, out_dir / f"{today}-inventory.md")
    write_inventory_csv(inventory, out_dir / f"{today}-inventory.csv")
    print(f"scanned={len(inventory)}")
    print(f"markdown={out_dir / f'{today}-inventory.md'}")
    print(f"csv={out_dir / f'{today}-inventory.csv'}")


if __name__ == "__main__":
    main()
