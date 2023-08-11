# menor cantidad de vida
# dormido o congelado
# bajo nivel
# heavy para pesados (snorlax)
# fast para rapidos (jolteon)

import json
import os
import csv
import pandas as pd
import plotly.express as px
import numpy as np
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect, Pokemon

ITERATIONS = 100


def ex2d(configFileName):
    factory = PokemonFactory("pokemon.json")
    with open(configFileName, "r") as f:
        pokemons = json.load(f)

        pokeballs = ["pokeball", "heavyball", "fastball"]
        levels = [1, 25, 50, 75, 100]
        healths = [0.01, 0.25, 0.50, 0.75, 1]
        pokeMap = {}

        for pocketMonster in pokemons:
            pokeMap[pocketMonster["pokemon"]] = {}
            for level in levels:
                pokeMap[pocketMonster["pokemon"]][level] = {}
                for health in healths:
                    pokeMap[pocketMonster["pokemon"]][level][health] = []
                    
            for level in levels:
                for health in healths:
                    for effect in StatusEffect:
                        pokeMap[pocketMonster["pokemon"]][level][health].append(factory.create(pocketMonster["pokemon"], level, effect, health))


        for pokeName in pokeMap.keys():
            with open(f"Results/Ex2d/{pokeName}-data.csv", "w", newline='') as f:
                writer = csv.writer(f)

                i = 0
                while i < 6:
                    writer.writerow(["pokeball name"] + [effect.value[0] for effect in StatusEffect])
                    i += 1

                    for pokeball in pokeballs:
                        catchRate = {}

                        for level in levels:
                            for health in healths:
                                for pokemonWithEffect in pokeMap[pokeName][level][health]:
                                    catches = 0
                                    for _ in range(ITERATIONS):
                                        catched, probability = attempt_catch(pokemonWithEffect, pokeball)
                                        if catched:
                                            catches += 1

                                    catchRate[pokemonWithEffect.status_effect] = catches / ITERATIONS

                                printData = [pokeball]
                                for percentage in catchRate.values():
                                    printData.append(percentage)

                                writer.writerow(printData)

