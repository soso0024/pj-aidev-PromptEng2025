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

def test_flip_case_empty_string():
    assert flip_case("") == ""

@pytest.mark.parametrize("input,expected", [
    ("Hello World", "hELLO wORLD"),
    ("UPPERCASE", "lowercase"),
    ("lowercase", "UPPERCASE"),
    ("MixedCase", "mIXEDcASE"),
    ("123ABC", "123abc"),
    ("abc123", "ABC123"),
    ("1 2 3", "1 2 3")
])
def test_flip_case_normal_cases(input, expected):
    assert flip_case(input) == expected

def test_flip_case_non_string_input():
    with pytest.raises(TypeError):
        flip_case(123)

def test_flip_case_none_input():
    with pytest.raises(TypeError):
        flip_case(None)

def flip_case(string: str) -> str:
    return string.swapcase()