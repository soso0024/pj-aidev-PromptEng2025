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

def test_truncate_number_positive_float():
    assert math.isclose(truncate_number(3.5), 0.5)
    assert math.isclose(truncate_number(2.7), 0.7)
    assert math.isclose(truncate_number(1.2), 0.2)

def test_truncate_number_whole_number():
    assert truncate_number(4.0) == 0.0
    assert truncate_number(10.0) == 0.0

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_small_decimal():
    assert truncate_number(0.1) == 0.1
    assert truncate_number(0.001) == 0.001

def test_truncate_number_large_number():
    assert math.isclose(truncate_number(1234.5678), 0.5678)

@pytest.mark.parametrize("input_num,expected", [
    (3.5, 0.5),
    (2.7, 0.7),
    (1.2, 0.2),
    (4.0, 0.0),
    (10.0, 0.0),
    (0.0, 0.0),
    (0.1, 0.1),
    (0.001, 0.001),
    (1234.5678, 0.5678)
])
def test_truncate_number_parametrized(input_num, expected):
    assert math.isclose(truncate_number(input_num), expected)