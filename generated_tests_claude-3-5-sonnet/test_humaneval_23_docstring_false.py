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
from typing import Any

@pytest.mark.parametrize("test_input,expected", [
    ("", 0),
    ("a", 1),
    ("abc", 3),
    ("Hello, World!", 13),
    (" ", 1),
    ("    ", 4),
    ("!@#$%^&*()", 10),
    ("Mixed 123 String!", 17),
    ("新年快乐", 4),
    ("🌟✨🌙", 3),
])
def test_strlen_valid_inputs(test_input: str, expected: int) -> None:
    assert strlen(test_input) == expected

def test_strlen_none_input() -> None:
    with pytest.raises(TypeError):
        strlen(None)

def test_strlen_non_string_input() -> None:
    with pytest.raises(TypeError):
        strlen(123)
    with pytest.raises(TypeError):
        strlen(['a', 'b', 'c'])
    with pytest.raises(TypeError):
        strlen({'key': 'value'})

def test_strlen_very_long_string() -> None:
    long_string = "a" * 1000000
    assert strlen(long_string) == 1000000

def test_strlen_special_chars() -> None:
    assert strlen("\n\t\r") == 3
    assert strlen("\u0000") == 1