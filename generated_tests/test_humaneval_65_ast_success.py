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
    assert circular_shift(1, 2) == "1"

@pytest.mark.parametrize("number,shift,expected", [
    (12345, 2, "45123"),
    (67890, 3, "89067"),
    (1, 1, "1"),
    (123, 5, "321"),
    (1000, 2, "0010"),
    (999, 1, "999"),
    (54321, 0, "54321"),
])
def test_circular_shift_parametrized(number, shift, expected):
    assert circular_shift(number, shift) == expected

def test_circular_shift_zero_number():
    assert circular_shift(0, 1) == "0"
    assert circular_shift(0, 2) == "0"

def test_circular_shift_negative_number():
    assert circular_shift(-123, 1) == "3-12"
    assert circular_shift(-123, 4) == "-123"

def test_circular_shift_large_numbers():
    assert circular_shift(1000000, 3) == "0001000"
    assert circular_shift(9999999, 4) == "9999999"

def test_circular_shift_special_cases():
    assert circular_shift(101010, 3) == "010101"
    assert circular_shift(111111, 2) == "111111"
    assert circular_shift(100100, 6) == "100100"