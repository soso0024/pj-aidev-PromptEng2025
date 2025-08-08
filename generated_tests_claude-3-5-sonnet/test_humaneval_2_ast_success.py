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

def test_truncate_number_basic():
    assert truncate_number(3.14) == pytest.approx(0.14)
    assert truncate_number(2.0) == pytest.approx(0.0)

@pytest.mark.parametrize("number,expected", [
    (1.5, 0.5),
    (2.75, 0.75),
    (3.0, 0.0),
    (0.123, 0.123),
    (-1.75, 0.25),
    (-2.25, 0.75),
    (0.0, 0.0),
    (1.999999, 0.999999),
])
def test_truncate_number_parametrized(number, expected):
    assert isclose(truncate_number(number), expected, rel_tol=1e-9)

def test_truncate_number_large_values():
    assert isclose(truncate_number(1000.123), 0.123, rel_tol=1e-9)
    assert isclose(truncate_number(-1000.123), 0.877, rel_tol=1e-9)

def test_truncate_number_small_decimals():
    assert isclose(truncate_number(1.000001), 0.000001, rel_tol=1e-6)
    assert isclose(truncate_number(2.000000001), 0.000000001, rel_tol=1e-6)

@pytest.mark.parametrize("invalid_input", [
    "1.23",
    None,
    [],
    {},
])
def test_truncate_number_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        truncate_number(invalid_input)

def test_truncate_number_boolean():
    result = truncate_number(True)
    assert result == 0.0

def test_truncate_number_infinity():
    result = truncate_number(float('inf'))
    assert result != result  # NaN check

def test_truncate_number_nan():
    result = truncate_number(float('nan'))
    assert result != result  # NaN check