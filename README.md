[![ci-cd](https://github.com/UBC-MDS/pokehelpyer/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/pokehelpyer/actions/workflows/ci-cd.yml)

# pokehelpyer

`pokehelpyer` is a Python package designed to assist Pokémon players in building teams of pokémon. Users can provide a list of pokémon currently on their team, and `pokehelpyer` will recommend a suitable pokémon to add to the team based on the current team's overall weaknesses and resistances.

In the Pokémon game, players battle using teams of up to six pokémon. Each pokémon has a type, such as grass, water, or fire. Each type in the game is either weak to, resistant to, or neutrally affected by each other type in the game. If a player does not consider these weaknesses and resistances when creating their team of pokémon, they may find themselves in a scenario in which they are consistently struggling to win battles against certain types of pokémon. For a simple example, if a player were to use a team of six fire-type pokémon, then they would likely struggle to win battles against water-type pokémon. The preceding is obviously an extreme example, but in a competitive setting, even a small imbalance in a team's weaknesses and resistances can cause major issues for a player.

The `pokehelpyer` package aims to assist players in avoiding imbalances in weaknesses/resistances when building a pokémon team. Given a list of up to five pokémon currently on a team, `pokehelpyer` will determine which types the team is most weak to and which types the team is most resistant to. Based on this information, `pokehelpyer` will then recommend a pokémon that could be added to the current team to make its weaknesses and resistances more balanced.

(If you are reading this and aren't familiar with Pokémon, it might be helpful to note that "pokémon" is both the singular and plural form of the word, and also that lowercase "pokémon" refers to an individual character in the game, such as Pikachu, whereas capitalized "Pokémon" refers to the franchise/game.)

## Functions Included

- `get_types`: Given a list of pokémon names, determine the types of those pokémon using an existing dataset.
<br>

- `calc_resistances`:  Given a list of pokémon types present on a player's team,
    calculate a measure of how resistant the team is to each type in the game.

  - Creates a dictionary in which the keys are each of the 18 types
    in the game, and the values are integers measuring the level of
    resistance the input team has to that key (type). Higher values indicate a
    higher level of resistance to that type.
<br><br>

- `calc_weaknesses`: Given a list of pokémon types present on a player's team,
    calculate a measure of how weak the team is to each type in the game.

  - Creates a dictionary in which the keys are each of the 18 types
    in the game, and the values are integers measuring the level of
    weakness the input team has to that key (type). Higher values indicate a
    higher level of weakness to that type.
<br><br>

- `recommend`: Given a team of up to 5 pokémon, recommend a
    pokémon that could be added to the
    current team to make its weaknesses and
    resistances more balanced.
  - Determines which types the
    team is most resistant to and weak to via `calc_resistances` and
    `calc_weaknesses`, and then makes its recommendation
    based on this information.
  - In particular, it uses `calc_balance` together a brute-force search of
    all ~700 pokémon to determine its recommendation based on the objective of
    maximizing balance.
<br><br>

- `calc_balance`: Calculate a measure of how balanced a pokémon team is using its
    weaknesses and resistances. Higher values indicate a more balanced team.

## Datasets Included

- [pokémon.csv](https://github.com/UBC-MDS/pokehelpyer/blob/main/data/pokemon.csv): Dataset containing details about each pokémon including its name, type(s), and base stats.
- [type_chart.csv](https://github.com/UBC-MDS/pokehelpyer/blob/main/data/type_chart.csv): Dataset containing details abouts the weaknesses and strengths of each type of pokémon.

## Place Within the Python Ecosystem

There are websites and applications that help build pokémon teams, such as the [Mariland Team Builder](https://marriland.com/tools/team-builder/en/). However these tools simply present the player with a visual representation of their current team's weaknesses and resistances. They don't make recommendations. In other words, the existing tools simply given visual representations of the dictionaries created by `calc_weaknesses` and `calc_resistances`. There doesn't seem to be any existing Python packages which will use the weaknesses/resistances data to make reccomendations for additional team members.

## Installation

```bash
pip install pokehelpyer
```

## Usage

See https://pokehelpyer.readthedocs.io/en/latest/

```python
import pokehelpyer.pokehelpyer as pk
```

<br>

`get_types`:

```python
team_list = ['Pikachu', 'Eevee', 'Charizard', 'Metapod']
team_types = pk.get_types(team_list)
```

<br>

`calc_weaknesses` and `calc_resistances`:

```python
team_weaknesses = pk.calc_weaknesses(team_types)
team_resistances = pk.calc_resistances(team_types)
```

<br>

`calc_balance`:

```python
team_balance = pk.calc_balance(
    resistances=team_resistances, 
    weaknesses=team_weaknesses
)
```

`recommend`:

```python
pk.recommend(['Pikachu', 'Eevee', 'Charizard', 'Metapod'], n_recommendations=2)
```

## Contributors

- Raul Aguilar
- Jakob Thoms
- Ritisha Sharma
- Sneha Sunil

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/pokehelpyer/blob/main/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/pokehelpyer/blob/main/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## Credits

`pokehelpyer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## License

`pokehelpyer` was created by Jakob Thoms, Ritisha Sharma, Raul Aguilar, and Sneha Sunil. It is licensed under the terms of the MIT license.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
