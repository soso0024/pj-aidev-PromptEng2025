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
    assert circular_shift(123, 1) == '312'
    assert circular_shift(1234, 0) == '1234'

def test_circular_shift_full_length_shift():
    assert circular_shift(1234, 4) == '1234'

def test_circular_shift_longer_than_length():
    assert circular_shift(1234, 5) == '4321'
    assert circular_shift(5678, 10) == '8765'

def test_circular_shift_negative_input():
    assert circular_shift(-12345, 2) == '45-123'

def test_circular_shift_zero_input():
    assert circular_shift(0, 2) == '0'

@pytest.mark.parametrize("x,shift,expected", [
    (12345, 2, '45123'),
    (123, 1, '312'),
    (1234, 0, '1234'),
    (1234, 4, '1234'),
    (1234, 5, '4321'),
    (-12345, 2, '45-123'),
    (0, 2, '0')
])
def test_circular_shift_parametrized(x, shift, expected):
    assert circular_shift(x, shift) == expected