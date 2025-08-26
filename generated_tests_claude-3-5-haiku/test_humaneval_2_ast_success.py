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

def test_truncate_number_positive_whole():
    assert truncate_number(5.0) == 0.0

def test_truncate_number_positive_fraction():
    assert round(truncate_number(3.14), 2) == 0.14

def test_truncate_number_negative_whole():
    assert truncate_number(-5.0) == 0.0

def test_truncate_number_negative_fraction():
    assert round(truncate_number(-3.14), 2) == 0.86

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

@pytest.mark.parametrize("input_value,expected", [
    (1.5, 0.5),
    (2.75, 0.75),
    (-1.25, 0.75),
    (10.99, 0.99)
])
def test_truncate_number_parametrized(input_value, expected):
    assert round(truncate_number(input_value), 2) == expected

def test_truncate_number_large_number():
    assert truncate_number(1000000.5) == 0.5

def test_truncate_number_small_number():
    assert truncate_number(0.000001) == 0.000001