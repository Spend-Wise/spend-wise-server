import pytest

from unittest.mock import patch, MagicMock
from app.exceptions.auth_exceptions import UsernameAlreadyExistsError, InvalidPasswordError
from app.exceptions.spend_wise_exceptions import UserNotFoundError
from app.services.user_service import UserService
from app.schemas.user import UserCredentials, UserInfo, UserData

@pytest.fixture
def user_service():
    return UserService()

def test_create_user_success(user_service):
    with patch('app.services.user_service.save_user') as mock_save_user:
        mock_save_user.return_value = UserInfo(id='1', username='testuser')
        user_credentials = UserCredentials(username='testuser', password='password')
        user_info = user_service.create_user(user_credentials)
        assert user_info.id == '1'
        assert user_info.username == 'testuser'
        mock_save_user.assert_called_once_with(user_credentials)

def test_create_user_empty_credentials(user_service):
    with pytest.raises(ValueError, match="username and password are required"):
        user_service.create_user(UserCredentials(username='', password=''))

def test_create_user_username_exists(user_service):
    with patch('app.services.user_service.get_user_by_name') as mock_get_user_by_name:
        mock_get_user_by_name.return_value = UserData(id='1', username='testuser', password='password')
        user_credentials = UserCredentials(username='testuser', password='password')
        with pytest.raises(UsernameAlreadyExistsError, match="Username already exists. Please choose a different username."):
            user_service.create_user(user_credentials)
        mock_get_user_by_name.assert_called_once_with('testuser')

def test_authenticate_user_success(user_service):
    with patch('app.services.user_service.get_user_by_name') as mock_get_user_by_name:
        mock_user = UserData(id='1', username='testuser', password='password')
        mock_get_user_by_name.return_value = mock_user
        user_credentials = UserCredentials(username='testuser', password='password')
        user_info = user_service.authenticate_user(user_credentials)
        assert user_info.id == '1'
        assert user_info.username == 'testuser'
        mock_get_user_by_name.assert_called_once_with('testuser')

def test_authenticate_user_not_found(user_service):
    with patch('app.services.user_service.get_user_by_name') as mock_get_user_by_name:
        mock_get_user_by_name.return_value = None
        user_credentials = UserCredentials(username='testuser', password='password')
        with pytest.raises(UserNotFoundError, match="User with provided username is not found"):
            user_service.authenticate_user(user_credentials)
        mock_get_user_by_name.assert_called_once_with('testuser')

def test_authenticate_user_wrong_password(user_service):
    with patch('app.services.user_service.get_user_by_name') as mock_get_user_by_name:
        mock_user = UserData(id='1', username='testuser', password='password')
        mock_get_user_by_name.return_value = mock_user
        user_credentials = UserCredentials(username='testuser', password='wrongpassword')
        with pytest.raises(InvalidPasswordError, match="Password did not match"):
            user_service.authenticate_user(user_credentials)
        mock_get_user_by_name.assert_called_once_with('testuser')
