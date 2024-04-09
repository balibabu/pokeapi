import asyncpg

class DBManagement:

    def __init__(self) -> None:
        pass

    async def create_connection(self,user,password,database,host):
        try:
            self.connection = await asyncpg.connect(user=user,password=password,database=database,host=host)
            return not self.connection.is_closed()
        except Exception as e:
            print(e)
            return False

    async def create_table(self,tablename):
        try:
            await self.connection.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {tablename} (
                    id serial PRIMARY KEY,
                    name VARCHAR(50) UNIQUE,
                    image TEXT,
                    type TEXT
                )
                """
            )
            return True
        except Exception as e:
            print(e)
            return False
    
    async def insert_row(self,table,pokemon):
        try:
            await self.connection.execute(
                    f"""
                    INSERT INTO {table} (name, image, type)
                    VALUES ($1, $2, $3)
                    """,
                    f"{pokemon['name']}",
                    f"{pokemon['image']}",
                    f"{pokemon['type']}"
                )
            return True
        except Exception as e:
            print(e)
            return False
    
    async def fetch_rows(self,tablename):
        try:
            records = await self.connection.fetch(f"SELECT * FROM {tablename}")
            return records
        except Exception as e:
            print(e)
            return []
        
    async def fetch_filtered_rows(self,tablename,type,name):
        try:
            records = await self.connection.fetch(f"SELECT * FROM {tablename} where type like '%{type}%' or name='{name}'")
            return records
        except Exception as e:
            print(e)
            return []
        
    async def close_connection(self):
        await self.connection.close()