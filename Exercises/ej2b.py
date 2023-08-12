import json
import os
import csv
import pandas as pd
import plotly.express as px
import numpy as np
from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect, Pokemon


def ex2b(configFileName):
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


def graph_ex2b():
    data = []

    for name in os.listdir("./Results/Ex2b/"):
        pokemon = name.split("-")[0]

        with open(f"./Results/Ex2b/{pokemon}-hp-data.csv", "r") as pokemon_file:
            reader = csv.reader(pokemon_file)
            next(reader)  # Skip header row

            health = []
            capture_percentage = []

            for row in reader:
                health.append(float(row[0]))
                capture_percentage.append(float(row[1]))

            data.append({
                'pokemon': pokemon,
                'health': health,
                'capture_percentage': capture_percentage
            })

    scatter_data = []
    for item in data:
        scatter_data.extend([
            {'pokemon': item['pokemon'], 'health': h, 'capture_percentage': c}
            for h, c in zip(item['health'], item['capture_percentage'])
        ])

    df = pd.DataFrame(scatter_data)

    fig = px.scatter(df, x='health', y='capture_percentage', color='pokemon',
                     title='Pokemon Health vs. Capture Percentage',
                     labels={'health': 'Health', 'capture_percentage': 'Capture Percentage'},
                     width=800, height=600)

    # Calculate and add lines of best fit for each Pokémon's data
    for pokemon in df['pokemon'].unique():
        pokemon_df = df[df['pokemon'] == pokemon]
        line_fit = np.polyfit(pokemon_df['health'], pokemon_df['capture_percentage'], 1)
        line_equation = f'{pokemon} Best Fit: y = {line_fit[0]:.4f}x + {line_fit[1]:.4f}'
        fig.add_scatter(x=pokemon_df['health'], y=np.polyval(line_fit, pokemon_df['health']),
                        mode='lines', name=line_equation)

    fig.show()
