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

def triangle_area(a, h):
    return a * h / 2.0

def test_triangle_area_positive_integers():
    assert triangle_area(5, 3) == 7.5

def test_triangle_area_positive_floats():
    assert triangle_area(4.5, 2.0) == 4.5

def test_triangle_area_zero_base():
    assert triangle_area(0, 5) == 0.0

def test_triangle_area_zero_height():
    assert triangle_area(10, 0) == 0.0

def test_triangle_area_both_zero():
    assert triangle_area(0, 0) == 0.0

def test_triangle_area_small_values():
    assert abs(triangle_area(0.1, 0.2) - 0.01) < 1e-10

def test_triangle_area_large_values():
    assert triangle_area(1000, 500) == 250000.0

def test_triangle_area_fractional_result():
    assert triangle_area(3, 1) == 1.5

@pytest.mark.parametrize("a,h,expected", [
    (1, 1, 0.5),
    (2, 4, 4.0),
    (10, 6, 30.0),
    (7.5, 4, 15.0),
    (0.5, 0.8, 0.2),
    (100, 0.01, 0.5)
])
def test_triangle_area_parametrized(a, h, expected):
    assert triangle_area(a, h) == expected

def test_triangle_area_negative_base():
    assert triangle_area(-5, 4) == -10.0

def test_triangle_area_negative_height():
    assert triangle_area(6, -3) == -9.0

def test_triangle_area_both_negative():
    assert triangle_area(-4, -5) == 10.0

def test_triangle_area_returns_float():
    result = triangle_area(3, 2)
    assert isinstance(result, float)
    assert result == 3.0