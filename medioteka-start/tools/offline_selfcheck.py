"""Проверка основной логики стандартной библиотекой, без установки пакетов."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from catalog import load_catalog, search_items, filter_by_category, validate_item, total_duration

items = load_catalog()
checks = [
    ("Каталог содержит 6 записей", len(items) == 6),
    ("Пустой поиск возвращает каталог", search_items(items, "") == items),
    ("Поиск без учёта регистра", len(search_items(items, "PYTHON")) == 1),
    ("Пробелы по краям запроса", len(search_items(items, "  Python  ")) == 1),
    ("Фильтр выбранной категории", [x["id"] for x in filter_by_category(items, "Разработка")] == [1, 2]),
    ("Отрицательная длительность отклоняется", bool(validate_item({"title":"Тест", "duration":-1}))),
    ("Суммарная длительность", total_duration(items) == 72),
    ("Пустое название отклоняется", bool(validate_item({"title":" ", "duration":1}))),
]
for name, ok in checks:
    print(("PASS " if ok else "FAIL ") + name)
print(f"Пройдено: {sum(ok for _, ok in checks)} из {len(checks)}")
sys.exit(0 if all(ok for _, ok in checks) else 1)
