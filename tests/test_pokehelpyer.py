from pokehelpyer.pokehelpyer import calc_weaknesses

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
