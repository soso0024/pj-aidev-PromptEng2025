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

def test_triangle_area_normal_case():
    assert triangle_area(5, 4) == 10.0

def test_triangle_area_zero_base():
    assert triangle_area(0, 10) == 0.0

def test_triangle_area_zero_height():
    assert triangle_area(10, 0) == 0.0

def test_triangle_area_negative_values():
    assert triangle_area(-5, 4) == -10.0
    assert triangle_area(5, -4) == -10.0

def test_triangle_area_floating_point():
    assert triangle_area(3.5, 2.5) == 4.375

@pytest.mark.parametrize("base,height,expected", [
    (5, 4, 10.0),
    (0, 10, 0.0),
    (10, 0, 0.0),
    (-5, 4, -10.0),
    (3.5, 2.5, 4.375)
])
def test_triangle_area_parametrized(base, height, expected):
    assert triangle_area(base, height) == expected
