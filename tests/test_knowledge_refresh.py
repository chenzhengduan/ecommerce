import tempfile
import unittest
from pathlib import Path

from tools.knowledge_refresh import (
    classify_markdown_file,
    extract_headings,
    extract_title,
    scan_markdown_tree,
    write_inventory_csv,
    write_inventory_markdown,
)


class KnowledgeRefreshTests(unittest.TestCase):
    def test_extract_title_prefers_first_h1(self):
        text = "Intro\n\n# 亚马逊平台基础\n\n## 账号体系\n"

        self.assertEqual(extract_title(text, "fallback.md"), "亚马逊平台基础")

    def test_extract_title_uses_filename_when_h1_missing(self):
        self.assertEqual(extract_title("## 二级标题\n", "速卖通运营策略.md"), "速卖通运营策略")

    def test_extract_headings_returns_top_level_markdown_headings(self):
        text = "# 标题\n\n## 一\n\n### 二\n\n#### 三\n"

        self.assertEqual(extract_headings(text), ["# 标题", "## 一", "### 二"])

    def test_classify_daily_log(self):
        path = Path("cross-border-ecommerce/daily/2026-05-06.md")

        self.assertEqual(classify_markdown_file(path), "学习日志")

    def test_scan_markdown_tree_records_relative_paths_and_types(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            docs = root / "cross-border-ecommerce"
            (docs / "01-基础概念").mkdir(parents=True)
            (docs / "daily").mkdir()
            (docs / "01-基础概念" / "跨境电商基础概念.md").write_text(
                "# 跨境电商基础概念\n\n## 定义\n", encoding="utf-8"
            )
            (docs / "daily" / "2026-05-06.md").write_text(
                "# 每日学习\n", encoding="utf-8"
            )

            inventory = scan_markdown_tree(docs)

            paths = [item["path"] for item in inventory]
            self.assertEqual(
                paths,
                ["01-基础概念/跨境电商基础概念.md", "daily/2026-05-06.md"],
            )
            self.assertEqual(inventory[0]["file_type"], "正式主题笔记")
            self.assertEqual(inventory[1]["file_type"], "学习日志")

    def test_inventory_writers_support_custom_knowledge_base_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inventory = [
                {
                    "path": "01-平台基础/阿里巴巴电商体系总览.md",
                    "title": "阿里巴巴电商体系总览",
                    "headings": "# 阿里巴巴电商体系总览",
                    "topic_number": "01",
                    "category": "平台基础",
                    "file_type": "正式主题笔记",
                    "date_sensitive": "是",
                    "modified_date": "2026-05-26",
                }
            ]

            markdown_path = root / "alibaba-ecommerce" / "00-知识刷新" / "inventory.md"
            csv_path = root / "alibaba-ecommerce" / "00-知识刷新" / "inventory.csv"
            write_inventory_markdown(inventory, markdown_path)
            write_inventory_csv(inventory, csv_path)

            self.assertIn("阿里巴巴电商体系总览", markdown_path.read_text(encoding="utf-8"))
            self.assertIn("01-平台基础/阿里巴巴电商体系总览.md", csv_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
