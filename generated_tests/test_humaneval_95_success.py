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

def test_empty_dict():
    assert check_dict_case({}) == False

def test_single_uppercase_key():
    assert check_dict_case({"HELLO": 1}) == True

def test_single_lowercase_key():
    assert check_dict_case({"hello": 1}) == True

def test_mixed_case_keys():
    assert check_dict_case({"HELLO": 1, "world": 2}) == False

def test_all_uppercase_keys():
    assert check_dict_case({"HELLO": 1, "WORLD": 2, "TEST": 3}) == True

def test_all_lowercase_keys():
    assert check_dict_case({"hello": 1, "world": 2, "test": 3}) == True

def test_non_string_keys():
    assert check_dict_case({1: "test", 2: "hello"}) == False

def test_mixed_type_keys():
    assert check_dict_case({"HELLO": 1, 2: "world"}) == False

@pytest.mark.parametrize("test_dict,expected", [
    ({"ABC": 1, "DEF": 2}, True),
    ({"abc": 1, "def": 2}, True),
    ({"ABC": 1, "def": 2}, False),
    ({"Hello": 1}, False),
    ({"HELLO123": 1}, True),
    ({"hello123": 1}, True),
    ({" ": 1}, False),
    ({"!@#": 1}, False),
    ({"ABC": 1, 123: 2}, False),
    ({True: 1, False: 2}, False)
])
def test_various_cases(test_dict, expected):
    assert check_dict_case(test_dict) == expected

def test_special_characters():
    assert check_dict_case({"HELLO!": 1, "WORLD@": 2}) == True
    assert check_dict_case({"hello!": 1, "world@": 2}) == True

def test_numbers_in_strings():
    assert check_dict_case({"TEST123": 1, "ABC456": 2}) == True
    assert check_dict_case({"test123": 1, "abc456": 2}) == True

def test_single_character_keys():
    assert check_dict_case({"A": 1, "B": 2}) == True
    assert check_dict_case({"a": 1, "b": 2}) == True

def test_whitespace_keys():
    assert check_dict_case({"HELLO WORLD": 1}) == True
    assert check_dict_case({"hello world": 1}) == True
