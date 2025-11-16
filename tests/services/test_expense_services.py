import pytest

from app.exceptions import UserNotFoundError
from app.services.expense_services import ExpenseServices


def test_successful_save(expense_factory, expense_repository_mock, user_repository_mock):
    expense_data = expense_factory()
    saved_expense = ExpenseServices.save_expense(expense_data)
    expense_repository_mock.assert_called_once_with(expense_data)
    assert saved_expense == {**expense_data.model_dump(), id: "1"}


def test_save_expense_exception(expense_factory, expense_repository_mock, user_repository_mock):
    expense_data = expense_factory()
    expense_repository_mock.side_effect = Exception("DB Error")
    with pytest.raises(Exception) as exc:
        ExpenseServices.save_expense(expense_data)
    expense_repository_mock.assert_called_once_with(expense_data)
    assert str(exc.value) == "DB Error"


def test_save_expense_invalid_amount(expense_factory, expense_repository_mock, user_repository_mock):
    expense_data = expense_factory(amount=0.0)
    with pytest.raises(ValueError) as exc:
        ExpenseServices.save_expense(expense_data)
    expense_repository_mock.assert_not_called()
    assert str(exc.value) == "Invalid expense value, should be greater than zero"


def test_save_expense_with_invalid_date(expense_factory, expense_repository_mock, user_repository_mock):
    expense_data = expense_factory(date="2001-04-22")
    with pytest.raises(ValueError) as exc:
        ExpenseServices.save_expense(expense_data)
    expense_repository_mock.assert_not_called()
    assert str(exc.value) == "Invalid date format, should be DD-MM-YYYY"


def test_save_expense_with_invalid_user_id(expense_factory, expense_repository_mock, user_repository_mock):
    invalid_user_id = "00000000-0000-0000-0000-000000000000"
    expense_data = expense_factory(user_id= invalid_user_id)
    user_repository_mock.side_effect = None
    with pytest.raises(UserNotFoundError) as exc:
        ExpenseServices.save_expense(expense_data)
    assert exc.type == UserNotFoundError
    assert str(exc.value) == f"User with id {expense_data.user_id} not found"
    expense_repository_mock.assert_not_called()
