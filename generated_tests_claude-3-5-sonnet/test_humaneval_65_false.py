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

def test_circular_shift_basic():
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(12345, 1) == "51234"

def test_circular_shift_zero():
    assert circular_shift(12345, 0) == "12345"

def test_circular_shift_full_length():
    assert circular_shift(12345, 5) == "12345"

def test_circular_shift_greater_than_length():
    assert circular_shift(12345, 6) == "54321"
    assert circular_shift(12345, 10) == "54321"

def test_circular_shift_single_digit():
    assert circular_shift(1, 1) == "1"
    assert circular_shift(1, 5) == "1"

@pytest.mark.parametrize("number,shift,expected", [
    (12345, 2, "45123"),
    (67890, 3, "89067"),
    (1, 1, "1"),
    (22, 1, "22"),
    (123, 5, "321"),
    (1000, 2, "0010"),
    (999999, 3, "999999"),
])
def test_circular_shift_parametrized(number, shift, expected):
    assert circular_shift(number, shift) == expected

def test_circular_shift_large_numbers():
    assert circular_shift(1234567890, 3) == "8901234567"
    assert circular_shift(9999999999, 5) == "9999999999"

def test_circular_shift_with_zeros():
    assert circular_shift(1000, 1) == "0100"
    assert circular_shift(1000, 2) == "0010"

def test_circular_shift_repeated_digits():
    assert circular_shift(111, 1) == "111"
    assert circular_shift(222, 2) == "222"

def test_circular_shift_negative_numbers():
    result = circular_shift(-12345, 2)
    assert result == "-45123"
    result = circular_shift(-1000, 1)
    assert result == "-0100"