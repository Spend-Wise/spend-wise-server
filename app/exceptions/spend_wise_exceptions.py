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

    def __init__(self, user_id, message="User with provided username is not found"):
        self.user_id = user_id
        super().__init__(message)

    def to_detail(self):
        return {"error": self.name, "message": self.message, "user_id": self.user_id}
