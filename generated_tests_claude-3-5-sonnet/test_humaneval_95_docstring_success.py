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

def test_check_dict_case_empty():
    assert check_dict_case({}) == False

def test_check_dict_case_single_lower():
    assert check_dict_case({"a": "apple"}) == True

def test_check_dict_case_single_upper():
    assert check_dict_case({"A": "apple"}) == True

@pytest.mark.parametrize("test_dict,expected", [
    ({"a": "apple", "b": "banana"}, True),
    ({"A": "APPLE", "B": "BANANA"}, True),
    ({"STATE": "NC", "ZIP": "12345"}, True),
    ({"a": "apple", "A": "banana"}, False),
    ({"Name": "John", "Age": "36"}, False),
    ({"a": "apple", 8: "banana"}, False),
    ({"a": "apple", "B": "banana"}, False),
    ({"Hello": "World", "Test": "Case"}, False),
    ({"abc": "test", "DEF": "case"}, False),
    ({"": "empty"}, False),
    ({"a": "", "b": ""}, True),
    ({"A": None, "B": None}, True),
])
def test_check_dict_case_parametrized(test_dict, expected):
    assert check_dict_case(test_dict) == expected

def test_check_dict_case_special_chars():
    assert check_dict_case({"@": "at", "#": "hash"}) == False

def test_check_dict_case_numbers_as_strings():
    assert check_dict_case({"1": "one", "2": "two"}) == False

def test_check_dict_case_mixed_content():
    assert check_dict_case({"lower": 123, "case": True, "test": None}) == True

def test_check_dict_case_whitespace():
    assert check_dict_case({"a b": "space", "c d": "space"}) == True

def test_check_dict_case_single_char_mixed():
    assert check_dict_case({"a": 1, "B": 2}) == False

def test_check_dict_case_unicode():
    assert check_dict_case({"α": "alpha", "β": "beta"}) == True

def test_check_dict_case_large_dict():
    large_dict = {f"test{i}": str(i) for i in range(100)}
    assert check_dict_case(large_dict) == True