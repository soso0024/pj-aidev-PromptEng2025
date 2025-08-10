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
from circular_shift import circular_shift
import pytest

@pytest.mark.parametrize("x, shift, expected", [
    (123, 1, "321"),
    (123, 2, "231"),
    (123, 3, "123"),
    (123, 4, "321"),
    (123, 5, "231"),
    (123, 6, "123"),
    (123, 7, "321"),
    (123, 8, "231"),
    (123, 9, "123"),
    (0, 1, "0"),
    (0, 2, "0"),
    (0, 3, "0"),
    (-123, 1, "-321"),
    (-123, 2, "-231"),
    (-123, 3, "-123"),
    ("123", 1, "321"),
    ("123", 2, "231"),
    ("123", 3, "123"),
    ("abc", 1, "cab"),
    ("abc", 2, "bca"),
    ("abc", 3, "abc"),
    ("abc", 4, "cab"),
    ("abc", 5, "bca"),
    ("abc", 6, "abc"),
    ("", 1, ""),
    ("", 2, ""),
    ("", 3, ""),
])
def test_circular_shift(x, shift, expected):
    assert circular_shift(x, shift) == expected

@pytest.mark.parametrize("x, shift", [
    (123, -1),
    (123, -2),
    (123, -3),
    (0, -1),
    (0, -2),
    (0, -3),
    (-123, -1),
    (-123, -2),
    (-123, -3),
    ("abc", -1),
    ("abc", -2),
    ("abc", -3),
])
def test_circular_shift_negative_shift(x, shift):
    with pytest.raises(ValueError):
        circular_shift(x, shift)