# Test cases for HumanEval/27
# Generated using Claude API



def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    return string.swapcase()


# Generated test cases:
import pytest
from solution import flip_case

@pytest.mark.parametrize("input_string,expected_output", [
    ("Hello", "hELLO"),
    ("WORLD", "world"),
    ("aBcDeFg", "AbCdEfG"),
    ("", ""),
    ("123 ABC", "123 abc"),
    ("HeLlO wOrLd", "hElLo WoRlD"),
    ("   SPACES   ", "   spaces   "),
    ("!@#$%^&*()_+", "!@#$%^&*()_+")
])
def test_flip_case(input_string, expected_output):
    assert flip_case(input_string) == expected_output

def test_flip_case_type_error():
    with pytest.raises(TypeError):
        flip_case(123)