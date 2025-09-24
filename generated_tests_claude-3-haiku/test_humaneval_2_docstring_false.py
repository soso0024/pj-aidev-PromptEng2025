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
from math import isnan, modf

@pytest.mark.parametrize("input,expected", [
    (3.5, 0.5),
    (0.0, 0.0),
    (1.0, 0.0),
    (-1.5, -0.5),
    (100.99, 0.99),
    (float('inf'), 0.0),
    (float('-inf'), 0.0),
    (float('nan'), float('nan'))
])
def test_truncate_number(input, expected):
    assert truncate_number(input) == expected
    if isnan(expected):
        assert isnan(truncate_number(input))

def truncate_number(number: float) -> float:
    return number % 1.0