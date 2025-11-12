from fastapi import APIRouter, HTTPException, status

from ....schemas.user import UserCredentials, UserInfo
from ....services.user_service import UserService

router = APIRouter()


@router.post("/domain/auth/signup", response_model=UserInfo, status_code=status.HTTP_201_CREATED)
async def signup(credentials: UserCredentials) -> UserInfo:
    """Register a new user."""
    try:
        return UserService.create_user(credentials)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/domain/auth/login", response_model=UserInfo)
async def login(credentials: UserCredentials) -> UserInfo:
    """Authenticate a user and return user info."""
    user_info = UserService.authenticate_user(credentials)
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password"
        )
    return user_info
