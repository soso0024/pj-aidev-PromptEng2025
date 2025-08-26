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

def test_triangle_area_positive_values():
    assert triangle_area(5, 4) == 10.0
    assert triangle_area(10, 6) == 30.0
    assert triangle_area(3.5, 2.0) == 3.5

def test_triangle_area_zero_values():
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(5, 0) == 0.0

def test_triangle_area_negative_values():
    assert triangle_area(-5, 4) == -10.0
    assert triangle_area(5, -4) == -10.0
    assert triangle_area(-5, -4) == 10.0

def test_triangle_area_floating_point():
    assert triangle_area(2.5, 3.5) == 4.375
    assert triangle_area(0.1, 0.2) == pytest.approx(0.01)

@pytest.mark.parametrize("base,height,expected", [
    (5, 4, 10.0),
    (10, 6, 30.0),
    (3.5, 2.0, 3.5),
    (0, 5, 0.0),
    (5, 0, 0.0),
    (-5, 4, -10.0),
    (5, -4, -10.0),
    (2.5, 3.5, 4.375)
])
def test_triangle_area_parametrized(base, height, expected):
    assert triangle_area(base, height) == expected