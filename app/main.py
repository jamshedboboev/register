from contextlib import asynccontextmanager
import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.connection import db_con
from app.routers import users

# fix: В целом разобраться как можно строить асинхронные main файлы
# fix: Добавить JWT токены для авторизации

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)