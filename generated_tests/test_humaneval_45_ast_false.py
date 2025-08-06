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
import math
from typing import Union, Any

def test_triangle_area_positive_numbers():
    assert triangle_area(4, 3) == 6.0
    assert triangle_area(5, 2) == 5.0

def test_triangle_area_zero():
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(5, 0) == 0.0
    assert triangle_area(0, 0) == 0.0

def test_triangle_area_decimal_numbers():
    assert math.isclose(triangle_area(2.5, 3.0), 3.75, rel_tol=1e-9)
    assert math.isclose(triangle_area(1.5, 2.5), 1.875, rel_tol=1e-9)

def test_triangle_area_large_numbers():
    assert triangle_area(1000000, 2000000) == 1000000000000.0

@pytest.mark.parametrize("base,height,expected", [
    (4, 3, 6.0),
    (5, 2, 5.0),
    (2.5, 3.0, 3.75),
    (0, 5, 0.0),
    (1000, 2000, 1000000.0)
])
def test_triangle_area_parametrized(base, height, expected):
    assert math.isclose(triangle_area(base, height), expected, rel_tol=1e-9)

@pytest.mark.parametrize("base,height", [
    (-4, 3),
    (4, -3),
    (-4, -3)
])
def test_triangle_area_negative_numbers(base, height):
    result = triangle_area(base, height)
    assert isinstance(result, float)
    assert result < 0 if (base < 0) != (height < 0) else result > 0

def test_triangle_area_types():
    assert isinstance(triangle_area(4, 3), float)
    assert isinstance(triangle_area(5, 2), float)
    assert isinstance(triangle_area(0, 0), float)

@pytest.mark.parametrize("invalid_input", [
    "string",
    None,
    [],
    {},
])
def test_triangle_area_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        triangle_area(invalid_input, 5)
    with pytest.raises((TypeError, ValueError)):
        triangle_area(5, invalid_input)

def test_triangle_area_boolean():
    with pytest.raises((TypeError, ValueError)):
        triangle_area(True, 5)
    with pytest.raises((TypeError, ValueError)):
        triangle_area(5, True)