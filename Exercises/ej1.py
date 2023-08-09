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

            for pokemonName, probability in reader:
                data.append({'Pokeball': pokeball, 'Pokemon': pokemonName, 'Probability': float(probability)})

    df = pd.DataFrame(data)
    fig = px.bar(df, x='Pokeball', y='Probability', color='Pokemon', barmode='group')
    fig.show()

