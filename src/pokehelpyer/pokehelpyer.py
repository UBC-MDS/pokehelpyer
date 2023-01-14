def calc_resistance(team):
    """
    Given a list of Pokemon types (based on the team provided by the user), 
    calculates all the Pokemon types to which the team provided is resistant to.

    Parameters
    ----------
    team : list
        the list of Pokemon types associated to the user's team

    Returns
    -------
    resistant : dictionary 
        a dictionary containing all Pokemon types as keys, 
        and the number of Pokemons resistant to each type as value.

    Example
    --------
    >>> calc_resistance(['Electric', 'Grass', 'Fighting', 'Poison', 'Ground']) 
    {'Normal': 0, 'Fire': 0, 'Water': 1, 'Electric': 2, 'Grass': 2, 'Ice': 1, ...}
    
    """
    # Function code (Due to Milestone 2)

def calc_weaknesses(team_list):
    """
    Given a list of Pokemon types, calculates the total number of types
    from the team list (based on the team provided by the user), which is weak
    against each of the pokemon type in the game.

    Parameters
    ----------
    team_list : list
        the list of Pokemon types associated with the user's team

    Returns
    -------
    weaknesses : dictionary 
        a dictionary containing all Pokemon types as keys 
        and the number of Pokemons weak against each type as values.

    Example
    --------
    >>> calc_weaknesses(['Ice', 'Grass']) 
    {'Bug': 1, 'Fire': 2, 'Rock': 1, 'Grass': 0, ...}
    
    """

    # Function code (TBD in Milestone 2)