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

def test_check_dict_case_lowercase_keys():
    assert check_dict_case({"a": "apple", "b": "banana"}) == True

def test_check_dict_case_uppercase_keys():
    assert check_dict_case({"STATE": "NC", "ZIP": "12345"}) == True

def test_check_dict_case_mixed_case():
    assert check_dict_case({"a": "apple", "A": "banana"}) == False

def test_check_dict_case_non_string_keys():
    assert check_dict_case({"a": "apple", 8: "banana"}) == False

def test_check_dict_case_mixed_case_names():
    assert check_dict_case({"Name": "John", "Age": "36"}) == False

def test_check_dict_case_empty_dict():
    assert check_dict_case({}) == False

@pytest.mark.parametrize("test_input,expected", [
    ({"a": "apple", "b": "banana"}, True),
    ({"STATE": "NC", "ZIP": "12345"}, True),
    ({"a": "apple", "A": "banana"}, False),
    ({"a": "apple", 8: "banana"}, False),
    ({"Name": "John", "Age": "36"}, False),
    ({}, False)
])
def test_check_dict_case_parametrized(test_input, expected):
    assert check_dict_case(test_input) == expected
