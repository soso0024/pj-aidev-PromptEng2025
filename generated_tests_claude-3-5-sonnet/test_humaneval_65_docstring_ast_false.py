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

def test_basic_shift():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"

def test_larger_numbers():
    assert circular_shift(123456, 2) == "561234"
    assert circular_shift(123456, 3) == "456123"

def test_shift_greater_than_length():
    assert circular_shift(123, 4) == "321"
    assert circular_shift(1234, 5) == "4321"

def test_single_digit():
    assert circular_shift(5, 1) == "5"
    assert circular_shift(0, 2) == "0"

@pytest.mark.parametrize("number, shift, expected", [
    (12345, 1, "51234"),
    (12345, 2, "45123"),
    (12345, 5, "12345"),
    (12345, 6, "54321"),
    (10203, 2, "03102"),
    (1, 10, "1"),
    (999, 2, "999"),
])
def test_multiple_cases(number, shift, expected):
    assert circular_shift(number, shift) == expected

def test_zero_shift():
    assert circular_shift(12345, 0) == "12345"

def test_large_numbers():
    assert circular_shift(1000000, 3) == "0001000"
    assert circular_shift(9999999, 4) == "9999999"

def test_numbers_with_zeros():
    assert circular_shift(1020304, 2) == "041020"
    assert circular_shift(100, 1) == "010"

def test_negative_shift():
    with pytest.raises(ValueError):
        circular_shift(12345, -1)

def test_negative_number():
    with pytest.raises(ValueError):
        circular_shift(-123, 2)

def test_negative_both():
    with pytest.raises(ValueError):
        circular_shift(-123, -5)

def test_zero_negative_shift():
    with pytest.raises(ValueError):
        circular_shift(0, -5)