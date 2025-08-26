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
    s = str(abs(x))
    if shift >= len(s):
        return s[::-1]
    else:
        return s[shift:] + s[:shift]

def test_circular_shift_basic_cases():
    assert circular_shift(1234, 2) == '3412'
    assert circular_shift(12345, 3) == '45123'
    assert circular_shift(54321, 1) == '15432'

def test_circular_shift_zero_shift():
    assert circular_shift(1234, 0) == '1234'

def test_circular_shift_full_length_shift():
    assert circular_shift(1234, 4) == '4321'

def test_circular_shift_longer_than_length():
    assert circular_shift(1234, 5) == '4321'
    assert circular_shift(5678, 10) == '8765'

def test_circular_shift_negative_input():
    assert circular_shift(-1234, 2) == '3412'

def test_circular_shift_single_digit():
    assert circular_shift(5, 1) == '5'
    assert circular_shift(7, 2) == '7'

@pytest.mark.parametrize("x,shift,expected", [
    (1234, 2, '3412'),
    (54321, 3, '32154'),
    (9876, 1, '6987'),
    (100, 2, '001'),
    (42, 0, '42')
])
def test_circular_shift_parametrized(x, shift, expected):
    assert circular_shift(x, shift) == expected