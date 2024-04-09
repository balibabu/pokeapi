from pokemon_api import Pokemonapi
from db_management import DBManagement
import configparser

class DataRetriever:

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.table='pokemon5'
    
    async def get_db_instance(self):
        obj=DBManagement()
        await obj.create_connection(self.config['database']['user'],self.config['database']['password'],self.config['database']['database'],self.config['database']['host'])
        return obj

    async def fetch_from_api(self):
        pokemons= Pokemonapi.fetch_pokemons_range(0,5)
        await self.save_to_db(pokemons)
        return pokemons

    async def fetch_from_db(self):
        obj=await self.get_db_instance()
        rows=await obj.fetch_rows(self.table)
        pokemons=[{"name":row['name'],"type":row['type'],"image":row['image']} for row in rows]
        return pokemons

    async def save_to_db(self,pokemons):
        obj=await self.get_db_instance()
        await obj.create_table(self.table)
        for pokemon in pokemons:
            await obj.insert_row(self.table,pokemon)
        await obj.close_connection()

    async def fetch_pokemons(self):
        self.pokemons=await self.fetch_from_db()
        if not self.pokemons:
            self.pokemons=await self.fetch_from_api()
        return self.pokemons

    async def fetch_pokemons_by(self,typ='',name=''):
        pokemons=[]
        try:
            obj=await self.get_db_instance()
            rows=await obj.fetch_filtered_rows(self.table,typ,name)
            pokemons=[{"name":row['name'],"type":row['type'],"image":row['image']} for row in rows]
            if not pokemons:
                uf_pokemons=self.fetch_from_api()
                for pokemon in uf_pokemons:
                    if name==pokemon['name'] or typ==pokemon['type']:
                        pokemons.append(pokemon)
        except Exception as e:
            print(e)
        return pokemons

        