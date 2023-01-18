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
    # Check for empty input
    assert len(pokemon_names) != 0, "No names provided"

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
        assert name not in names_types_df["Name"], "Pokemon is not valid"
        
        # Find the row with match
        row = names_types_df.loc[names_types_df["Name"] == name].values[0]
        # Type 2 is optional
        if pd.isna(row[2]):
            poke_types.append([row[1]])
        else:
            poke_types.append([row[1], row[2]])
            
    return poke_types

# def calc_resistances(team_types):
#     """
#     Given a list of pokémon types present on a player's team,
#     calculate a measure of how resistant the team is to each type in the game.
    
#     Creates a dictionary in which the keys are each of the 18 types 
#     in the game, and the values are integers measuring the level of 
#     resistance the input team has to that type. Higher values indicate a
#     higher level of resistance to that type (key).

#     Parameters
#     ----------
#     team_types : list of list of strings
#         list of pokémon types associated to the user's team
#         obtained via `get_types`

#     Returns
#     -------
#     resistances : dictionary 
#         a dictionary containing all 18 pokémon types as keys, 
#         and integers measuring the level of resistance the input team
#         has to that type as values. 

#     Examples
#     --------
#     >>> calc_resistances([['Electric'], ['Normal'], ['Fire', 'Flying']) 
#     {'Normal': 0, 'Fire': 1, 'Water': 0, 'Grass': 2, 'Electric': 1, ...}

#     >>> calc_resistances([['Steel', 'Flying']) # Skarmory is doubly resistant to Grass
#     {'Normal': 1, 'Fire': 0, 'Water': 0, 'Grass': 2, 'Electric': 0, ...}
    
#     """
#     # Function code (TBD in Milestone 2)

# def calc_weaknesses(team_types):
#     """
#     Given a list of pokémon types present on a player's team,
#     calculate a measure of how weak the team is to each type in the game.
    
#     Creates a dictionary in which the keys are each of the 18 types 
#     in the game, and the values are integers measuring the level of 
#     weakness the input team has to that key (type). Higher values indicate a
#     higher level of weakness to that type. 

#     Parameters
#     ----------
#     team_types : list of list of strings
#         list of pokémon types associated to the user's team
#         obtained via `get_types`

#     Returns
#     -------
#     weaknesses : dictionary 
#         a dictionary containing all 18 pokémon types as keys, 
#         and integers measuring the level of weakness the input team
#         has to that type as values. 

#     Examples
#     --------
#     >>> calc_weaknesses([['Electric'], ['Normal'], ['Fire', 'Flying']) 
#     {'Normal': 0, 'Fire': 0, 'Water': 1, 'Grass': 0, 'Electric': 1, ...}

#     >>> calc_weaknesses([['Ice', 'Grass']) # Abomasnow is doubly weak to Fire
#     {'Normal': 0, 'Fire': 2, 'Water': 0, 'Grass': 0, 'Electric': 0, ...}
    
#     """

#     # Function code (TBD in Milestone 2)

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

# def calc_balance(resistances, weaknesses):
#     """
#     Calculate a measure of how balanced a team is using its 
#     weaknesses and resistances.

#     Higher values indicate a more balanced team.

#     Parameters
#     ----------
#     resistances : dictionary
#         obtained from calc_resistances

#     weaknesses : dictionary
#         obtained from calc_weaknesses

#     Returns
#     -------
#     balance : float 
#         measure of how balanced the team is.

#     Example
#     --------
#     TO-DO
#     """

#     # Code TBD
    