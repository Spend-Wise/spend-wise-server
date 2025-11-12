from pydantic import BaseModel, ConfigDict


class UserCredentials(BaseModel):
    username: str
    password: str


class UserData(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    username: str
    password: str


class UserInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    username: str
