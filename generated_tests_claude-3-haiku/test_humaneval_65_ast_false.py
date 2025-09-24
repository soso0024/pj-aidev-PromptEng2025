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
    assert circular_shift(54321, 4) == "43215"
    assert circular_shift("abcde", 3) == "cdeab"

def test_circular_shift_edge_cases():
    assert circular_shift(12345, 5) == "12345"
    assert circular_shift(12345, 0) == "12345"
    assert circular_shift("", 2) == ""
    assert circular_shift(12345, 6) == "54321"

@pytest.mark.parametrize("input,shift,expected", [
    (12345, 7, "54321"),
    ("abcde", 6, "abcde"),
    (54321, 10, "54321"),
    ("", 5, "")
])
def test_circular_shift_with_parametrize(input, shift, expected):
    assert circular_shift(input, shift) == expected

def test_circular_shift_with_negative_shift():
    with pytest.raises(ValueError):
        circular_shift(12345, -2)