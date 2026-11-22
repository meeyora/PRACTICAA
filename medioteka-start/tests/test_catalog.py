import pytest
from catalog import (load_catalog, search_items, filter_by_category,
                     total_duration, validate_item, duration_label)

@pytest.fixture
def items():
    return [
        {"id": 1, "title": "Python и тесты", "category": "Разработка", "duration": 60},
        {"id": 2, "title": "Защита данных", "category": "Безопасность", "duration": 120},
    ]

def test_dataset_has_six_records():
    assert len(load_catalog()) == 6

def test_empty_query_returns_all(items):
    assert search_items(items, "") == items

def test_search_exact(items):
    assert [x["id"] for x in search_items(items, "Python")] == [1]

def test_search_ignores_case(items):
    assert [x["id"] for x in search_items(items, "PYTHON")] == [1]

def test_search_trims_query(items):
    assert [x["id"] for x in search_items(items, "  Python  ")] == [1]

def test_missing_query_returns_empty(items):
    assert search_items(items, "несуществующий материал") == []

def test_category_matches_selected(items):
    assert [x["id"] for x in filter_by_category(items, "Разработка")] == [1]

def test_empty_category_returns_all(items):
    assert filter_by_category(items, "") == items

def test_duration_total(items):
    assert total_duration(items) == 180

def test_empty_duration_is_zero():
    assert total_duration([]) == 0

def test_valid_item_has_no_errors(items):
    assert validate_item(items[0]) == []

def test_negative_duration_is_invalid():
    assert validate_item({"title": "Тест", "duration": -1})

def test_blank_title_is_invalid():
    assert validate_item({"title": "   ", "duration": 10})

@pytest.mark.parametrize("seconds,label", [(0,"0 с"), (59,"59 с"), (60,"1 мин"),
    (61,"1 мин 1 с"), (3600,"1 ч"), (3660,"1 ч 1 мин"), (3661,"1 ч 1 мин 1 с")])
def test_duration_label(seconds, label):
    assert duration_label(seconds) == label
