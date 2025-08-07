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
from math import isnan, copysign

@pytest.mark.parametrize("number,expected", [
    (3.5, 0.5),
    (7.0, 0.0),
    (0.0, 0.0),
    (1.0, 0.0),
    (1.1, 0.1),
    (-1.0, -0.0),
    (-1.1, -0.1),
    (float('inf'), 0.0),
    (float('-inf'), -0.0),
    (float('nan'), float('nan'))
])
def test_truncate_number(number, expected):
    assert truncate_number(number) == expected if not isnan(expected) else isnan(truncate_number(number))

def truncate_number(number: float) -> float:
    return number % 1.0 if number >= 0 else -(abs(number) % 1.0)