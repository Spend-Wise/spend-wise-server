import uuid

from ..schema import UserCreate, UserRead

users = []


def save_user(user_create: UserCreate) -> UserRead:
    user = UserRead(
        id=str(uuid.uuid4()), username=user_create.username, password=user_create.password
    )
    users.append(user)
    return user


def get_user_by_id(user_id: str) -> UserRead | None:
    for user in users:
        if user["id"] == user_id:
            return user
    return None


def get_user_by_name(username: str) -> UserRead | None:
    for user in users:
        if user["username"] == username:
            return user
    return None
