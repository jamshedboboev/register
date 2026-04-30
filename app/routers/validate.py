import bcrypt
from app.core.connection import db_con

async def check_user(login : str , email : str):
    query = """
    SELECT id, login, email
    FROM users
    WHERE login = %s AND email = %s
    """
    r = await db_con.execute(query, (login, email))
    if r:
        return True
    return False

def check_password(hashed_pass: str , password: str) -> bool:
    password_check: bool = bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_pass.encode("utf-8")
    )
    return password_check