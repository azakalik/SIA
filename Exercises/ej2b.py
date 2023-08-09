import json
import os
import csv
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect, Pokemon


def ex2(configFileName):
    factory = PokemonFactory("pokemon.json")
    with open(configFileName, "r") as f:
        config = json.load(f)

        pokeball = "pokeball"

        
        for item in config:
            hp = 0.01
            pokemon = factory.create(item["pokemon"], item["level"], StatusEffect.NONE, hp)
            with open(f"Results/Ex2b/{pokemon.name}-hp-data.csv", "w") as f:
                while( hp <= 1 ):
                    pokemon.current_hp = pokemon.max_hp * hp
                    catches = 0
                    for _ in range(100):
                        catched, probability = attempt_catch(pokemon, pokeball)
                        if catched:
                            catches += 1
                    print(f"{round(pokemon.current_hp/pokemon.max_hp,2)},{catches / 100}", file=f)
                    hp += 0.01


