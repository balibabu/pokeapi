import requests

class Pokemonapi:

    @staticmethod
    def fetch_pokemons():
        try:
            response = requests.get('https://pokeapi.co/api/v1/pokemon/')
            response.raise_for_status()
            data = response.json()
            pokemons = [(pokemon['name'],pokemon['url']) for pokemon in data['results']]
            names=[]
            types=[]
            imgs=[]
            for name,url in pokemons:
                names.append(name)
                nested_res=requests.get(url)
                nested_res.raise_for_status()
                nested_data=nested_res.json()
                imgs.append(nested_data['sprites']['other']['home']['front_default'])
                types.append(nested_data['types'][0]['type']['name'])
            pokemons=[{"name":name,"type":typs,"image":img} for name,typs,img in zip(names,types,imgs)]
            return pokemons
        except requests.exceptions.RequestException as e:
            return {"error": "Failed to fetch Pokémon data from PokeAPI"}
        
    @staticmethod
    def fetch_pokemons_range(start=0,limit=10):
        pokemons=[]
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon?offset={start}&limit={limit}')
        if response.status_code==200:
            data = response.json()
            nameAndUrls=[(pokemon['name'],pokemon['url']) for pokemon in data['results']]
            for name,url in nameAndUrls:
                res2=requests.get(url)
                if res2.status_code==200:
                    pokDetails=res2.json()
                    image=pokDetails['sprites']['other']['home']['front_default']
                    typs=[li['type']['name'] for li in pokDetails['types']]
                    pokemons.append({'name':name,'image':image,'type':','.join(typs)})
        return pokemons

            

    