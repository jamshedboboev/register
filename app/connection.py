import psycopg

from app.config import settings


class Database:
    def __init__(self) -> None:
        self.conn = None

    async def connect(self):
        self.conn = await psycopg.AsyncConnection.connect(
            dbname=settings.db_name,
            user=settings.db_user,
            password=settings.db_password,
            host=settings.db_host,
            port=settings.db_port,
            sslmode="require",
        )

    async def close(self):
        if self.conn is not None:
            await self.conn.close()

    async def execute(self, query, params=None):
        async with self.conn.cursor() as cur:  # type: ignore
            await cur.execute(query, params)

            # если запрос возвращает данные (SELECT или RETURNING)
            if cur.description:
                rows = await cur.fetchall()

                # если одна строка — вернуть одну
                if len(rows) == 1:
                    return rows[0]

                return rows

            # если это INSERT/UPDATE/DELETE
            await self.conn.commit()  # type: ignore
            return None


db_con = Database()