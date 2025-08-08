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

@pytest.mark.parametrize("input_str,expected", [
    ("Hello World", "hELLO wORLD"),
    ("PYTHON", "python"),
    ("123AbC", "123aBc"),
    ("!@#$%^&*", "!@#$%^&*"),
    ("   spaces   ", "   SPACES   ")
])
def test_flip_case_normal_cases(input_str, expected):
    assert flip_case(input_str) == expected

def test_flip_case_non_string_input():
    with pytest.raises(TypeError):
        flip_case(123)

def flip_case(string: str) -> str:
    return string.swapcase()