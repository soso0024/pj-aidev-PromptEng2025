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
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"

@pytest.mark.parametrize("number, shift, expected", [
    (123, 1, "312"),
    (123, 2, "231"),
    (123, 3, "123"),
    (123, 4, "321"),
    (1234, 1, "4123"),
    (1234, 2, "3412"),
    (1234, 3, "2341"),
    (1234, 4, "1234"),
    (1234, 5, "4321"),
])
def test_circular_shift_parametrized(number, shift, expected):
    assert circular_shift(number, shift) == expected

def test_circular_shift_single_digit():
    assert circular_shift(5, 1) == "5"
    assert circular_shift(5, 2) == "5"
    assert circular_shift(5, 10) == "5"

def test_circular_shift_zero():
    assert circular_shift(0, 1) == "0"
    assert circular_shift(0, 5) == "0"

def test_circular_shift_large_numbers():
    assert circular_shift(123456789, 1) == "912345678"
    assert circular_shift(123456789, 10) == "987654321"

def test_circular_shift_large_shift():
    assert circular_shift(123, 100) == "321"
    assert circular_shift(1234, 1000) == "4321"

def test_circular_shift_leading_zeros():
    assert circular_shift(1001, 1) == "1100"
    assert circular_shift(1001, 5) == "1001"

def test_circular_shift_zero_shift():
    assert circular_shift(12345, 0) == "12345"
    assert circular_shift(0, 0) == "0"

def test_circular_shift_invalid_input():
    with pytest.raises((ValueError, TypeError, AttributeError)):
        circular_shift("abc", 1)
    with pytest.raises((ValueError, TypeError, AttributeError)):
        circular_shift(None, 1)
    with pytest.raises((ValueError, TypeError, AttributeError)):
        circular_shift(3.14, 1)
    with pytest.raises((ValueError, TypeError, AttributeError)):
        circular_shift([], 1)
    with pytest.raises((ValueError, TypeError, AttributeError)):
        circular_shift({}, 1)