from contextlib import asynccontextmanager
import asyncio

from fastapi import FastAPI

from app.connection import db_con
from app.routers import users


async def connect_database():
    await db_con.connect()


async def close_database():
    await db_con.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with asyncio.TaskGroup() as tg:
        tg.create_task(connect_database())

    yield

    async with asyncio.TaskGroup() as tg:
        tg.create_task(close_database())


app = FastAPI(lifespan=lifespan)

app.include_router(users.router)