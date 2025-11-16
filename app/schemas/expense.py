from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Expense(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str | None = None  # optional, assigned by repository
    amount: float
    description: str
    user_id: UUID
    date: str
