import pandas as pd

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
    # Function code (TBD in Milestone 2)

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
    >>> calc_resistances([['Electric'], ['Normal'], ['Fire', 'Flying']) 
    {'Normal': 0, 'Fire': 1, 'Water': 0, 'Grass': 2, 'Electric': 1, ...}

    >>> calc_resistances([['Steel', 'Flying']) # Skarmory is doubly resistant to Grass
    {'Normal': 1, 'Fire': 0, 'Water': 0, 'Grass': 2, 'Electric': 0, ...}
    
    """
    # Function code (TBD in Milestone 2)

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
    #team_types = [['Fire'], ['Steel', 'Flying'], ['Grass', 'Ice']]
    if len(team_types) == 0:
        return

    try:
        weakness_df = pd.read_csv("https://raw.githubusercontent.com/zonination/pokemon-chart/master/chart.csv", sep=',', index_col = 0)
    except Exception as ex:
        print("Exception occurred :" + ex)
        return
    
    if isinstance(weakness_df, pd.DataFrame):
        all_types = weakness_df.index.tolist()
        dict = {x: 0 for x in all_types}

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
            
            dict[item] = weakness_counter
    return dict  

# def recommend(current_team):
#     """
#     Given a team of up to 5 pokémon, recommend a 
#     pokémon that could be added to the 
#     current team to make its weaknesses and 
#     resistances more balanced.

#     This function first determines which types the 
#     team is most weak to and which types the team is 
#     most resistant to via `calc_resistances` and 
#     `calc_weaknesses`, and then makes its recommendation 
#     based on this information.

#     Parameters
#     ----------
#     current_team : list of strings
#         list of up to 5 pokémon names

#     Returns
#     -------
#     reccomendation : string 
#         the name of a pokémon that could be added to the input 
#         team to make its weaknesses and resistances more balanced.

#     Example
#     --------
#     >>> recommend(['Pikachu', 'Eevee', 'Charizard', ...]) 
#     "Lucario"  
#     """
#     # Function code (TBD in Milestone 2)
    
#     # Basic outline:
        
#     team_types = get_types(current_team)
#     current_resistances = calc_resistances(team_types)
#     current_weaknesses = calc_weaknesses(team_types)
    
#     current_balance = calc_balance(current_resistances, current_weaknesses)
#     best_balance = current_balance

#     pokemon_df = pd.read_csv('data/pokemon.csv')


#     # for each new_pokemon in pokemon_df:
#         # get the type(s) `new_pokemon`, call it `pkmn_type`
#         pkmn_resistances = calc_resistances(pkmn_type)
#         pkmn_weaknesses = calc_weaknesses(pkmn_type)

#         # add the new pokemon's resistances to the current team's resistances
#         new_resistances = defaultdict(int)
#         for d in (current_resistances, new_resistances):
#             for type, val in d.items():
#                 new_resistances[type] += val

#         # add the new pokemon's weaknesses to the current team's weaknesses
#         new_weaknesses = defaultdict(int)
#         for d in (current_weaknesses, new_weaknesses):
#             for type, val in d.items():
#                 new_weaknesses[type] += val

#         new_balance = calc_balance(new_resistances, new_weaknesses)
#         if new_balance > best_balance:
#             recommendation = new_pokemon

#     return recommendation

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

    # Code TBD
    