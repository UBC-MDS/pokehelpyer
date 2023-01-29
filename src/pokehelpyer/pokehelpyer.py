import pandas as pd
import re


def get_types(pokemon_names):
    """
    Given a list of pokémon names, determine the types of
    those pokémon using an existing dataset.

    Parameters
    ----------
    pokemon_names : list of strings
        list of pokémon names

    Returns
    -------
    pokemon_types : list of lists of strings
        list of lists of pokémon types corresponding to
        the pokémon names in the input list

    Example
    --------
    >>> get_types(['Pikachu', 'Eevee', 'Charizard', ...])
    [['Electric'], ['Normal'], ['Fire', 'Flying'], ...]
    """
    # Handle user input error in case of single pokemon
    if isinstance(pokemon_names, str):
        pokemon_names = [pokemon_names]
    # Check user input
    try:
        assert isinstance(
            pokemon_names, list
        ), f'{"Input should be a list of pokemon names."}'
        assert (
            len(pokemon_names) > 0
        ), f'{"Input should be a non-empty list of pokemon names."}'
        assert isinstance(
            pokemon_names[0], str
        ), f'{"Input should be a list of pokemon names."}'
    except AssertionError as ex:
        print(f"Invalid input: {ex}")
        return None

    # Read file with Pokemon names and types,
    # and keep only relevant subset of the data
    url = (
        "https://raw.githubusercontent.com/"
        + "UBC-MDS/pokehelpyer/main/data/pokemon.csv"
    )

    names_types_df = pd.read_csv(url)[["Name", "Type 1", "Type 2"]]

    # Clean string column "Name"
    names_types_df["Name"] = names_types_df["Name"].str.strip()
    names_types_df["Name"] = names_types_df["Name"].str.lower()
    # Some of the names in dataset contain symbols
    name_with_symbol = names_types_df[
        names_types_df["Name"].str.match(r".*[^\w\s].*")
    ]["Name"].tolist()

    poke_types = []
    for name in pokemon_names:
        # Clean string
        name = name.strip()
        name = name.lower()
        # Check if name is supposed to contain symbol, otherwise remove
        if name not in name_with_symbol:
            name = re.sub(r"[^\w\s]", "", name)

        # Check if exists in data
        assert (
            name in names_types_df["Name"].tolist()
        ), f'{"{name} is not a valid pokémon."}'

        # Find the row with match
        row = names_types_df.loc[names_types_df["Name"] == name].values[0]
        poke_types.append([row[1], row[2]])
        if pd.isna(row[2]):  # Type 2 is optional
            poke_types[-1].pop()

    return poke_types


def calc_resistances(team_types):
    """
    Given a list of pokémon types present on a player's team,
    calculate a measure of how resistant the team is to each type in the game.

    Creates a dictionary in which the keys are each of the 18 types
    in the game, and the values are integers measuring the level of
    resistance the input team has to that type. Higher values indicate a
    higher level of resistance to that type (key).

    Parameters
    ----------
    team_types : list of list of strings
        list of pokémon types associated to the user's team
        obtained via `get_types`

    Returns
    -------
    resistances : dictionary
        a dictionary containing all 18 pokémon types as keys,
        and integers measuring the level of resistance the input team
        has to that type as values.

    Examples
    --------
    >>> calc_resistances([['Electric'], ['Normal'],
                          ['Fire', 'Flying']])
    {'Normal': 0, 'Fire': 1, 'Water': 0, 'Grass': 2, 'Electric': 1, ...}

    >>> calc_resistances([['Steel', 'Flying']])
        # Skarmory is doubly resistant to Grass
    {'Normal': 1, 'Fire': 0, 'Water': 0, 'Grass': 2, 'Electric': 0, ...}

    """
    # Check user input
    try:
        assert isinstance(
            team_types, list
        ), f'{"Input should be a list of lists of pokemon types."}'
        assert (
            len(team_types) > 0
        ), f'{"Input should be a non-empty list of lists of pokemon types."}'
        assert isinstance(
            team_types[0], list
        ), f'{"Input should be a list of lists pokemon types."}'
        assert (
            len(team_types[0]) > 0
        ), f'{"Input should be a list of non-empty lists of pokemon types."}'
        assert isinstance(
            team_types[0][0], str
        ), f'{"Input should be a list of lists pokemon types."}'
    except AssertionError as ex:
        print(f"Invalid input: {ex}")
        return None

    # Loads the file with Pokemon types,
    # strengths and weaknesses into a data frame
    url = (
        "https://raw.githubusercontent.com/"
        + "UBC-MDS/pokehelpyer/main/data/type_chart.csv"
    )
    resistances_df = pd.read_csv(url, index_col=0)

    # Creating dictionary with all Pokemon types
    all_types = resistances_df.index.tolist()
    resistances = {x: 0 for x in all_types}

    for attacking_type in all_types:
        for type_combo in team_types:
            val1 = resistances_df.loc[attacking_type][type_combo[0]]
            if len(type_combo) == 1:
                val2 = 1
            else:
                val2 = resistances_df.loc[attacking_type][type_combo[1]]

            if val1 == 0 or val2 == 0:
                resistances[attacking_type] += 3
            elif (val1 == 0.5 and val2 == 2) or (
                val1 == 2 and val2 == 0.5
            ):
                continue
            elif val1 == 0.5 and val2 == 0.5:
                resistances[attacking_type] += 2
            elif (val1 == 1 and val2 == 0.5) or (
                val1 == 0.5 and val2 == 1
            ):
                resistances[attacking_type] += 1

    return resistances


def calc_weaknesses(team_types):
    """
    Given a list of pokémon types present on a player's team,
    calculate a measure of how weak the team is to each type in the game.

    Creates a dictionary in which the keys are each of the 18 types
    in the game, and the values are integers measuring the level of
    weakness the input team has to that key (type). Higher values indicate a
    higher level of weakness to that type.

    Parameters
    ----------
    team_types : list of list of strings
        list of pokémon types associated to the user's team
        obtained via `get_types`

    Returns
    -------
    weaknesses : dictionary
        a dictionary containing all 18 pokémon types as keys,
        and integers measuring the level of weakness the input team
        has to that type as values.

    Examples
    --------
    >>> calc_weaknesses([['Electric'], ['Normal'], ['Fire', 'Flying']])
    {'Normal': 0, 'Fire': 0, 'Water': 1, 'Grass': 0, 'Electric': 1, ...}

    >>> calc_weaknesses([['Ice', 'Grass']) # Abomasnow is doubly weak to Fire
    {'Normal': 0, 'Fire': 2, 'Water': 0, 'Grass': 0, 'Electric': 0, ...}

    """
    # Check user input
    try:
        assert isinstance(
            team_types, list
        ), f'{"Input should be a list of lists of pokemon types."}'
        assert (
            len(team_types) > 0
        ), f'{"Input should be a non-empty list of lists of pokemon types."}'
        assert isinstance(
            team_types[0], list
        ), f'{"Input should be a list of lists pokemon types."}'
        assert (
            len(team_types[0]) > 0
        ), f'{"Input should be list of non-empty lists of pokemon types."}'
        assert isinstance(
            team_types[0][0], str
        ), f'{"Input should be a list of lists pokemon types."}'
    except AssertionError as ex:
        print(f"Invalid input: {ex}")
        return None

    # Read the pokemon weakness dataframe using pandas
    url = (
        "https://raw.githubusercontent.com/"
        + "UBC-MDS/pokehelpyer/main/data/type_chart.csv"
    )
    weakness_df = pd.read_csv(url, index_col=0)

    # Fetch all types of pokemon
    all_types = weakness_df.index.tolist()
    weaknesses = {x: 0 for x in all_types}

    # Calculate weaknesses of all types and add it to a dictionary
    for attacking_type in all_types:
        for type_combo in team_types:
            val1 = weakness_df.loc[attacking_type][type_combo[0]]
            if len(type_combo) == 1:
                val2 = 1
            else:
                val2 = weakness_df.loc[attacking_type][type_combo[1]]

            if val1 == 0 or val2 == 0:
                continue
            elif (val1 == 0.5 and val2 == 2) or (
                val1 == 2 and val2 == 0.5
            ):
                continue
            elif val1 == 2 and val2 == 2:
                weaknesses[attacking_type] += 2
            elif (val1 == 1 and val2 == 2) or (val1 == 2 and val2 == 1):
                weaknesses[attacking_type] += 1

    return weaknesses


def recommend(
    current_team,
    n_recommendations=1,
    include_legendaries=False,
    include_megas=False,
    verbose=True,
    early_stop=False,
):
    """
    Given a team of up to 5 pokémon, recommend a
    pokémon that could be added to the
    current team to make its weaknesses and
    resistances more balanced.

    This function first determines which types the
    team is most weak to and which types the team is
    most resistant to via `calc_resistances` and
    `calc_weaknesses`, and then makes its recommendation
    based on this information.
    In particular, it uses `calc_balance` together a brute-force search of
    all ~700 pokémon to determine its recommendation based on the objective of
    maximizing balance.

    Parameters
    ----------
    current_team : list of strings
        list of up to 5 pokémon names
    n_recommendations : integer
        number of pokemon to recommend (default = 1).
    include_legendaries : boolean
        whether or not to include legendary pokémon in
        the recommendations (default = False).
    include_megas : boolean
        whether or not to include Mega pokémon in
        the recommendations (default = False).
    verbose : boolean
        whether or not to print progress updates during the brute-force search.
    early_stop : boolean
        whether or not to stop the brute force search early
        (for speeding up unit testing) (default = False).

    Returns
    -------
    reccomendation : string
        the name of a pokémon that could be added to the input
        team to make its weaknesses and resistances more balanced.

    Example
    --------
    >>> recommend(['Pikachu', 'Eevee', 'Charizard', ...])
    "Lucario"
    """
    # Handle user input error in case of single-pokemon team
    if isinstance(current_team, str):
        current_team = [current_team]

    # Check user input
    try:
        assert isinstance(
            current_team, list
        ), f'{"current_team should be a list of pokemon names."}'
        assert (
            len(current_team) > 0
        ), f'{"current_team should be a non-empty list of pokemon names."}'
        assert (
            len(current_team) < 6
        ), f'{"current_team should have less than six pokemon names."}'
        assert isinstance(
            current_team[0], str
        ), f'{"current_team should be a list of pokemon names."}'
        assert isinstance(
            n_recommendations, int
        ), f'{"n_recommendations should be an integer."}'
    except AssertionError as ex:
        print(f"Invalid input: {ex}")
        return None

    url = (
        "https://raw.githubusercontent.com/"
        + "UBC-MDS/pokehelpyer/main/data/pokemon.csv"
    )
    pokemon_df = pd.read_csv(url)
    if not include_legendaries:
        pokemon_df = pokemon_df.query("Legendary == False")
    if not include_megas:
        pokemon_df = pokemon_df[~pokemon_df["Name"].str.contains("Mega")]

    team_types = get_types(current_team)
    current_resistances = calc_resistances(team_types)
    current_weaknesses = calc_weaknesses(team_types)

    new_balance_dict = dict()

    # Loop through all posible pokemon that could be added to the team
    for i in range(len(pokemon_df)):
        pkmn = pokemon_df.iloc[i, :]
        pkmn_name = pkmn["Name"]
        pkmn_types = [pkmn["Type 1"], pkmn["Type 2"]]
        if pd.isna(pkmn_types[1]):
            pkmn_types.pop()

        pkmn_resistances = calc_resistances([pkmn_types])
        pkmn_weaknesses = calc_weaknesses([pkmn_types])

        # add the pokemon's resistances to the current team's resistances
        new_resistances = dict()
        for type_combo in current_resistances.keys():
            new_resistances[type_combo] = (
                current_resistances[type_combo]
                + pkmn_resistances[type_combo]
            )

        # add the new pokemon's weaknesses to the current team's weaknesses
        new_weaknesses = dict()
        for type_combo in current_weaknesses.keys():
            new_weaknesses[type_combo] = (
                current_weaknesses[type_combo]
                + pkmn_weaknesses[type_combo]
            )

        new_balance = calc_balance(new_resistances, new_weaknesses)
        new_balance_dict[pkmn_name] = new_balance

        if verbose and i % 100 == 99 or i == 0:
            print(f"Iteration number {i + 1} of {len(pokemon_df)}.")

        if early_stop and i > 30:
            print("Stopping early because `early_stop = True`.")
            print("Normally this is only used for testing.")
            break

    new_balance_df = (
        pd.DataFrame(new_balance_dict, index=["balance"])
        .T.reset_index()
        .rename(columns={"index": "Name"})
        .set_index("Name")
    )

    results_df = new_balance_df.join(
        pokemon_df.set_index("Name"), on="Name"
    ).sort_values(by=["balance", "Total"], ascending=False)

    if n_recommendations == 1:
        return results_df.iloc[0, :].name

    temp_df = results_df
    recommendations = []
    for i in range(n_recommendations):
        recommendations.append(temp_df.iloc[0, :].name)
        current_best_balance = temp_df.iloc[0, :]["balance"]
        # Only to pass style check
        if current_best_balance:
            pass
        temp_df = temp_df.query(
            "balance != @current_best_balance"
        ).sort_values(by=["balance", "Total"], ascending=False)

    return recommendations


def calc_balance(resistances, weaknesses):
    """
    Calculate a measure of how balanced a team is using its
    weaknesses and resistances.

    Higher values indicate a more balanced team.

    Parameters
    ----------
    resistances : dictionary
        obtained from calc_resistances

    weaknesses : dictionary
        obtained from calc_weaknesses

    Returns
    -------
    balance : float
        measure of how balanced the team is.

    Examples
    --------
    >>> bad_team = ['Abomasnow', 'Ferrothorn', 'Parasect']
        # All are doubly weak to fire
    >>> resistances = calc_resistances(get_types(bad_team))
    >>> weaknesses = calc_weaknesses(get_types(bad_team))
    >>> calc_balance(resistances, weaknesses)
    -3.11243

    >>> good_team = ['Spiritomb', 'Garchomp', 'Lucario']
    >>> resistances = calc_resistances(get_types(good_team))
    >>> weaknesses = calc_weaknesses(get_types(good_team))
    >>> calc_balance(resistances, weaknesses)
    25.06687
    """
    # Check user input
    try:
        assert isinstance(
            resistances, dict
        ), r"""Input 1 should be a dictionary of resistance values
            of the form {pkmn_type: <int or float>}."""
        assert isinstance(
            weaknesses, dict
        ), r"""Input 2 should be a dictionary of weakness values
            of the form {pkmn_type: <int or float>}."""
        url = (
            "https://raw.githubusercontent.com/"
            + "UBC-MDS/pokehelpyer/main/data/type_chart.csv"
        )
        types_set = set(
            pd.read_csv(url)["Attacking"].tolist()
        )
        assert (
            set(resistances.keys()) == types_set
        ), """Input 1 should be a dictionary of resistance values obtained
            via `calc_resistances`.\n
            There should be one key for each of the 18 pokemon types
            (including Fairy)."""
        assert (
            set(weaknesses.keys()) == types_set
        ), """Input 2 should be a dictionary of weakness values obtained
            via `calc_weaknesses`.\n
            There should be one key for each of the 18 pokemon types
            (including Fairy)."""
        assert isinstance(
            resistances["Normal"], (float, int)
        ), """Input 1 should be a dictionary of resistance values obtained
            via `calc_resistances`.\n
            The values should be floats or integers."""
        assert isinstance(
            weaknesses["Normal"], (float, int)
        ), """Input 2 should be a dictionary of weakness values obtained
            via `calc_weaknesses`.\n
            The values should be floats or integers."""
    except AssertionError as ex:
        print(f"Invalid input: {ex}")
        return None

    type_advantages = dict()
    for type_combo in resistances.keys():
        delta = resistances[type_combo] - weaknesses[type_combo]

        # Peicewise function to penalize negative values more
        # (i.e. to favor penalizing weaknesses over rewaring resistances)
        if delta >= 0:
            type_advantages[type_combo] = delta ** (3 / 4)
        else:
            type_advantages[type_combo] = -((-delta) ** (3 / 2))

    balance = sum(type_advantages.values())
    return balance
