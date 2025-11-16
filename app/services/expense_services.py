from datetime import datetime

from app.db.repository import expense, user
from app.exceptions import UserNotFoundError
from app.schemas.expense import Expense


class ExpenseServices:
    @staticmethod
    def save_expense(expense_data: Expense) -> Expense:
        if expense_data.amount <= 0:
            raise ValueError("Invalid expense value, should be greater than zero")

        try:
            datetime.strptime(expense_data.date, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Invalid date format, should be DD-MM-YYYY")

        user_in_db = user.get_user_by_id(str(expense_data.user_id))
        if not user_in_db:
            raise UserNotFoundError(expense_data.user_id)

        return expense.save_expense(expense_data)
