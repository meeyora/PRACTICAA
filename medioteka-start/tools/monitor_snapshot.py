"""Моментальный снимок репозитория. Запуск из корня проекта."""
import json
import subprocess
import datetime
from pathlib import Path

root = Path(__file__).resolve().parents[1]
def git(*args):
    p = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8")
    return p.stdout.strip() if p.returncode == 0 else "Git не инициализирован или команда недоступна"
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
result = {"timestamp_utc":stamp, "commit":git("rev-parse", "HEAD"),
          "working_tree":git("status", "--short"),
          "python_files":len(list(root.glob("*.py"))) + len(list((root / "tests").glob("*.py"))),
          "readme_exists":(root / "README.md").exists(),
          "specification_exists":(root / "docs/specification.md").exists()}
target = root / "reports" / "block02" / f"snapshot-{stamp}.json"
target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(target.relative_to(root))
