# Test cases for HumanEval/45
# Generated using Claude API



def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """

    return a * h / 2.0


# Generated test cases:
from math import isclose
import pytest
from triangle_area import triangle_area

@pytest.mark.parametrize("a, h, expected", [
    (0, 0, 0),
    (0, 10, 0),
    (10, 0, 0),
    (5, 10, 25),
    (10.5, 7.2, 37.8),
    (-5, 10, -25),
    (5, -10, -25),
    (0.0, 10.0, 0.0),
    (10.0, 0.0, 0.0),
    (5.0, 10.0, 25.0)
])
def test_triangle_area(a, h, expected):
    assert isclose(triangle_area(a, h), expected)

def test_triangle_area_zero_input():
    with pytest.raises(ZeroDivisionError):
        triangle_area(0, 0)

def test_triangle_area_negative_input():
    assert triangle_area(-5, 10) == -25
    assert triangle_area(5, -10) == -25