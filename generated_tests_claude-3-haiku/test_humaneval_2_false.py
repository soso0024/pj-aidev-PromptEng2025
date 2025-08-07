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
from solution import truncate_number
import pytest
from math import isnan, inf, nan

@pytest.mark.parametrize("number,expected", [
    (0.0, 0.0),
    (1.0, 0.0),
    (-1.0, 0.0),
    (3.14, 0.14),
    (-3.14, -0.14),
    (1.5, 0.5),
    (-1.5, -0.5),
    (0.0001, 0.0001),
    (-0.0001, -0.0001),
    (inf, 0.0),
    (-inf, 0.0),
    (nan, nan)
])
def test_truncate_number(number, expected):
    result = truncate_number(number)
    if isnan(expected):
        assert isnan(result)
    else:
        assert result == expected