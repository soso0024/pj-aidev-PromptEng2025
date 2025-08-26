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
    if not value:
        return 0

    if value.count('.') == 1:
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = round(num)
        else:
            res = round(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res

def test_closest_integer_positive_numbers():
    assert closest_integer('1.4') == 1
    assert closest_integer('1.5') == 2
    assert closest_integer('1.6') == 2
    assert closest_integer('2.0') == 2
    assert closest_integer('2.1') == 2

def test_closest_integer_negative_numbers():
    assert closest_integer('-1.4') == -1
    assert closest_integer('-1.5') == -1
    assert closest_integer('-1.6') == -2
    assert closest_integer('-2.0') == -2
    assert closest_integer('-2.1') == -2

def test_closest_integer_zero_cases():
    assert closest_integer('0.0') == 0
    assert closest_integer('0.4') == 0
    assert closest_integer('0.5') == 0
    assert closest_integer('0.6') == 1

def test_closest_integer_trailing_zeros():
    assert closest_integer('1.500') == 2
    assert closest_integer('1.50000') == 2
    assert closest_integer('-1.500') == -1

def test_closest_integer_edge_cases():
    assert closest_integer('') == 0
    assert closest_integer('1') == 1
    assert closest_integer('-1') == -1

@pytest.mark.parametrize("input_value,expected", [
    ('1.4', 1),
    ('1.5', 2),
    ('1.6', 2),
    ('-1.4', -1),
    ('-1.5', -1),
    ('-1.6', -2),
    ('0.5', 0),
    ('1.500', 2),
    ('', 0)
])
def test_closest_integer_parametrized(input_value, expected):
    assert closest_integer(input_value) == expected