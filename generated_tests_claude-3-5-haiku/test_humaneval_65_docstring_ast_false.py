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
import pytest

def test_circular_shift_basic_cases():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(1234, 2) == "3412"

@pytest.mark.parametrize("x,shift,expected", [
    (12, 1, "21"),
    (12, 2, "12"),
    (1234, 2, "3412"),
    (5678, 3, "6785"),
    (100, 1, "001"),
    (9, 1, "9"),
    (9, 2, "9")
])
def test_circular_shift_parametrized(x, shift, expected):
    assert circular_shift(x, shift) == expected

def test_circular_shift_large_shift():
    assert circular_shift(123, 5) == "321"
    assert circular_shift(456, 10) == "654"

def test_circular_shift_zero_shift():
    assert circular_shift(789, 0) == "789"

def test_circular_shift_single_digit():
    assert circular_shift(5, 1) == "5"
    assert circular_shift(5, 2) == "5"