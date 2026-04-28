from fastapi import APIRouter

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