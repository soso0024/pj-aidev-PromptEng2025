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
from math import floor, ceil

def closest_integer(value):
    if value.count('.') == 1:
        while value[-1] == '0':
            value = value[:-1]
        if value[-1] == '.':
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    else:
        res = round(num)

    return int(res)

import pytest

@pytest.mark.parametrize("value,expected", [
    ("3.5", 4),
    ("2.4", 2),
    ("-1.5", -2),
    ("0.5", 1),
    ("-0.5", 0),
    ("10", 10),
    ("-10", -10),
    ("0", 0),
    ("", 0),
    ("3.14159", 3),
    ("-3.14159", -3),
    ("2.50", 3),
    ("-2.50", -3),
    ("2.49", 2),
    ("-2.49", -2),
])
def test_closest_integer(value, expected):
    assert closest_integer(value) == expected

def test_closest_integer_edge_cases():
    assert closest_integer("") == 0
    assert closest_integer("0") == 0
    assert closest_integer("-0") == 0
    assert closest_integer("0.0") == 0
    assert closest_integer("-0.0") == 0

def test_closest_integer_rounding():
    assert closest_integer("3.5") == 4
    assert closest_integer("-3.5") == -4
    assert closest_integer("2.49") == 2
    assert closest_integer("-2.49") == -2
    assert closest_integer("2.50") == 3
    assert closest_integer("-2.50") == -3

def test_closest_integer_trailing_zeros():
    assert closest_integer("3.000") == 3
    assert closest_integer("-3.000") == -3
    assert closest_integer("2.400") == 2
    assert closest_integer("-2.400") == -2