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

def triangle_area(a, h):
    return a * h / 2.0

def test_triangle_area_positive_integers():
    assert triangle_area(4, 6) == 12.0

def test_triangle_area_positive_floats():
    assert abs(triangle_area(3.5, 4.2) - 7.35) < 1e-10

def test_triangle_area_mixed_int_float():
    assert triangle_area(5, 2.4) == 6.0
    assert triangle_area(3.6, 5) == 9.0

def test_triangle_area_zero_base():
    assert triangle_area(0, 5) == 0.0

def test_triangle_area_zero_height():
    assert triangle_area(5, 0) == 0.0

def test_triangle_area_both_zero():
    assert triangle_area(0, 0) == 0.0

def test_triangle_area_negative_base():
    assert triangle_area(-4, 6) == -12.0

def test_triangle_area_negative_height():
    assert triangle_area(4, -6) == -12.0

def test_triangle_area_both_negative():
    assert triangle_area(-4, -6) == 12.0

def test_triangle_area_very_small_values():
    assert triangle_area(0.001, 0.002) == 0.000001

def test_triangle_area_very_large_values():
    assert triangle_area(1000000, 2000000) == 1000000000000.0

@pytest.mark.parametrize("base,height,expected", [
    (1, 2, 1.0),
    (2, 1, 1.0),
    (10, 5, 25.0),
    (7, 8, 28.0),
    (0.5, 4, 1.0),
    (3, 0.5, 0.75)
])
def test_triangle_area_parametrized(base, height, expected):
    assert triangle_area(base, height) == expected

def test_triangle_area_returns_float():
    result = triangle_area(3, 4)
    assert isinstance(result, float)

def test_triangle_area_precision():
    result = triangle_area(1, 3)
    assert abs(result - 1.5) < 1e-10