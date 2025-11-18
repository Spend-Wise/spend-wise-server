class SpendWiseError(Exception):
    """Base class for all exceptions in this application."""

    @property
    def name(self):
        return self.__class__.__name__

    def to_detail(self):
        return {"error": self.name, "message": self.message}

    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(message)


class UserNotFoundError(SpendWiseError):
    """Exception raised for errors in the input user ID.

    Attributes:
        user_id -- input user ID which caused the error
        message -- explanation of the error (optional)
    """

    def __init__(self, user_id, message=None):
        self.user_id = user_id
        if message is None:
            message = f"User with id {user_id} not found"
        super().__init__(message)


class AuthError(SpendWiseError):
    """Base class for auth-related exceptions in this module."""

    def __init__(self, message="Authentication error occurred"):
        super().__init__(message)


class UsernameAlreadyExistsError(AuthError):
    """Exception raised when trying to create a user with a username that already exists.

    Attributes:
        username -- input username which caused the error
        message -- explanation of the error (optional)
    """

    def __init__(self, username, message=None):
        self.username = username
        if message is None:
            message = f"Username '{username}' already exists. Please choose a different username."

        super().__init__(message)
