from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    ################# USERS TABLE ####################

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE 
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    ################# CHANNELS TABLE ####################

    async def create_table_socials(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Socials (
        id SERIAL PRIMARY KEY,
        
        -- Ijtimoiy kategoriyasi
        category_code VARCHAR(20) NOT NULL,
        category_name VARCHAR(50) NOT NULL,
        
        -- Ijtimoiy haqida malumot
        name VARCHAR(50) NOT NULL,
        link varchar(255) NULL,
        description VARCHAR(3000) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_product(
        self,
        category_code,
        category_name,
        name,
        link,
        description="",
    ):
        sql = "INSERT INTO Socials (category_code, category_name, name, link, description) VALUES($1, $2, $3, $4, $5) returning *"
        return await self.execute(
            sql,
            category_code,
            category_name,
            name,
            link,
            description,
            fetchrow=True,
        )

    async def get_categories(self):
        sql = "SELECT DISTINCT category_name, category_code FROM Socials"
        return await self.execute(sql, fetch=True)

    async def count_socials(self, category_code):
        sql = f"SELECT COUNT(*) FROM Socials WHERE category_code='{category_code}'"
        return await self.execute(sql, fetchval=True)

    async def get_socials(self, category_code):
        sql = f"SELECT * FROM Socials WHERE category_code='{category_code}'"
        return await self.execute(sql, fetch=True)

    async def get_product(self, product_id):
        sql = f"SELECT * FROM Socials WHERE id={product_id}"
        return await self.execute(sql, fetchrow=True)

    async def delete_product(self, product_id):
        sql = f"DELETE FROM Socials WHERE id={product_id}"
        return await self.execute(sql, fetchrow=True)

    async def drop_socials(self):
        await self.execute("DROP TABLE Socials", execute=True)

    ################# USERS TABLE ####################

    async def create_table_offers(self):
        sql = """
        CREATE TABLE IF NOT EXISTS offers (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        offer varchar(255) NULL,
        offerer TEXT NOT NULL 
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_offer(self, title, offer, offerer):
        sql = (
            "INSERT INTO offers (title, offer, offerer) VALUES($1, $2, $3) returning *"
        )
        return await self.execute(sql, title, offer, offerer, fetchrow=True)

    async def select_all_offers(self):
        sql = "SELECT * FROM offers"
        return await self.execute(sql, fetch=True)

    async def select_offer(self, **kwargs):
        sql = "SELECT * FROM offers WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_offers(self):
        sql = "SELECT COUNT(*) FROM offers"
        return await self.execute(sql, fetchval=True)

    async def delete_offers(self):
        await self.execute("DELETE FROM offers WHERE TRUE", execute=True)

    async def drop_offers(self):
        await self.execute("DROP TABLE offers", execute=True)
