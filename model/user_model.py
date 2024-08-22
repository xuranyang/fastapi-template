from pydantic import BaseModel


class LoginModel(BaseModel):
    username: str = 'admin'
    password: str = '123456'
