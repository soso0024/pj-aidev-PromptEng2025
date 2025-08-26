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
    assert circular_shift(12345, 2) == '45123'
    assert circular_shift(54321, 3) == '32154'

def test_circular_shift_zero_shift():
    assert circular_shift(12345, 0) == '12345'

def test_circular_shift_full_length_shift():
    assert circular_shift(12345, 5) == '12345'

def test_circular_shift_longer_than_length():
    assert circular_shift(12345, 6) == '54321'

def test_circular_shift_negative_number():
    assert circular_shift(-12345, 2) == '45-123'

@pytest.mark.parametrize("x,shift,expected", [
    (12345, 1, '51234'),
    (12345, 4, '23451'),
    (54321, 2, '21543'),
    (100, 2, '001'),
    (9, 3, '9')
])
def test_circular_shift_parametrized(x, shift, expected):
    assert circular_shift(x, shift) == expected

def test_circular_shift_single_digit():
    assert circular_shift(7, 1) == '7'

def test_circular_shift_zero():
    assert circular_shift(0, 2) == '0'