import json
import os
import csv
import pandas as pd
import plotly.express as px
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect, Pokemon

ITERATIONS = 10000


def ex1(configFileName):
    factory = PokemonFactory("pokemon.json")
    with open(configFileName, "r") as f:
        config = json.load(f)
        pokemons: list[Pokemon] = []
        for item in config:
            pokemon = factory.create(item["pokemon"], item["level"], StatusEffect.NONE, item["hp"])
            pokemons.append(pokemon)

    pokeballs = ["pokeball", "ultraball", "fastball", "heavyball"]

    for ball in pokeballs:
        with open(f"Results/Ex1/{ball}-data.csv", "w") as f:
            for pokemon in pokemons:
                catches = 0
                for _ in range(ITERATIONS):
                    catched, probability = attempt_catch(pokemon, ball)
                    if catched:
                        catches += 1
                print(f"{pokemon.name},{catches / ITERATIONS}", file=f)

def graph_ex1():
    data = []

    for name in os.listdir("./Results/Ex1/"):
        pokeball = name.split("-")[0]

        with open(f"./Results/Ex1/{pokeball}-data.csv", "r") as pokeball_file:
            reader = csv.reader(pokeball_file)

            average = 0
            AMOUNT_OF_POKEMONS = 5

            for pokemonName, probability in reader:
                data.append({'Pokeball': pokeball, 'Pokemon': pokemonName, 'Probability': float(probability)})
                average += float(probability)

            average /= AMOUNT_OF_POKEMONS
            data.append({'Pokeball': pokeball, 'Pokemon': 'Average', 'Probability': average})

    df = pd.DataFrame(data)
    fig = px.bar(df, x='Pokeball', y='Probability', color='Pokemon', barmode='group', title='Catch probability by pokeball')
    fig.update_layout(yaxis_range=[0,1])
    fig.show()

def graph_ex1b():


    pokemonData = {}
    for name in os.listdir("./Results/Ex1/"):
       pokeball = name.split("-")[0]
       pokemonData[pokeball] = {}
       with open(f"./Results/Ex1/{pokeball}-data.csv", "r") as pokeball_file:
           reader = csv.reader(pokeball_file)
           for pokemonName, probability in reader:
               pokemonData[pokeball][pokemonName] = float(probability)
    
    
   
    normalPokeball = pokemonData.pop("pokeball")
    for pokeballName in pokemonData.keys():
        currentBall : dict = pokemonData[pokeballName]
        for name in currentBall.keys():
            currentBall[name] /= normalPokeball[name]
    

    graphData = []
    for pokeballData in pokemonData.keys():
        currentBallPokemonData : dict = pokemonData[pokeballData]
        for pokemon in currentBallPokemonData.keys():
            graphData.append({"Pokemon": pokemon, "Pokeball": pokeballData,"captureRate": currentBallPokemonData[pokemon]})
    
    df = pd.DataFrame(graphData)
    fig = px.bar(df,x="Pokemon",y="captureRate", labels= { "Pokemon" : "Pokemon", "captureRate" : "Capture Effectiveness"} ,color="Pokeball", barmode="group",title="Capture Effectiveness for each Pokeball as proportion of standard Pokeball")
    fig.show()

               



