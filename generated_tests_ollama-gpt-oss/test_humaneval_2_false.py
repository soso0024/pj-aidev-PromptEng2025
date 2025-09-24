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
import sys
import os

# Ensure the root directory is in sys.path so that truncate_number can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from truncate_number import truncate_number

@pytest.mark.parametrize("input_value,expected", [
    (5, 0.0),
    (-3, 0.0),
    (3.1415, 0.1415),
    (-2.718, 0.282),  # approximate
    (0, 0.0),
    (1e20 + 0.123, 0.123),
    (1e-10 + 0.5, 0.5),
    (10, 0.0),
    (True, 0.0),
    (-0.0, 0.0),
    (float('nan'), float('nan')),
])
def test_truncate_number(input_value, expected):
    result = truncate_number(input_value)
    if math.isnan(expected):
        assert math.isnan(result)
    else:
        assert math.isclose(result, expected, rel_tol=1e-9, abs_tol=1e-9)