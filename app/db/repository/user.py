import uuid
from ..schema import userCreate, userRead

users = [];

def save_user(userCreate: userCreate) -> userRead:
    user_id = str(uuid.uuid4())
    user_data = userCreate.dict()
    user_data.update({"id": user_id})
    users.append(user_data)
    return user_data
    
def get_user_by_id(user_id: str) -> userRead | None:
    for user in users:
        if user["id"] == user_id:
            return user
    return None;

def get_user_by_name(username: str) -> userRead | None:
    for user in users:
        if user["username"] == username:
            return user
    return None;