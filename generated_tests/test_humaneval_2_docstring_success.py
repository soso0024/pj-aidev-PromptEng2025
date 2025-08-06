# Test cases for HumanEval/2
# Generated using Claude API



def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    return number % 1.0


# Generated test cases:
import pytest
import math
from typing import Union, List

def test_basic_decimal():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(2.25) == 0.25

def test_whole_numbers():
    assert truncate_number(1.0) == 0.0
    assert truncate_number(5.0) == 0.0

def test_small_decimals():
    assert math.isclose(truncate_number(1.001), 0.001, rel_tol=1e-9)
    assert math.isclose(truncate_number(2.999), 0.999, rel_tol=1e-9)

def test_large_numbers():
    assert math.isclose(truncate_number(1000.123), 0.123, rel_tol=1e-9)
    assert math.isclose(truncate_number(999999.999), 0.999, rel_tol=1e-9)

@pytest.mark.parametrize("number,expected", [
    (3.5, 0.5),
    (1.25, 0.25),
    (7.75, 0.75),
    (10.1, 0.1),
    (2.0, 0.0)
])
def test_multiple_cases(number, expected):
    assert math.isclose(truncate_number(number), expected, rel_tol=1e-9)

def test_zero():
    assert truncate_number(0.0) == 0.0

@pytest.mark.parametrize("number", [
    -1.5,
    -2.25,
    -10.75
])
def test_negative_numbers(number):
    result = truncate_number(number)
    expected = number - math.floor(number)
    assert math.isclose(result, expected, rel_tol=1e-9)

def test_non_float_input():
    with pytest.raises(TypeError):
        truncate_number("3.5")
    with pytest.raises(TypeError):
        truncate_number([1.5])
    with pytest.raises(TypeError):
        truncate_number(None)