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

def test_positive_half_values():
    assert closest_integer("10.5") == 11
    assert closest_integer("1.5") == 2
    assert closest_integer("0.5") == 1

def test_negative_half_values():
    assert closest_integer("-10.5") == -11
    assert closest_integer("-1.5") == -2
    assert closest_integer("-0.5") == -1

def test_positive_non_half_values():
    assert closest_integer("10.4") == 10
    assert closest_integer("10.6") == 11
    assert closest_integer("1.2") == 1
    assert closest_integer("1.8") == 2

def test_negative_non_half_values():
    assert closest_integer("-10.4") == -10
    assert closest_integer("-10.6") == -11
    assert closest_integer("-1.2") == -1
    assert closest_integer("-1.8") == -2

def test_integer_values():
    assert closest_integer("10") == 10
    assert closest_integer("-10") == -10
    assert closest_integer("0") == 0
    assert closest_integer("1") == 1

def test_trailing_zeros():
    assert closest_integer("10.50") == 11
    assert closest_integer("-10.50") == -11
    assert closest_integer("1.500") == 2
    assert closest_integer("-1.500") == -2
    assert closest_integer("10.40") == 10
    assert closest_integer("10.60") == 11

def test_multiple_trailing_zeros():
    assert closest_integer("10.5000") == 11
    assert closest_integer("-10.5000") == -11
    assert closest_integer("1.2000") == 1

def test_decimal_without_trailing_zeros():
    assert closest_integer("10.1") == 10
    assert closest_integer("10.9") == 11
    assert closest_integer("-10.1") == -10
    assert closest_integer("-10.9") == -11

def test_zero_variations():
    assert closest_integer("0.0") == 0
    assert closest_integer("0.00") == 0
    assert closest_integer("-0.0") == 0

def test_small_decimals():
    assert closest_integer("0.1") == 0
    assert closest_integer("0.9") == 1
    assert closest_integer("-0.1") == 0
    assert closest_integer("-0.9") == -1

def test_large_numbers():
    assert closest_integer("1000.5") == 1001
    assert closest_integer("-1000.5") == -1001
    assert closest_integer("999.4") == 999
    assert closest_integer("999.6") == 1000

def test_edge_case_half_with_trailing_zeros():
    assert closest_integer("2.50") == 3
    assert closest_integer("-2.50") == -3
    assert closest_integer("100.500") == 101
    assert closest_integer("-100.500") == -101