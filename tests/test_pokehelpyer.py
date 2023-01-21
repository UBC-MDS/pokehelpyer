from pokehelpyer.pokehelpyer import get_types
from pokehelpyer.pokehelpyer import calc_weaknesses

def test_get_types():
    """Test get_types function returns correct result for different inputs."""
    assert get_types(["RaICHu", "zubAt"]) == [["Electric"], ["Poison", "Flying"]], "Not able to handle improper capitalization"
    assert get_types(["Snorlax!!", "...Chingling"]) == [["Normal"], ["Psychic"]], "Not able to handle improper punctuation"
    assert get_types(["Mime Jr.", "Porygon-Z", "Nidoran♀"]) == [["Psychic", "Fairy"], ["Normal"], ["Poison"]], "Not able to handle Pokemon with symbol in the name"