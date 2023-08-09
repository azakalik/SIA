import csv
import os
import pandas as pd
import plotly.express as px
import plotly
from src.pokemon import *
from src.catching import attempt_catch

ITERATIONS = 10000


def ex2a(configFileName):
    with open(configFileName, "r") as fp:
        pokemons = json.load(fp)

    pokemonObjs = {}

    pokeballs = ["pokeball", "ultraball", "fastball", "heavyball"]

    factory = PokemonFactory("pokemon.json")

    for pokemon in pokemons:

        pokemonObjs[pokemon["pokemon"]] = []

        for effect in StatusEffect:
            pokemonObjs[pokemon["pokemon"]].append(factory.create(pokemon["pokemon"], pokemon["level"], effect, 1.0))

    for pokemonName in pokemonObjs.keys():
        with open(f"Results/Ex2a/{pokemonName}-data.csv", "w", newline='') as f:
            writer = csv.writer(f)

            writer.writerow(["pokeball name"] + [effect.value[0] for effect in StatusEffect])

            for pokeball in pokeballs:
                catchRate = {}

                for pokemonWithEffect in pokemonObjs[pokemonName]:
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


def graph_ex2a():

    for name in os.listdir("./Results/Ex2a/"):
        pokemonName = name.split("-")[0]
        data = []
        with open(f"./Results/Ex2a/{pokemonName}-data.csv", "r") as pokemonFile:
            reader = csv.reader(pokemonFile)

            names = next(reader)
            statusEffectNames = names[1::]
            for values in reader:

                iterable = iter(values)
                pokeball = next(iterable)

                for index, value in enumerate(iterable):
                    data.append({'Effect': statusEffectNames[index], 'Pokeball': pokeball, 'Probability': float(value)})

        df = pd.DataFrame(data)
        fig = px.bar(df, x='Effect', y='Probability', color='Pokeball', barmode='group')

        plotly.offline.plot(fig, filename=f"./Results/Ex2a/{pokemonName}-graph.html")


