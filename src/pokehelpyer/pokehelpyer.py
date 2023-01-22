import pandas as pd
import itertools
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
    # Check input type
    assert isinstance(pokemon_names, (list, str)), f"Incorrect input type."

    # Check for empty input
    assert len(pokemon_names) != 0, "No names provided."

    if isinstance(pokemon_names, str):
        pokemon_names = [pokemon_names]

    # Read file with Pokemon names and types
    url = "https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv"
    # Keep only relevant subset of the data
    names_types_df = pd.read_csv(url)[["Name", "Type 1", "Type 2"]]

    # Clean string column "Name"
    names_types_df["Name"] = names_types_df["Name"].str.strip()
    names_types_df["Name"] = names_types_df["Name"].str.lower()
    # Some of the names in dataset contain symbols
    name_with_symbol = names_types_df[names_types_df["Name"].str.match(".*[^\w\s].*")]["Name"].tolist()
    
    poke_types = []
    for name in pokemon_names:
        # Clean string
        name = name.strip()
        name = name.lower()
        # Check if name is supposed to contain symbol, otherwise remove
        if name not in name_with_symbol:
            name = re.sub(r"[^\w\s]", "", name)
                
        # Check if exists in data
        assert name in names_types_df["Name"].tolist(), f"{name} is not a valid pokémon."
        
        # Find the row with match
        row = names_types_df.loc[names_types_df["Name"] == name].values[0]
        # Type 2 is optional
        if pd.isna(row[2]):
            poke_types.append([row[1]])
        else:
            poke_types.append([row[1], row[2]])
            
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
    >>> calc_resistances([['Electric'], ['Normal'], ['Fire', 'Flying']]) 
    {'Normal': 0, 'Fire': 1, 'Water': 0, 'Grass': 2, 'Electric': 1, ...}

    >>> calc_resistances([['Steel', 'Flying']]) # Skarmory is doubly resistant to Grass
    {'Normal': 1, 'Fire': 0, 'Water': 0, 'Grass': 2, 'Electric': 0, ...}
    
    """
    # Check for empty input
    assert len(team_types) != 0, "No types provided"

    # Reads the file with Pokemon types, strengths and weaknesses
    url = "https://raw.githubusercontent.com/zonination/pokemon-chart/master/chart.csv"

    # Saves the data in Pandas data frame
    resistances_df = pd.read_csv(url)

    # Flattening list and creating dictionary with all Pokemon types
    flat_types = list(itertools.chain.from_iterable(team_types))
    resistances_dict = {value: 0 for value in resistances_df['Attacking'].values.tolist()}

    # Iterates over all types in the team
    for i in flat_types:

        # Checks for type resistance and adds 1 to Pokemon type 
        normal_resistance = resistances_df[['Attacking', i]].query(f'{i}==0.5') 
        list_normal = normal_resistance['Attacking'].values.tolist()
        
        for item in list_normal:
            if item in resistances_dict:
                resistances_dict[item] += 1

        # Checks for Pokemon immunity and adds 4 to Pokemon type        
        double_resistance = resistances_df[['Attacking', i]].query(f'{i}==0')
        list_double = double_resistance['Attacking'].values.tolist()
                
        for item in list_double:
            if item in resistances_dict:
                resistances_dict[item] += 4
    
    return resistances_dict


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
    >>> calc_weaknesses([['Electric'], ['Normal'], ['Fire', 'Flying']) 
    {'Normal': 0, 'Fire': 0, 'Water': 1, 'Grass': 0, 'Electric': 1, ...}

    >>> calc_weaknesses([['Ice', 'Grass']) # Abomasnow is doubly weak to Fire
    {'Normal': 0, 'Fire': 2, 'Water': 0, 'Grass': 0, 'Electric': 0, ...}
    
    """    
    # Check if input list is empty
    if len(team_types) == 0:
        return

    # Read the pokemon weakness dataframe using pandas
    try:
        weakness_df = pd.read_csv("https://raw.githubusercontent.com/zonination/pokemon-chart/master/chart.csv", sep=',', index_col = 0)
    except Exception as ex:
        print("Exception occurred :" + ex)
        return
    
    # Check if the returned object is a dataframe and fetch all types of pokemon
    if isinstance(weakness_df, pd.DataFrame):
        all_types = weakness_df.index.tolist()
        weaknesses = {x: 0 for x in all_types}

    # Calculate weaknesses of all types and add it to a dictionary
    if all_types:
        for item in all_types:
            weakness_counter = 0
            for type in team_types:
                if len(type) == 1:
                    val1 = weakness_df.loc[item][type[0]]
                    if(val1 == 2):
                        weakness_counter = 1

                elif len(type) == 2:
                    type1 = type[0]
                    type2 = type[1]
                    val1 = weakness_df.loc[item][type1]
                    val2 = weakness_df.loc[item][type2]

                    if val1 == 2 and val2 == 2:
                        weakness_counter += 2
                    elif (val1 == 1 and val2 == 2) or (val1 == 2 and val2 == 1):
                        weakness_counter += 1
            
            weaknesses[item] = weakness_counter
    return weaknesses

def recommend(current_team, n_recommendations=1, include_legendaries=False, include_megas=False, verbose=True):
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
    if isinstance(pokemon_names, str):
        pokemon_names = [pokemon_names]

    # Check user input
    assert isinstance(current_team, list), f"current_team should be a list of pokemon names."
    assert len(current_team) > 0, "current_team should be a non-empty list of pokemon names."
    assert isinstance(current_team[0], str), f"current_team should be a list of pokemon names."
    assert isinstance(n_recommendations, int), f"n_recommendations should be an integer."
    assert isinstance(include_legendaries, bool), f"include_legendaries should be a boolean value."
    assert isinstance(include_megas, bool), f"include_megas should be a boolean value."
    assert isinstance(verbose, bool), f"verbose should be a boolean value."

    try:
        pokemon_df = pd.read_csv('data/pokemon.csv')
    except Exception as ex:
        print("Exception occurred when loading pokémon data: " + ex)
        return
    if not include_legendaries:
        pokemon_df = pokemon_df.query("Legendary == False")
    if not include_megas:
        pokemon_df = pokemon_df[~pokemon_df['Name'].str.contains('Mega')]

    team_types = get_types(current_team)
    current_resistances = calc_resistances(team_types)
    current_weaknesses = calc_weaknesses(team_types)

    new_balance_dict = dict()

    # Loop through all posible pokemon that could be added to the team
    for i in range(len(pokemon_df)):
        pkmn = pokemon_df.iloc[i, :]
        pkmn_name = pkmn['Name']
        pkmn_types = [pkmn['Type 1'], pkmn['Type 2']]
        if pd.isna(pkmn_types[1]):
            pkmn_types.pop()

        pkmn_resistances = calc_resistances([pkmn_types])
        pkmn_weaknesses = calc_weaknesses([pkmn_types])

        # add the pokemon's resistances to the current team's resistances
        new_resistances = dict()
        for type in current_resistances.keys():
            new_resistances[type] = current_resistances[type] + pkmn_resistances[type]

        # add the new pokemon's weaknesses to the current team's weaknesses
        new_weaknesses = dict()
        for type in current_weaknesses.keys():
                new_weaknesses[type] = current_weaknesses[type] + pkmn_weaknesses[type]

        new_balance = calc_balance(new_resistances, new_weaknesses)
        new_balance_dict[pkmn_name] = new_balance
        
        if verbose and i % 25 == 24 or i == 0:
            print(f'Iteration number {i + 1} of {len(pokemon_df)}.')

    new_balance_df = pd.DataFrame(new_balance_dict, index=['balance']).T.\
        reset_index().rename(columns={'index': 'Name'}).set_index('Name')

    results_df = new_balance_df.join(pokemon_df.set_index('Name'), on = 'Name').\
        sort_values(by=['balance', 'Total'], ascending=False)

    if n_recommendations == 1:
        return results_df.iloc[0, :].name

    temp_df = results_df
    recommendations = []
    for i in range(n_recommendations):
        recommendations.append(temp_df.iloc[0, :].name)
        current_best_balance = temp_df.iloc[0, :]['balance']
        temp_df = temp_df.query("balance != @current_best_balance").\
        sort_values(by=['balance', 'Total'], ascending=False)

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

    Example
    --------
    TO-DO
    """
    type_advantages = dict()
    for type in resistances.keys():
        delta = resistances[type] - weaknesses[type]
        if delta >= 0:
            type_advantages[type] = delta ** (3 / 4)
        else:
            type_advantages[type] = -(-delta) ** (3 / 2)
    
    balance = sum(type_advantages.values())
    return balance
    