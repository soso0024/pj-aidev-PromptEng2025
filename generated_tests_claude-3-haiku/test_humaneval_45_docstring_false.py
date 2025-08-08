# Test cases for HumanEval/45
# Generated using Claude API



def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """

    return a * h / 2.0


# Generated test cases:
import pytest
from math import isclose

def triangle_area(a, h):
    if a <= 0 or h <= 0:
        raise ValueError("Side length and height must be positive")
    return a * h / 2.0

@pytest.mark.parametrize("a, h, expected", [
    (5, 3, 7.5),
    (10, 6, 30.0),
    (0, 10, pytest.raises(ValueError)),
    (-5, 3, pytest.raises(ValueError)),
    (5, 0, pytest.raises(ValueError)),
    (5.5, 3.2, 8.8),
    (2.3, 4.1, 4.715)
])
def test_triangle_area(a, h, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            triangle_area(a, h)
    else:
        assert isclose(triangle_area(a, h), expected)

def test_triangle_area_zero_side():
    with pytest.raises(ValueError):
        triangle_area(0, 10)

def test_triangle_area_negative_side():
    with pytest.raises(ValueError):
        triangle_area(-5, 3)

def test_triangle_area_negative_height():
    with pytest.raises(ValueError):
        triangle_area(5, -3)