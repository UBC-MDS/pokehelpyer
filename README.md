# pokehelpyer

The Python package, pokehelpyer, assists Pokemon players in building teams of various pokemon types based on weaknesses and resistances Using the five names of Pokemons provided by the user, pokehelpyer recommends the sixth player that would be best suited according to the types of the Pokemons present in the current team. It bases this recommendation on the calculations of weaknesses and resistances to make a team less susceptible to a certain weakness. 

## Contributors
- Raul Aguilar
- Jakob Thoms
- Ritisha Sharma
- Sneha Sunil

## Functions Included
- `add_team_members`: Given a list of names of Pokemons provided by the user, it finds the corresponding types from a dataset present in the project. 

- `calc_resistance`: Given a list of Pokemon types (based on the team provided by the user), calculates all the Pokemon types to which the team provided is resistant to. It uses a pokemon-chart dataset for details on the resistances.

- `calc_weakness`: Given a list of Pokemon types, calculates the total number of typesfrom the team list (based on the team provided by the user), which is weak against each of the pokemon type in the game. It uses a pokemon-chart dataset for details on the resistances.

- `recommend`: Using the calculations of weaknesses and strengths, it identifies the weak spots on the team and recommends the sixth team member.


## Installation

```bash
$ pip install pokehelpyer
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pokehelpyer` was created by Sneha Sunil, Jakob Thoms, Ritisha Sharma, Raul Aguilar. It is licensed under the terms of the MIT license.

## Credits

`pokehelpyer` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
