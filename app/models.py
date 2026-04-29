from datetime import date
from pydantic import Field, BaseModel, EmailStr, SecretStr


class UserLogIn(BaseModel):
    login: str = Field(..., title="User login", min_length=4, max_length=40)
    password: SecretStr = Field(..., title="User password", min_length=8, max_length=20)


class UserRegist(UserLogIn):
    name: str = Field(..., title="User name", min_length=1, max_length=40)
    surname: str = Field(..., title="User surname", min_length=1, max_length=40)
    birthdate: date = Field(..., title="User birth date", examples=["2004-08-01"])
    email: EmailStr = Field(..., title="User email")