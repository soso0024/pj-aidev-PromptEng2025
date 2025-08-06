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
from math import isclose
from typing import Union, Any

def test_basic_truncation():
    assert isclose(truncate_number(3.5), 0.5, rel_tol=1e-9)
    assert isclose(truncate_number(1.25), 0.25, rel_tol=1e-9)
    assert isclose(truncate_number(7.875), 0.875, rel_tol=1e-9)

@pytest.mark.parametrize("number,expected", [
    (1.0, 0.0),
    (2.0, 0.0),
    (3.0, 0.0),
])
def test_whole_numbers(number, expected):
    assert isclose(truncate_number(number), expected, rel_tol=1e-9)

@pytest.mark.parametrize("number,expected", [
    (0.1, 0.1),
    (0.5, 0.5),
    (0.99, 0.99),
])
def test_decimal_only_numbers(number, expected):
    assert isclose(truncate_number(number), expected, rel_tol=1e-9)

def test_large_numbers():
    assert isclose(truncate_number(1234567.89), 0.89, rel_tol=1e-9)
    assert isclose(truncate_number(999999.999), 0.999, rel_tol=1e-9)

def test_small_decimals():
    assert isclose(truncate_number(1.000001), 0.000001, rel_tol=1e-6)
    assert isclose(truncate_number(2.000000001), 0.000000001, rel_tol=1e-6)

def test_negative_numbers():
    assert isclose(truncate_number(-1.5), 0.5, rel_tol=1e-9)
    assert isclose(truncate_number(-2.75), 0.25, rel_tol=1e-9)
    assert isclose(truncate_number(-0.5), 0.5, rel_tol=1e-9)

def test_zero():
    assert isclose(truncate_number(0.0), 0.0, rel_tol=1e-9)

@pytest.mark.parametrize("invalid_input", [
    "1.5",
    None,
    [],
    {},
])
def test_invalid_types_raise_error(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        truncate_number(invalid_input)