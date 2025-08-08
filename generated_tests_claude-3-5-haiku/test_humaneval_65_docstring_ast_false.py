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
    assert circular_shift(5, 2) == "5"

@pytest.mark.parametrize("x,shift,expected", [
    (12, 0, "12"),
    (123, 0, "123"),
    (1234, 0, "1234")
])
def test_circular_shift_zero_shift(x, shift, expected):
    assert circular_shift(x, shift) == expected

@pytest.mark.parametrize("x,shift,expected", [
    (12, 3, "21"),
    (123, 4, "321"),
    (1234, 5, "4321")
])
def test_circular_shift_larger_than_digits(x, shift, expected):
    assert circular_shift(x, shift) == expected

def test_circular_shift_large_number():
    assert circular_shift(987654321, 3) == "321987654"

def test_circular_shift_negative_number():
    assert circular_shift(-12, 1) == "-21"