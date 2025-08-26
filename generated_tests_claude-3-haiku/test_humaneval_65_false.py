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

def test_circular_shift_normal_cases():
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(54321, 4) == "21543"
    assert circular_shift(1, 1) == "1"
    assert circular_shift(123, 3) == "123"

def test_circular_shift_edge_cases():
    assert circular_shift(12345, 5) == "12345"
    assert circular_shift(12345, 6) == "12345"
    assert circular_shift(12345, 0) == "12345"
    assert circular_shift(1, 0) == "1"

def test_circular_shift_negative_shift():
    assert circular_shift(12345, -2) == "45123"
    assert circular_shift(54321, -4) == "21543"
    assert circular_shift(1, -1) == "1"
    assert circular_shift(123, -3) == "123"

def test_circular_shift_string_input():
    assert circular_shift("12345", 2) == "45123"
    assert circular_shift("54321", 4) == "21543"
    assert circular_shift("1", 1) == "1"
    assert circular_shift("123", 3) == "123"

def test_circular_shift_zero_input():
    assert circular_shift(0, 2) == "0"
    assert circular_shift(0, 0) == "0"

def test_circular_shift_negative_input():
    assert circular_shift(-12345, 2) == "-12345"
    assert circular_shift(-54321, 4) == "-54321"

def test_circular_shift_large_shift():
    assert circular_shift(12345, 100) == "12345"
    assert circular_shift(54321, 1000) == "54321"

def test_circular_shift_invalid_input():
    with pytest.raises(TypeError):
        circular_shift(None, 2)
    with pytest.raises(TypeError):
        circular_shift([1, 2, 3], 2)