import json
import os
import csv
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect, Pokemon


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
                for _ in range(100):
                    catched, probability = attempt_catch(pokemon, ball)
                    if catched:
                        catches += 1
                print(f"{pokemon.name},{catches / 100}", file=f)


def graph_ex1():
    pokeballs = []
    for name in os.listdir("./Results/Ex1/"):
        pokeball = name.split("-")[0]
        pokeballs.append(pokeball)
        with open(f"{pokeball}-data.csv", "r") as pokeball_file:
            reader = csv.reader(pokeball_file)
            

