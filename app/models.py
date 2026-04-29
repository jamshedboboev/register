from datetime import date
from pydantic import Field, BaseModel, EmailStr, SecretStr


class UserLogIn(BaseModel):
    #я сменил login на username потому что мне лень добавлять новый или менять старый на фронте
    username: str = Field(..., title="User Name", min_length=4, max_length=40)
    password: SecretStr = Field(..., title="User password", min_length=8, max_length=20)


class UserRegist(UserLogIn):
    #мне было лень добавлять surname поэтмоу я просто его убрал
    birthdate: date = Field(..., title="User birth date", examples=["2004.08.01"])
    email: EmailStr = Field(..., title="User email")