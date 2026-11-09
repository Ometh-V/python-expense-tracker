from project import validate, get_date
from datetime import datetime

expenses = [
    ["2025-01-31", "miscellaneous", 500.0],
    ["2025-01-31", "food", 500.0],
    ["2025-01-31", "miscellaneous", 10000.0],
]


def test_vali_dates():
    date = "2025-01-31"
    assert validate(date, 0, expenses) == True
    assert validate("2025-01-30", 0, expenses) == False
    assert validate("cat", 0, expenses) == False


def test_vali_cat():
    assert validate("misc", 1, expenses) == True
    assert validate("FOOD", 1, expenses) == True
    assert validate("other", 1, expenses) == False


def test_get_date_today(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")
    result = get_date()
    assert result == datetime.today().strftime("%Y-%m-%d")


def test_get_date_valid_date(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2025-01-31")
    result = get_date()
    assert result == "2025-01-31"


def test_get_date_invalid_date_then_valid(monkeypatch):
    def mock_input(prompt):
        if not hasattr(mock_input, "counter"):
            mock_input.counter = 0
        mock_input.counter += 1
        if mock_input.counter == 1:
            return "2025-31-01"  # Invalid date
        return "2025-01-31"  # Valid date

    monkeypatch.setattr("builtins.input", mock_input)
    result = get_date()
    assert result == "2025-01-31"
