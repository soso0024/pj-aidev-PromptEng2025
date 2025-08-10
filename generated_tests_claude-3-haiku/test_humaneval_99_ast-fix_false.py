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

def test_closest_integer(value, expected):
    num = float(value) if value else 0
    if value and value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    else:
        res = int(round(num))
    assert res == expected

@pytest.mark.parametrize("value,expected", [
    ("3.5", 4),
    ("2.4", 2),
    ("-1.5", -2),
    ("10", 10),
    ("0.0", 0),
    ("5.50", 6),
    ("-2.50", -3),
    ("0", 0),
    ("", 0),
    ("   ", 0),
    ("abc", 0),
    ("3.14159", 3),
    ("-4.99999", -5),
    ("2.50000", 3),
    ("-1.00000", -1)
])
def test_closest_integer(value, expected):
    test_closest_integer(value, expected)