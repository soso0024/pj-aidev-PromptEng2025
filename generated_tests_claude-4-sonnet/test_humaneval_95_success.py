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

def test_empty_dict():
    assert check_dict_case({}) == False

def test_single_uppercase_key():
    assert check_dict_case({"A": 1}) == True

def test_single_lowercase_key():
    assert check_dict_case({"a": 1}) == True

def test_multiple_uppercase_keys():
    assert check_dict_case({"A": 1, "B": 2, "C": 3}) == True

def test_multiple_lowercase_keys():
    assert check_dict_case({"a": 1, "b": 2, "c": 3}) == True

def test_mixed_case_keys():
    assert check_dict_case({"A": 1, "b": 2}) == False

def test_mixed_case_keys_reverse():
    assert check_dict_case({"a": 1, "B": 2}) == False

def test_non_string_keys():
    assert check_dict_case({1: "a", 2: "b"}) == False

def test_mixed_string_and_non_string_keys():
    assert check_dict_case({"A": 1, 2: "b"}) == False

def test_mixed_string_and_non_string_keys_lowercase():
    assert check_dict_case({"a": 1, 2: "b"}) == False

def test_single_non_string_key():
    assert check_dict_case({1: "value"}) == False

def test_keys_with_numbers_uppercase():
    assert check_dict_case({"A1": 1, "B2": 2}) == True

def test_keys_with_numbers_lowercase():
    assert check_dict_case({"a1": 1, "b2": 2}) == True

def test_keys_with_mixed_alphanumeric():
    assert check_dict_case({"A1": 1, "b2": 2}) == False

def test_empty_string_key():
    assert check_dict_case({"": 1}) == False

def test_empty_string_with_uppercase():
    assert check_dict_case({"": 1, "A": 2}) == False

def test_empty_string_with_lowercase():
    assert check_dict_case({"": 1, "a": 2}) == False

def test_special_characters_uppercase():
    assert check_dict_case({"A_": 1, "B_": 2}) == True

def test_special_characters_lowercase():
    assert check_dict_case({"a_": 1, "b_": 2}) == True

def test_single_character_uppercase():
    assert check_dict_case({"X": 1}) == True

def test_single_character_lowercase():
    assert check_dict_case({"x": 1}) == True

def test_numeric_string_keys():
    assert check_dict_case({"1": 1, "2": 2}) == False

def test_mixed_numeric_and_uppercase():
    assert check_dict_case({"1": 1, "A": 2}) == False

def test_mixed_numeric_and_lowercase():
    assert check_dict_case({"1": 1, "a": 2}) == False

def test_boolean_keys():
    assert check_dict_case({True: 1, False: 2}) == False

def test_none_key():
    assert check_dict_case({None: 1}) == False

def test_float_keys():
    assert check_dict_case({1.5: "a", 2.5: "b"}) == False