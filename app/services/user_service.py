from ..db.repository.user import get_user_by_name, save_user
from ..exceptions.auth_exceptions import InvalidPasswordError, UsernameAlreadyExistsError
from ..exceptions.spend_wise_exceptions import UserNotFoundError
from ..schemas.user import UserCredentials, UserInfo


class UserService:
    @staticmethod
    def create_user(credentials: UserCredentials) -> UserInfo:
        username = credentials.username.strip()
        password = credentials.password
        if username == "" or password == "":
            raise ValueError("username and password are required")

        existing_user = get_user_by_name(username)
        if existing_user:
            raise UsernameAlreadyExistsError(username)

        user_info = save_user(credentials)

        return user_info

    @staticmethod
    def authenticate_user(credentials: UserCredentials) -> UserInfo | None:
        user = get_user_by_name(credentials.username)
        if not user:
            raise UserNotFoundError(f"No user found with username: {credentials.username}")
        if user.password != credentials.password:
            raise InvalidPasswordError(user.password)

        return UserInfo(id=user.id, username=user.username)
