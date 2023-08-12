import csv
import os
import pandas as pd
import plotly.express as px
import plotly
from src.pokemon import *
from src.catching import attempt_catch

ITERATIONS = 10000
MINLEVEL = 1
MAXLEVEL = 100


def ex2c(configFileName):
    with open(configFileName, "r") as fp:
        pokemons = json.load(fp)

    # the dictionary pokemonObjs will have the pokemon names as keys
    # each key (pokemon name) will have as value an array of newly created pokemons with different levels and 100% health
    pokemonObjs = {}

    pokeballs = ["pokeball", "ultraball", "fastball", "heavyball"]

    factory = PokemonFactory()

    # fills pokemonObjs with intended values
    for pokemon in pokemons:
        pokemonObjs[pokemon["pokemon"]] = []
        for level in range(MINLEVEL, MAXLEVEL+1):
            pokemonObjs[pokemon["pokemon"]].append(factory.create(pokemon["pokemon"], level, StatusEffect.NONE, 1.0))

    for pokemonName in pokemonObjs.keys():
        with open(f"Results/Ex2c/{pokemonName}-data.csv", "w", newline='') as f:
            writer = csv.writer(f)

            # writes titles to the components of the CSV results file
            writer.writerow(["pokeball name"] + [level for level in range(MINLEVEL, MAXLEVEL+1)])

            for pokeball in pokeballs:
                catchRate = {}

                for pokemonWithNLevel in pokemonObjs[pokemonName]:
                    catches = 0
                    for _ in range(ITERATIONS):
                        catched, probability = attempt_catch(pokemonWithNLevel, pokeball)
                        if catched:
                            catches += 1

                    catchRate[pokemonWithNLevel] = catches / ITERATIONS

                printData = [pokeball]
                for percentage in catchRate.values():
                    printData.append(percentage)

                writer.writerow(printData)