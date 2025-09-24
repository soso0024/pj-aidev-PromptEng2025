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

def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

def test_circular_shift_basic_cases():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"

def test_circular_shift_single_digit():
    assert circular_shift(5, 1) == "5"
    assert circular_shift(5, 0) == "5"
    assert circular_shift(5, 2) == "5"

def test_circular_shift_zero():
    assert circular_shift(0, 1) == "0"
    assert circular_shift(0, 0) == "0"
    assert circular_shift(0, 5) == "0"

def test_circular_shift_no_shift():
    assert circular_shift(123, 0) == "123"
    assert circular_shift(9876, 0) == "9876"

def test_circular_shift_full_rotation():
    assert circular_shift(123, 3) == "123"
    assert circular_shift(1234, 4) == "1234"

def test_circular_shift_multiple_rotations():
    assert circular_shift(123, 6) == "321"
    assert circular_shift(1234, 8) == "4321"

def test_circular_shift_shift_greater_than_digits():
    assert circular_shift(123, 4) == "321"
    assert circular_shift(1234, 5) == "4321"
    assert circular_shift(12, 3) == "21"

def test_circular_shift_large_numbers():
    assert circular_shift(123456789, 1) == "912345678"
    assert circular_shift(123456789, 3) == "789123456"
    assert circular_shift(123456789, 9) == "123456789"

def test_circular_shift_negative_numbers():
    assert circular_shift(-123, 1) == "3-12"
    assert circular_shift(-123, 2) == "23-1"
    assert circular_shift(-123, 4) == "321-"
    assert circular_shift(-1, 1) == "1-"
    assert circular_shift(-1, 2) == "-1"

@pytest.mark.parametrize("x,shift,expected", [
    (12, 1, "21"),
    (12, 2, "12"),
    (123, 1, "312"),
    (123, 2, "231"),
    (1234, 1, "4123"),
    (1234, 2, "3412"),
    (1234, 3, "2341"),
    (5, 10, "5"),
    (789, 5, "987")
])
def test_circular_shift_parametrized(x, shift, expected):
    assert circular_shift(x, shift) == expected

def test_circular_shift_edge_cases():
    assert circular_shift(10, 1) == "01"
    assert circular_shift(100, 1) == "010"
    assert circular_shift(1000, 2) == "0010"