from ..db.repository.user import get_user_by_name, save_user
from ..schemas.user import UserCredentials, UserInfo


class UserService:
    @staticmethod
    def create_user(credentials: UserCredentials) -> UserInfo:
        username = credentials.username.strip()
        password = credentials.password
        if username == "" or password == "":
            raise ValueError("username and password are required")

        user_info = save_user(credentials)

        return user_info

    @staticmethod
    def authenticate_user(credentials: UserCredentials) -> UserInfo | None:
        user = get_user_by_name(credentials.username)
        if not user:
            return None
        if user.password != credentials.password:
            return None

        return UserInfo(id=user.id, username=user.username)
