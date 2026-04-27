from datetime import date

from fastapi import FastAPI
from pydantic import SecretStr

from app.models import UserRegist


app = FastAPI()

@app.get("/")
async def get_user():
    return UserRegist(
        name="Ясин",
        surname="Фамилия",
        birthdate=date(year=2006, day=1, month=1),
        email="YasinSamuray@mail.com",
        login="Yasin123",
        password=SecretStr("EasyPass123")
    )