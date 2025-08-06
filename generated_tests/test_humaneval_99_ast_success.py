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
from math import floor, ceil

@pytest.mark.parametrize("value,expected", [
    ("1.5", 2),
    ("-1.5", -2),
    ("2.5", 3),
    ("-2.5", -3),
    ("1.4", 1),
    ("1.6", 2),
    ("-1.4", -1),
    ("-1.6", -2),
    ("1.0", 1),
    ("1.00", 1),
    ("1.000", 1),
    ("0", 0),
    ("0.0", 0),
    ("3.14159", 3),
    ("-3.14159", -3),
    ("100.5", 101),
    ("-100.5", -101),
    ("0.5", 1),
    ("-0.5", -1),
    ("999999.5", 1000000),
    ("-999999.5", -1000000)
])
def test_closest_integer_parametrized(value, expected):
    assert closest_integer(value) == expected

def test_closest_integer_zero():
    assert closest_integer("0.0") == 0
    assert closest_integer("0.00") == 0
    assert closest_integer("-0.0") == 0

@pytest.mark.parametrize("value", [
    "abc",
    "1.2.3",
    "1,5",
    "",
    None,
    "inf",
    "-inf",
    "nan"
])
def test_closest_integer_invalid_input(value):
    with pytest.raises((ValueError, AttributeError, OverflowError)):
        closest_integer(value)

def test_closest_integer_scientific():
    assert closest_integer("1e5") == 100000
    assert closest_integer("1.5e1") == 15
    assert closest_integer("-1e2") == -100

def test_closest_integer_edge_cases():
    assert closest_integer("0.499999999") == 0
    assert closest_integer("-0.499999999") == 0
    assert closest_integer("0.500000001") == 1
    assert closest_integer("-0.500000001") == -1

def test_closest_integer_trailing_zeros():
    assert closest_integer("1.500") == 2
    assert closest_integer("-1.500") == -2
    assert closest_integer("1.40000") == 1
    assert closest_integer("-1.40000") == -1