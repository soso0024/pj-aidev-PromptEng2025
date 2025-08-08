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

def test_circular_shift_normal_case():
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(54321, 3) == "21543"

def test_circular_shift_full_shift():
    assert circular_shift(12345, 5) == "12345"
    assert circular_shift(54321, 5) == "54321"

def test_circular_shift_zero_shift():
    assert circular_shift(12345, 0) == "12345"
    assert circular_shift(54321, 0) == "54321"

def test_circular_shift_negative_shift():
    assert circular_shift(12345, -2) == "45123"
    assert circular_shift(54321, -3) == "21543"

def test_circular_shift_large_shift():
    assert circular_shift(12345, 10) == "12345"
    assert circular_shift(54321, 20) == "54321"

def test_circular_shift_string_input():
    assert circular_shift("abcde", 2) == "deabc"
    assert circular_shift("xyz", 1) == "zxy"

def test_circular_shift_empty_input():
    assert circular_shift("", 2) == ""
    assert circular_shift(0, 3) == "0"

@pytest.mark.parametrize("input,shift,expected", [
    (12345, 2, "45123"),
    (54321, 3, "21543"),
    (12345, 5, "12345"),
    (54321, 5, "54321"),
    (12345, 0, "12345"),
    (54321, 0, "54321"),
    (12345, -2, "45123"),
    (54321, -3, "21543"),
    (12345, 10, "12345"),
    (54321, 20, "54321"),
    ("abcde", 2, "deabc"),
    ("xyz", 1, "zxy"),
    ("", 2, ""),
    (0, 3, "0")
])
def test_circular_shift_parametrized(input, shift, expected):
    assert circular_shift(input, shift) == expected