from pokehelpyer.pokehelpyer import (
    get_types,
    calc_weaknesses,
    calc_resistances,
    recommend,
    calc_balance,
)


# get_types:


def test_get_types():
    """Test get_types function returns correct result for different inputs."""
    assert get_types(["RaICHu", "zubAt"]) == [
        ["Electric"],
        ["Poison", "Flying"],
    ], "Not able to handle improper capitalization"
    assert get_types(["Snorlax!!", "...Chingling"]) == [
        ["Normal"],
        ["Psychic"],
    ], "Not able to handle improper punctuation"
    assert get_types(["Mime Jr.", "Porygon-Z", "Nidoran♀"]) == [
        ["Psychic", "Fairy"],
        ["Normal"],
        ["Poison"],
    ], "Not able to handle Pokemon with symbol in the name"


# calc_weaknesses:


def test_calc_weaknesses_valid_result():
    """Tests the calculate weaknesses function for valid output/positive testcase"""
    input_list = [["Fire"], ["Steel", "Flying"], ["Grass", "Ice"]]
    actual_dict = calc_weaknesses(input_list)
    expected_dict = {
        "Normal": 0,
        "Fire": 3,
        "Water": 1,
        "Electric": 1,
        "Grass": 0,
        "Ice": 0,
        "Fighting": 1,
        "Poison": 1,
        "Ground": 1,
        "Flying": 1,
        "Psychic": 0,
        "Bug": 1,
        "Rock": 2,
        "Ghost": 0,
        "Dragon": 0,
        "Dark": 0,
        "Steel": 1,
        "Fairy": 0,
    }
    assert actual_dict == expected_dict
    assert isinstance(actual_dict, dict)


def test_calc_weaknesses_invalid_result():
    """Tests the calculate weaknesses function for negative testcase"""
    actual_dict = calc_weaknesses([["Steel", "Flying"], ["Grass", "Ice"]])
    expected_dict = {
        "Normal": 0,
        "Fire": 0,
        "Water": 1,
        "Electric": 1,
        "Grass": 0,
        "Ice": 0,
        "Fighting": 1,
        "Poison": 1,
        "Ground": 1,
        "Flying": 1,
        "Psychic": 0,
        "Bug": 1,
        "Rock": 2,
        "Ghost": 0,
        "Dragon": 0,
        "Dark": 0,
        "Steel": 1,
        "Fairy": 0,
    }
    assert actual_dict != expected_dict


def test_calc_weaknesses_invalid_input():
    """Tests the calculate weaknesses function for empty inputs"""
    actual_val = calc_weaknesses([])
    assert actual_val == None
    actual_val = calc_weaknesses([[], []])
    assert actual_val == None


# calc_resistances:


def test_calc_resistances():
    """Test calc_resistances functionality."""
    assert (
        sum(calc_resistances([["Normal"]]).values()) == 3
    ), "Pokemon type does not add 3 points for immunity"
    assert (
        calc_resistances([["Steel", "Flying"]])["Grass"] == 2
    ), "Pokemon type does not add 2 points for double resistance"
    assert (
        sum(calc_resistances([["Dark", "Fairy"]]).values())
        == 3 + 3 + 2 + 1
    ), "Combination of immunity, double resistance or single resistance not being calculated properly"


# recommend:


def test_recommend():
    """Test `recommend` returns the correct type of output."""
    actual = recommend(
        ["Pikachu", "Charizard"], n_recommendations=1, early_stop=False
    )  #  Do a full run for one test. Early stop for the rest.
    assert isinstance(
        actual, str
    ), "recommend with n_recommendations=1 should return a string."

    n = 3
    actual = recommend(
        ["Pikachu", "Charizard"], n_recommendations=n, early_stop=True
    )
    assert isinstance(
        actual, list
    ), "recommend with n_recommendations > 1 should return a list of strings."
    assert isinstance(
        actual[0], str
    ), "recommend with n_recommendations > 1 should return a list of strings."
    assert (
        len(actual) == n
    ), "recommend with n_recommendations > 1 should return a list of strings with length equal to n_recommendations."

    """Test `recommend` deals with errorneous user input in the case of a team with only one pokémon."""
    actual = recommend("Pikachu", early_stop=True)
    expected = recommend(["Pikachu"], early_stop=True)
    assert actual == expected


# calc_balance:


def test_calc_balance():
    zero_resistances = {
        "Normal": 0,
        "Fire": 0,
        "Water": 0,
        "Electric": 0,
        "Grass": 0,
        "Ice": 0,
        "Fighting": 0,
        "Poison": 0,
        "Ground": 0,
        "Flying": 0,
        "Psychic": 0,
        "Bug": 0,
        "Rock": 0,
        "Ghost": 0,
        "Dragon": 0,
        "Dark": 0,
        "Steel": 0,
        "Fairy": 0,
    }
    zero_weaknesses = zero_resistances
    fire_water_resistances = {
        "Normal": 0,
        "Fire": 1,
        "Water": 1,
        "Electric": 0,
        "Grass": 0,
        "Ice": 0,
        "Fighting": 0,
        "Poison": 0,
        "Ground": 0,
        "Flying": 0,
        "Psychic": 0,
        "Bug": 0,
        "Rock": 0,
        "Ghost": 0,
        "Dragon": 0,
        "Dark": 0,
        "Steel": 0,
        "Fairy": 0,
    }
    fire_water_weaknesses = fire_water_resistances
    all_resistances = {
        "Normal": 1,
        "Fire": 1,
        "Water": 1,
        "Electric": 1,
        "Grass": 1,
        "Ice": 1,
        "Fighting": 1,
        "Poison": 1,
        "Ground": 1,
        "Flying": 1,
        "Psychic": 1,
        "Bug": 1,
        "Rock": 1,
        "Ghost": 1,
        "Dragon": 1,
        "Dark": 1,
        "Steel": 1,
        "Fairy": 1,
    }
    all_weaknesses = all_resistances

    """Test `calc_balance` returns a float."""
    assert isinstance(
        calc_balance(
            zero_resistances,
            zero_weaknesses,
        ),
        float,
    ), "calc_balance should return a float."
    assert isinstance(
        calc_balance(fire_water_resistances, fire_water_weaknesses), float
    ), "calc_balance should return a float."

    """Test `calc_balance` returns reasonable values."""
    assert (
        calc_balance(zero_resistances, zero_weaknesses) == 0
    ), "calc_balance should return zero for a team with no resistances nor weaknesses."
    assert (
        calc_balance(fire_water_resistances, fire_water_weaknesses) == 0
    ), "calc_balance should return zero for a team with equal and opposite resistances and weaknesses."
    assert (
        calc_balance(fire_water_resistances, zero_weaknesses) > 0
    ), "calc_balance should return a positive number for a team with resistances and no weaknesses."
    assert calc_balance(all_resistances, zero_weaknesses) > calc_balance(
        fire_water_resistances, zero_weaknesses
    ), "calc_balance should return higher numbers for teams with more resistances."
    assert (
        calc_balance(zero_resistances, fire_water_weaknesses) < 0
    ), "calc_balance should return a negative number for a team with weaknesses and no resistances."
    assert calc_balance(zero_resistances, all_weaknesses) < calc_balance(
        zero_resistances, fire_water_weaknesses
    ), "calc_balance should return lower numbers for teams with more weaknesses."
