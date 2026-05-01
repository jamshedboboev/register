import psycopg
from psycopg.rows import dict_row

from app.core.config import settings

# fix: Попробовать перелопатить данный класс и сделать правильный "connection"

class Database:
    async def connect(self):
        self.conn = await psycopg.AsyncConnection.connect(
            dbname=settings.db.db_name,
            user=settings.db.db_user,
            password=settings.db.db_password,
            host=settings.db.db_host,
            port=settings.db.db_port,
            sslmode="require",
            row_factory=dict_row  # type: ignore
        )

    async def close(self):
        if self.conn is not None:
            await self.conn.close()

    async def execute(self, query, params=None):
        async with self.conn.cursor() as cur:
            await cur.execute(query, params)

            # если запрос возвращает данные (SELECT или RETURNING)
            if cur.description:
                rows = await cur.fetchall()

                # если одна строка — вернуть одну
                if len(rows) == 1:
                    return rows[0]

                return rows

            # если это INSERT/UPDATE/DELETE
            await self.conn.commit()


db_con = Database()