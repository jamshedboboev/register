from fastapi import APIRouter

from app.core.connection import db_con

from app.models import UserRegist , UserLogIn
from app.auth.security import get_hashed_pass, check_hash_pass


router = APIRouter(tags=["Users"])


@router.get("/users")
async def get_user():
    query = """
    SELECT *
    FROM users
    """
    r = await db_con.execute(query)

    return r


@router.post("/users/register")
async def register_user(user: UserRegist):
    # fix: проверку на наличие совпадений в БД переместить в файл validate.py
    query = """
    SELECT id, login, email
    FROM users
    WHERE login = %s and email = %s
    """
    r = await db_con.execute(query, (user.login, user.email))
    if r:
        return {"message": "User already exists"}

    hashed_pass = get_hashed_pass(user.password.get_secret_value())

    # fix: добавление пользователя в БД переместить в файл связанный с update-ами
    query = """
    INSERT INTO users (login, password_hash, name, surname, birthdate, email)
    VALUES (%(login)s, %(password)s, %(name)s, %(surname)s, %(birthdate)s, %(email)s)
    """

    await db_con.execute(query, {
        "login": user.login,
        "password": hashed_pass,
        "name": user.name,
        "surname": user.surname,
        "birthdate": user.birthdate,
        "email": user.email
    })
    return {"message": "User registered successfully"}


@router.post("/users/login")
async def login_user(user: UserLogIn):
    query = """
    SELECT id, login, password_hash
    FROM users
    WHERE login = %s
    """

    r = await db_con.execute(query, (user.login,))

    # fix: Доработать данное условие и добавить логиврование и обработку ошибок
    if not r:
        raise Exception()
    
    password_check = check_hash_pass(user.password, r["password_hash"])  # type: ignore | Разобраться с типизацией

    if password_check:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}

# fix: По возможности добавить дополнительные роуты для других задач