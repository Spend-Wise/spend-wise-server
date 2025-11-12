from ..db.repository.user import get_user_by_name, save_user
from ..schemas.user import UserCredentials, UserInfo


class UserService:
    @staticmethod
    def create_user(body: UserCredentials) -> UserInfo:
        username = body.username
        password = body.password
        if username == "" or password == "":
            raise ValueError("username and password are required")

        user_info = save_user(body)

        return user_info

    @staticmethod
    def authenticate_user(body: UserCredentials) -> UserInfo | None:
        user = get_user_by_name(body.username)
        if not user:
            return None
        if user.password != body.password:
            return None

        return UserInfo(id=user.id, username=user.username)
