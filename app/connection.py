import psycopg


class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    async def connect(self):
        self.conn = await psycopg.AsyncConnection.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
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


db_con = Database(
    dbname="neondb",
    user="neondb_owner",
    password="npg_vPM6qDx5RfIO",
    host="ep-plain-king-aorf7r0j-pooler.c-2.ap-southeast-1.aws.neon.tech",
    port=5432,
)