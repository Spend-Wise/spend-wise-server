class ExpenseError(Exception):
    """Base class for exceptions in this module."""

    pass


class UserNotFoundError(Exception):
    """Exception raised for errors in the input user ID.

    Attributes:
        user_id -- input user ID which caused the error
        message -- explanation of the error
    """

    def __init__(self, user_id, message="User with id {user_id} not found"):
        self.user_id = user_id
        self.message = message.format(user_id=user_id)
        super().__init__(self.message)
