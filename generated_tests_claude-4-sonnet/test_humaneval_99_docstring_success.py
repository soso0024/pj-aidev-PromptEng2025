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

def closest_integer(value):

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

def test_integer_strings():
    assert closest_integer("10") == 10
    assert closest_integer("0") == 0
    assert closest_integer("-5") == -5
    assert closest_integer("100") == 100

def test_decimal_strings():
    assert closest_integer("15.3") == 15
    assert closest_integer("15.7") == 16
    assert closest_integer("-15.3") == -15
    assert closest_integer("-15.7") == -16

def test_half_values_round_away_from_zero():
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("0.5") == 1
    assert closest_integer("-0.5") == -1
    assert closest_integer("1.5") == 2
    assert closest_integer("-1.5") == -2

def test_trailing_zeros():
    assert closest_integer("10.0") == 10
    assert closest_integer("15.50") == 16
    assert closest_integer("-15.50") == -16
    assert closest_integer("0.0") == 0
    assert closest_integer("5.000") == 5

def test_small_decimals():
    assert closest_integer("0.1") == 0
    assert closest_integer("0.4") == 0
    assert closest_integer("0.6") == 1
    assert closest_integer("0.9") == 1
    assert closest_integer("-0.1") == 0
    assert closest_integer("-0.4") == 0
    assert closest_integer("-0.6") == -1
    assert closest_integer("-0.9") == -1

def test_large_numbers():
    assert closest_integer("999.4") == 999
    assert closest_integer("999.6") == 1000
    assert closest_integer("-999.4") == -999
    assert closest_integer("-999.6") == -1000

def test_edge_cases():
    assert closest_integer("0.0") == 0
    assert closest_integer("-0.0") == 0

@pytest.mark.parametrize("value,expected", [
    ("2.5", 3),
    ("-2.5", -3),
    ("3.5", 4),
    ("-3.5", -4),
    ("10.5", 11),
    ("-10.5", -11)
])
def test_parametrized_half_values(value, expected):
    assert closest_integer(value) == expected

@pytest.mark.parametrize("value,expected", [
    ("1.2", 1),
    ("1.8", 2),
    ("-1.2", -1),
    ("-1.8", -2),
    ("2.3", 2),
    ("2.7", 3)
])
def test_parametrized_regular_rounding(value, expected):
    assert closest_integer(value) == expected
