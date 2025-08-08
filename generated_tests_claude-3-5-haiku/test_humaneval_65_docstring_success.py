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

def test_circular_shift_single_digit():
    assert circular_shift(5, 1) == "5"
    assert circular_shift(7, 2) == "7"

def test_circular_shift_large_shift():
    assert circular_shift(123, 4) == "321"
    assert circular_shift(456, 5) == "654"

@pytest.mark.parametrize("x,shift,expected", [
    (12, 1, "21"),
    (12, 2, "12"),
    (1234, 2, "3412"),
    (5, 1, "5"),
    (123, 4, "321"),
    (456, 5, "654"),
    (10, 1, "01"),
    (100, 2, "001")
])
def test_circular_shift_parametrized(x, shift, expected):
    assert circular_shift(x, shift) == expected

def test_circular_shift_zero():
    assert circular_shift(0, 1) == "0"
    assert circular_shift(0, 2) == "0"

def test_circular_shift_negative_number():
    assert circular_shift(-12, 1) == "21"
    assert circular_shift(-1234, 2) == "3412"

def circular_shift(x, shift):
    s = str(abs(x))
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]