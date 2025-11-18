import uuid

from ...schemas.user import UserCredentials, UserData, UserInfo

users: list[UserData] = []


def save_user(user_create: UserCredentials) -> UserInfo:
    user = UserData(
        id=str(uuid.uuid4()), username=user_create.username, password=user_create.password
    )
    users.append(user)
    return UserInfo(id=user.id, username=user.username)


def get_user_by_id(user_id: str) -> UserData | None:
    for user in users:
        if user.id == user_id:
            return user
    return None


def get_user_by_name(username: str) -> UserData | None:
    for user in users:
        if user.username == username:
            return user
    return None
