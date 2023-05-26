from fastapi import FastAPI
from pydantic import BaseMode1

app=FastAPI()

@app.get("/")
def index(): 
        return "Hola :)"

@app.get("/Pokemon/{num}")
def pokemon(num):
        pokemons={
        "1":"Bulbasur",
        "2":"Ivysaur",
        "3":"Venasur",
        "4":"Charmander",
        
       }
    return pokemons{num}


