from fastapi import APIRouter, HTTPException, status

from ...schemas.expense import Expense
from ...services.expense_services import ExpenseServices
from .endpoints import auth

api_router = APIRouter()
api_router.include_router(auth.router)


@api_router.post("/expense", summary="Create a new expense")
async def create_expense(expense: Expense):
    try:
        return ExpenseServices.save_expense(expense)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
