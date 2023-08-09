import sys
import json
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect, Pokemon


if __name__ != "__main__":
    quit()


factory = PokemonFactory("pokemon.json")
with open(f"{sys.argv[1]}", "r") as f:
    config = json.load(f)
    pokemons : list[Pokemon] = []
    for item in config:
        pokemon = factory.create(item["pokemon"], item["level"], StatusEffect.NONE, item["hp"])
        pokemons.append(pokemon)
    
    pokeballs = ["pokeball","ultraball","fastball","heavyball"]

    for ball in pokeballs:
        with open(f"Results/Ex1/{ball}-data.csv","w") as f:
            for pokemon in pokemons:
                catches = 0
                for _ in range(100):
                    catched, probability = attempt_catch(pokemon,ball)
                    if catched:
                        catches += 1
                print(f"{pokemon.name},{catches / 100}",file=f)
                        




    # print("No noise: ", attempt_catch(pokemon, ball))
    # for _ in range(10):
    #     print("Noisy: ", attempt_catch(pokemon, ball, 0.15))
