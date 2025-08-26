# Test cases for HumanEval/23
# Generated using Claude API



def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    return len(string)


# Generated test cases:
import pytest

def test_strlen_empty_string():
    assert strlen("") == 0

def test_strlen_single_character():
    assert strlen("a") == 1

def test_strlen_multiple_characters():
    assert strlen("hello world") == 11

@pytest.mark.parametrize("input,expected", [
    ("", 0),
    ("a", 1),
    ("hello", 5),
    ("   ", 3),
    ("123456789", 9)
])
def test_strlen_parametrized(input, expected):
    assert strlen(input) == expected

def test_strlen_non_string_input():
    with pytest.raises(TypeError):
        strlen(123)
