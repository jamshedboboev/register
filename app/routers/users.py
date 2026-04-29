from fastapi import APIRouter
from app.models import UserRegist , UserLogIn
from app.connection import db_con


router = APIRouter(tags=["Users"])


@router.get("/users")
async def get_user():
    query = """
    SELECT *
    FROM users
    """

    r = await db_con.execute(query)

    return r


# fix: Добавить роут для авторизации
@router.post("/users/register")
async def register_user(user: UserRegist):
    query = """
    SELECT *
    FROM users
    WHERE username = %s OR email = %s
    """
    r = await db_con.execute(query, (user.username, user.email))
    if r:
        return {"message": "User already exists"}

    query = """
    INSERT INTO users (username, email, password)
    VALUES (%s, %s, %s)
    """
    await db_con.execute(query, (user.username, user.email, user.password.get_secret_value()))
    return {"message": "User registered successfully"}

# fix: Добавить роут для авторизации
@router.post("/users/login")
async def login_user(user: UserLogIn):
    query = """
    SELECT *
    FROM users
    WHERE username = %s AND password = %s
    """
    r = await db_con.execute(query, (user.username, user.password))
    if r:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}

# fix: По возможности добавить дополнительные роуты для других задач