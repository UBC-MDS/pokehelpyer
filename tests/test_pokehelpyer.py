from pokehelpyer.pokehelpyer import get_types
from pokehelpyer.pokehelpyer import calc_weaknesses

def test_get_types():
    """Test get_types function returns correct result for different inputs."""
    assert get_types(["RaICHu", "zubAt"]) == [["Electric"], ["Poison", "Flying"]], "Not able to handle improper capitalization"
    assert get_types(["Snorlax!!", "...Chingling"]) == [["Normal"], ["Psychic"]], "Not able to handle improper punctuation"
    assert get_types(["Mime Jr.", "Porygon-Z", "Nidoran♀"]) == [["Psychic", "Fairy"], ["Normal"], ["Poison"]], "Not able to handle Pokemon with symbol in the name"

def test_calc_weaknesses_valid_result():
    """Tests the calculate weaknesses function for valid output/positive testcase"""
    input_list = [['Fire'], ['Steel', 'Flying'], ['Grass', 'Ice']]
    actual_dict = calc_weaknesses(input_list)
    expected_dict = {'Normal': 0, 'Fire': 3, 'Water': 1, 'Electric': 1, 'Grass': 0, 'Ice': 0, 'Fighting': 1,
     'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 0, 'Bug': 1, 'Rock': 2, 'Ghost': 0, 'Dragon': 0,
      'Dark': 0, 'Steel': 1, 'Fairy': 0}
    assert actual_dict == expected_dict
    assert isinstance(actual_dict, dict)    

def test_calc_weaknesses_invalid_result():
    """Tests the calculate weaknesses function for negative testcase"""
    actual_dict = calc_weaknesses([['Steel', 'Flying'], ['Grass', 'Ice']])
    expected_dict = {'Normal': 0, 'Fire': 0, 'Water': 1, 'Electric': 1, 'Grass': 0, 'Ice': 0, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 0, 'Bug': 1, 'Rock': 2, 'Ghost': 0, 'Dragon': 0, 'Dark': 0, 'Steel': 1, 'Fairy': 0}
    assert actual_dict != expected_dict

def test_calc_weaknesses_invalid_input_list():
    """Tests the calculate weaknesses function for empty input list"""
    actual_val = calc_weaknesses([])
    assert actual_val == None