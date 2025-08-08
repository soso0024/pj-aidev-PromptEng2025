# Test cases for HumanEval/99
# Generated using Claude API


def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''

    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res



# Generated test cases:
import pytest

@pytest.mark.parametrize("value,expected", [
    ("1.5", 2),
    ("-1.5", -2),
    ("2.3", 2),
    ("2.7", 3),
    ("-2.3", -2),
    ("-2.7", -3),
    ("1.0", 1),
    ("0.0", 0),
    ("42", 42),
    ("-42", -42),
    ("0.500", 1),
    ("-0.500", -1),
    ("2.500", 3),
    ("-2.500", -3),
    ("0.499", 0),
    ("-0.499", 0),
    ("3.499", 3),
    ("-3.499", -3),
    ("1.50000", 2),
    ("-1.50000", -2)
])
def test_closest_integer_normal_cases(value, expected):
    assert closest_integer(value) == expected

def test_closest_integer_empty_string():
    with pytest.raises(ValueError):
        closest_integer("")

@pytest.mark.parametrize("value", [
    "abc",
    "1.2.3",
    "1,5",
    None,
    ".",
    ".."
])
def test_closest_integer_invalid_input(value):
    with pytest.raises((ValueError, AttributeError)):
        closest_integer(value)

def test_closest_integer_scientific_notation():
    assert closest_integer("1e5") == 100000
    assert closest_integer("1.5e2") == 150

def test_closest_integer_large_numbers():
    assert closest_integer("999999999.5") == 1000000000
    assert closest_integer("-999999999.5") == -1000000000

def test_closest_integer_small_numbers():
    assert closest_integer("0.000001") == 0
    assert closest_integer("-0.000001") == 0

def test_closest_integer_edge_cases():
    assert closest_integer("0.5") == 1
    assert closest_integer("-0.5") == -1
    assert closest_integer("0.50") == 1
    assert closest_integer("-0.50") == -1