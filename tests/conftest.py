from unittest.mock import MagicMock
import pytest
import uuid
from app.schemas.expense import Expense

@pytest.fixture
def expense_repository_mock(monkeypatch):
    """Fixture that patches the expense repository's save_expense.

    Tests must include `expense_repository_mock` in their parameters to use it.
    Returns a MagicMock so tests can set return_value or side_effect.
    """
    from app.db.repository import expense
    mock = MagicMock(name="save_expense")

    mock.side_effect = lambda expense_data: {**expense_data.model_dump(), id: "1"}
    mock.return_value = None
    monkeypatch.setattr(expense, "save_expense", mock)
    return mock

@pytest.fixture
def user_repository_mock(monkeypatch):
    """Fixture that patches the user repository's get_user_by_id.

    Tests must include `user_repository_mock` in their parameters to use it.
    Returns a MagicMock so tests can set return_value or side_effect.
    """
    from app.db.repository import user
    mock = MagicMock(name="get_user_by_id")

    mock.side_effect = lambda user_id: {
        "id": str(user_id),
        "username": "testuser",
        "password": "hashedpassword"
    }

    mock.return_value = None

    monkeypatch.setattr(user, "get_user_by_id", mock)
    return mock

@pytest.fixture
def expense_factory():
    """Factory fixture to build Expense objects with sensible defaults.
    Override any field via keyword arguments.
    """
    def _factory(**overrides):
        base = {
            "amount": 100.0,
            "description": "Test expense",
            "user_id": uuid.UUID("123e4567-e89b-12d3-a456-426614174000"),
            "date": "01-06-2024",
        }
        base.update(overrides)
        return Expense(**base)
    return _factory
