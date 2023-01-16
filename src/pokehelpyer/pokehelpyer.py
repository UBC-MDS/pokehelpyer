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

def calc_resistance(team_list):
    """
    Given a list of pokémon types, determine how many types in the list 
    are resistant to each type in the game.
    
    Creates a dictionary in which the keys are each of the 18 types 
    in the game, and the values are integers ranging 
    from 0 to the length of the input list of types.
    The values indicate the number of types in the 
    input list that are resistant to each key (type). 

    Parameters
    ----------
    team_list : list
        the list of pokémon types associated to the user's team

    Returns
    -------
    resistances : dictionary 
        a dictionary containing all pokémon types as keys, 
        and the number of types in the input list resistant to
        each key (type) as values.

    Example
    --------
    >>> calc_resistances(['Electric', 'Normal', 'Fire']) 
    {'Normal': 0, 'Fire': 1, 'Water': 0, 'Steel': 2, ...}
    
    """
    # Function code (TBD in Milestone 2)

def calc_weaknesses(team_list):
    """
    Given a list of pokémon types, determine how many types in the list 
    are weak to each type in the game.
    
    Creates a dictionary in which the keys are each of the 18 types 
    in the game, and the values are integers ranging 
    from 0 to the length of the input list of types.
    The values indicate the number of types in the 
    input list that are weak to each key (type). 

    Parameters
    ----------
    team_list : list
        the list of Pokemon types associated to the user's team

    Returns
    -------
    weaknesses : dictionary 
        a dictionary containing all pokémon types as keys, 
        and the number of types in the input list resistant to
        each key (type) as values.

    Example
    --------
    >>> calc_weaknesses(['Ice', 'Grass']) 
    {'Bug': 1, 'Fire': 2, 'Rock': 1, 'Grass': 0, ...}
    
    """

    # Function code (TBD in Milestone 2)

def recommend(current_team):
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
    current_team : list
        list of up to 5 pokémon names

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
    # Function code (TBD in Milestone 2)
    