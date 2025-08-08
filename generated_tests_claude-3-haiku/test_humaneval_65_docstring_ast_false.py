# Test cases for HumanEval/65
# Generated using Claude API


def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


# Generated test cases:
from functools import partial
import pytest

@pytest.mark.parametrize("x, shift, expected", [
    (12, 1, "21"),
    (12, 2, "12"),
    (123, 1, "312"),
    (123, 2, "231"),
    (123, 3, "123"),
    (123, 4, "321"),
    (0, 1, "0"),
    (1, 1, "1"),
    (1, 2, "1"),
    (-12, 1, "-12"),
    (12345, 5, "12345"),
    (12345, 6, "54321"),
])
def test_circular_shift(x, shift, expected):
    assert circular_shift(x, shift) == expected

def test_circular_shift_empty_input():
    with pytest.raises(TypeError):
        circular_shift(None, 1)

def test_circular_shift_negative_shift():
    with pytest.raises(ValueError):
        circular_shift(12, -1)