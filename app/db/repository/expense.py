from app.schemas.expense import Expense

expenses: list[Expense] = []


def save_expense(expense_data: Expense) -> Expense:
    expense_id = str(len(expenses) + 1)
    expense_data.id = expense_id
    expenses.append(expense_data)
    return expense_data
