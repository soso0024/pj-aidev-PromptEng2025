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

def test_single_lower():
    assert check_dict_case({"a": "apple"}) == True

def test_single_upper():
    assert check_dict_case({"A": "apple"}) == True

def test_multiple_lower():
    assert check_dict_case({"a": "apple", "b": "banana", "c": "cherry"}) == True

def test_multiple_upper():
    assert check_dict_case({"ABC": "test", "DEF": "test", "GHI": "test"}) == True

def test_mixed_case():
    assert check_dict_case({"a": "apple", "B": "banana"}) == False

def test_non_string_keys():
    assert check_dict_case({1: "one", 2: "two"}) == False

def test_mixed_type_keys():
    assert check_dict_case({"a": "apple", 1: "one"}) == False

@pytest.mark.parametrize("test_input,expected", [
    ({"hello": "world", "python": "test"}, True),
    ({"HELLO": "WORLD", "PYTHON": "TEST"}, True),
    ({"Hello": "World", "Python": "Test"}, False),
    ({"a": 1, "b": 2, "C": 3}, False),
    ({"name": "John", "AGE": "30"}, False),
    ({"STATE": "NC", "ZIP": "12345"}, True),
    ({"state": "nc", "zip": "12345"}, True),
    ({" ": "space"}, False),
    ({"a": "", "b": ""}, True),
    ({"A": None, "B": None}, True)
])
def test_parametrized_cases(test_input, expected):
    result = check_dict_case(test_input)
    assert result == expected, f"Expected {expected} but got {result} for input {test_input}"

def test_special_characters():
    assert check_dict_case({"@": "at", "#": "hash"}) == False

def test_unicode_characters():
    assert check_dict_case({"α": "alpha", "β": "beta"}) == True

def test_whitespace_keys():
    assert check_dict_case({"a b": "space", "c d": "space"}) == False

def test_empty_string_keys():
    assert check_dict_case({"": "empty"}) == False

def test_large_dict():
    large_dict = {chr(i): str(i) for i in range(97, 123)}  # a-z
    assert check_dict_case(large_dict) == True

def test_single_char_upper():
    assert check_dict_case({"A": 1}) == True

def test_single_char_lower():
    assert check_dict_case({"a": 1}) == True

def test_numeric_string_keys():
    assert check_dict_case({"123": "num", "456": "num"}) == False