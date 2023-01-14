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
    calc_resistance([]) 
    """
    # Function code (Due to Milestone 2)