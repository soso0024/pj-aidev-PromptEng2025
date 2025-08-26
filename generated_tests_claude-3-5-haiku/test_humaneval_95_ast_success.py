# Test cases for HumanEval/95
# Generated using Claude API


def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """

    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower" 


# Generated test cases:
import pytest

def check_dict_case(dict):
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():
            if not isinstance(key, str):
                return False
            if not key.isalpha():
                return False
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    return False
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                return False
        return state == "upper" or state == "lower"

def test_check_dict_case_empty_dict():
    assert check_dict_case({}) == False

def test_check_dict_case_all_uppercase():
    assert check_dict_case({"A": 1, "B": 2, "C": 3}) == True

def test_check_dict_case_all_lowercase():
    assert check_dict_case({"a": 1, "b": 2, "c": 3}) == True

def test_check_dict_case_mixed_case():
    assert check_dict_case({"A": 1, "b": 2, "C": 3}) == False

def test_check_dict_case_non_string_keys():
    assert check_dict_case({1: "a", 2: "b"}) == False

@pytest.mark.parametrize("test_input,expected", [
    ({"HELLO": 1, "WORLD": 2}, True),
    ({"hello": 1, "world": 2}, True),
    ({"Hello": 1, "World": 2}, False),
    ({"HELLO": 1, "world": 2}, False),
    ({}, False),
    ({1: "a", 2: "b"}, False),
    ({"A1": 1, "B2": 2}, False),
    ({"a1": 1, "b2": 2}, False)
])
def test_check_dict_case_parametrized(test_input, expected):
    assert check_dict_case(test_input) == expected

def test_check_dict_case_single_key_uppercase():
    assert check_dict_case({"A": 1}) == True

def test_check_dict_case_single_key_lowercase():
    assert check_dict_case({"a": 1}) == True

def test_check_dict_case_complex_keys():
    assert check_dict_case({"A_B_C": 1, "D_E_F": 2}) == False