from pokehelpyer.pokehelpyer import get_types
from pokehelpyer.pokehelpyer import calc_resistances

def test_get_types():
    """Test get_types function returns correct result for different inputs."""
    assert get_types(["RaICHu", "zubAt"]) == [["Electric"], ["Poison", "Flying"]], "Not able to handle improper capitalization"
    assert get_types(["Snorlax!!", "...Chingling"]) == [["Normal"], ["Psychic"]], "Not able to handle improper punctuation"
    assert get_types(["Mime Jr.", "Porygon-Z", "Nidoran♀"]) == [["Psychic", "Fairy"], ["Normal"], ["Poison"]], "Not able to handle Pokemon with symbol in the name"

def test_calc_resistances():
    """Test calc_resistances functionality."""
    assert sum(calc_resistances([["Normal"]]).values()) == 4, "Pokemon type does not add 4 points for immunity"
    assert calc_resistances([['Steel', 'Flying']])['Grass'] == 2, "Pokemon type does not add 2 points for double resistance"
    assert sum(calc_resistances([['Dark', 'Fairy']]).values()) == 13, "Combination of immunity, double resistance or single resistance not being calculated properly"
    