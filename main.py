from flask import Flask, request
from dataRetriever import DataRetriever
import uvicorn
import asyncio
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
data=DataRetriever()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/api/v1/pokemons")
async def get_pokemons():
    pokemons=await data.fetch_pokemons() 
    return pokemons

@app.route("/api/v1/pokemons/params")
async def get_pokemons_by_query():
    name = request.args.get('name', '')
    typs = request.args.get('type', '')
    pokemons = await data.fetch_pokemons_by(typs, name) 
    return pokemons

if __name__ == '__main__': 
    asgi_app = WsgiToAsgi(app)
    uvicorn.run(asgi_app)