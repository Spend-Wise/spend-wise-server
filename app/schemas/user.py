from pydantic import BaseModel


class UserCredentials(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: str
    username: str
    password: str

    class Config:
        orm_mode = True


class UserInfo(BaseModel):
    id: str
    username: str

    class Config:
        orm_mode = True
