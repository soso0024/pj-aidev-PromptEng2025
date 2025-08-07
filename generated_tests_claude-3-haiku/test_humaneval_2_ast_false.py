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
from math import modf, isnan

@pytest.mark.parametrize("number,expected", [
    (0.0, 0.0),
    (1.0, 0.0),
    (-1.0, 0.0),
    (3.14, 0.14),
    (-3.14, -0.86),
    (1.5, 0.5),
    (-1.5, -0.5),
    (float('inf'), 0.0),
    (float('-inf'), 0.0),
    (float('nan'), float('nan')),
])
def test_truncate_number(number, expected):
    assert round(modf(number)[0], 14) == round(expected, 14) or (isnan(modf(number)[0]) and isnan(expected))

def truncate_number(number: float) -> float:
    return number % 1.0