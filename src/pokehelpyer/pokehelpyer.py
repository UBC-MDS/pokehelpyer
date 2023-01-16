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
    