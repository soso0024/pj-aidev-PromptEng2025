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

def test_truncate_number_basic():
    assert truncate_number(3.5) == 0.5

def test_truncate_number_zero_decimal():
    assert truncate_number(5.0) == 0.0

def test_truncate_number_small_decimal():
    assert abs(truncate_number(1.1) - 0.1) < 1e-10

def test_truncate_number_large_decimal():
    assert abs(truncate_number(2.9999) - 0.9999) < 1e-10

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_less_than_one():
    assert abs(truncate_number(0.7) - 0.7) < 1e-10

def test_truncate_number_very_small():
    assert abs(truncate_number(0.001) - 0.001) < 1e-10

def test_truncate_number_large_integer_part():
    assert abs(truncate_number(1000.25) - 0.25) < 1e-10

@pytest.mark.parametrize("input_num,expected", [
    (1.0, 0.0),
    (2.5, 0.5),
    (10.75, 0.75),
    (0.333, 0.333),
    (99.99, 0.99),
    (0.0001, 0.0001)
])
def test_truncate_number_parametrized(input_num, expected):
    result = truncate_number(input_num)
    assert abs(result - expected) < 1e-10

def test_truncate_number_floating_point_precision():
    result = truncate_number(1.23456789)
    assert abs(result - 0.23456789) < 1e-10

def test_truncate_number_very_large_number():
    result = truncate_number(123456789.123)
    assert abs(result - 0.123) < 1e-8