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
from your_module import check_dict_case

import pytest

@pytest.mark.parametrize("input_dict,expected", [
    ({"a":"apple", "b":"banana"}, True),
    ({"a":"apple", "A":"banana", "B":"banana"}, False),
    ({"a":"apple", 8:"banana", "a":"apple"}, False),
    ({"Name":"John", "Age":"36", "City":"Houston"}, False),
    ({"STATE":"NC", "ZIP":"12345"}, True),
    ({}, False),
    ({"a":"apple", "B":"banana"}, False),
    ({"A":"apple", "b":"banana"}, False),
    ({"a":"apple", "b":"banana", "C":"cherry"}, True),
    ({"A":"apple", "B":"banana", "C":"cherry"}, True)
])
def test_check_dict_case(input_dict, expected):
    assert check_dict_case(input_dict) == expected