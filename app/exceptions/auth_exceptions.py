from app.exceptions.spend_wise_exceptions import SpendWiseError


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

    def __init__(
        self, username, message="Username already exists. Please choose a different username."
    ):
        self.username = username
        self.message = message
        super().__init__(message)

    def to_detail(self):
        return {"error": self.name, "message": self.message, "username": self.username}


class InvalidPasswordError(AuthError):
    """Exception raised when the provided password is invalid.

    Attributes:
        message -- explanation of the error (optional)
    """

    def __init__(self, password, message="Password did not match"):
        self.password = password
        self.message = message
        super().__init__(message)

    def to_detail(self):
        return {"error": self.name, "message": self.message, "password": self.password}
