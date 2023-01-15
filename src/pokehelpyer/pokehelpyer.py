def add_team_members(pokemon_names):
    """
    Given a list of pokémon names, determine the types of 
    those pokémon using an existing dataset.

    Parameters
    ----------
    pokemon_names : list
        list of pokémon names

    Returns
    -------
    pokemon_types : list 
        list of pokémon types corresponding to 
        the pokémon names in the input list

    Example
    --------
    >>> add_team_memebers(['Pikachu', 'Eevee', 'Charizard', ...]) 
    ['Electric', 'Normal', 'Fire', ...]    
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
