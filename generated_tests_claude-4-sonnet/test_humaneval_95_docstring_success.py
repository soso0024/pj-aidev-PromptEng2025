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

@pytest.mark.parametrize("input_dict,expected", [
    ({"a": "apple", "b": "banana"}, True),
    ({"a": "apple", "A": "banana", "B": "banana"}, False),
    ({"a": "apple", 8: "banana", "a": "apple"}, False),
    ({"Name": "John", "Age": "36", "City": "Houston"}, False),
    ({"STATE": "NC", "ZIP": "12345"}, True),
    ({}, False),
    ({"A": "value"}, True),
    ({"a": "value"}, True),
    ({"ABC": "value", "DEF": "value"}, True),
    ({"abc": "value", "def": "value"}, True),
    ({"A": "value", "b": "value"}, False),
    ({"a": "value", "B": "value"}, False),
    ({1: "value", 2: "value"}, False),
    ({"a": "value", 1: "value"}, False),
    ({"A": "value", 1: "value"}, False),
    ({"": "value"}, False),
    ({"A": "value", "": "value"}, False),
    ({"a": "value", "": "value"}, False),
    ({"123": "value", "456": "value"}, False),
    ({"ABC": "value", "123": "value"}, False),
    ({"abc": "value", "123": "value"}, False),
    ({"A1": "value", "B2": "value"}, True),
    ({"a1": "value", "b2": "value"}, True),
    ({None: "value"}, False),
    ({"a": "value", None: "value"}, False),
    ({True: "value"}, False),
    ({False: "value"}, False),
    ({3.14: "value"}, False),
    ({"Aa": "value"}, False),
    ({"aA": "value"}, False),
    ({"AA": "value", "BB": "value", "CC": "value"}, True),
    ({"aa": "value", "bb": "value", "cc": "value"}, True),
    ({"AA": "value", "bb": "value"}, False),
    ({"aa": "value", "BB": "value"}, False)
])
def test_check_dict_case(input_dict, expected):
    assert check_dict_case(input_dict) == expected

def test_empty_dict():
    assert check_dict_case({}) == False

def test_single_lowercase_key():
    assert check_dict_case({"x": "value"}) == True

def test_single_uppercase_key():
    assert check_dict_case({"X": "value"}) == True

def test_mixed_case_single_key():
    assert check_dict_case({"Xx": "value"}) == False

def test_numeric_keys_only():
    assert check_dict_case({1: "one", 2: "two"}) == False

def test_mixed_string_and_numeric_keys():
    assert check_dict_case({"a": "letter", 1: "number"}) == False

def test_all_empty_string_keys():
    assert check_dict_case({"": "empty1"}) == False

def test_special_characters_lowercase():
    assert check_dict_case({"key_1": "value", "key-2": "value"}) == True

def test_special_characters_uppercase():
    assert check_dict_case({"KEY_1": "value", "KEY-2": "value"}) == True

def test_special_characters_mixed():
    assert check_dict_case({"KEY_1": "value", "key-2": "value"}) == False