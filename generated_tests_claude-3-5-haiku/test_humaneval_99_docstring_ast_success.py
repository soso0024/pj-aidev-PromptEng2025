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
import math

def test_closest_integer_positive_numbers():
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("15.5") == 16
    assert closest_integer("15.4") == 15
    assert closest_integer("15.6") == 16

def test_closest_integer_negative_numbers():
    assert closest_integer("-10") == -10
    assert closest_integer("-15.3") == -15
    assert closest_integer("-15.5") == -16
    assert closest_integer("-15.4") == -15
    assert closest_integer("-15.6") == -16

def test_closest_integer_zero_cases():
    assert closest_integer("0") == 0
    assert closest_integer("0.0") == 0
    assert closest_integer("0.1") == 0
    assert closest_integer("-0.1") == 0

def test_closest_integer_decimal_cases():
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("14.50") == 15
    assert closest_integer("-14.50") == -15

def test_closest_integer_trailing_zeros():
    assert closest_integer("15.000") == 15
    assert closest_integer("-15.000") == -15

@pytest.mark.parametrize("input_value,expected", [
    ("10", 10),
    ("15.3", 15),
    ("15.5", 16),
    ("-15.5", -16),
    ("0", 0),
    ("14.50", 15),
    ("-14.50", -15)
])
def test_closest_integer_parametrized(input_value, expected):
    assert closest_integer(input_value) == expected
