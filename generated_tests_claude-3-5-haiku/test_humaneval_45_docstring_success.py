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
    if a < 0 or h < 0:
        raise ValueError("Side and height must be non-negative")
    return a * h / 2.0

def test_triangle_area_normal_case():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 20.0

def test_triangle_area_zero_values():
    assert triangle_area(0, 5) == 0
    assert triangle_area(5, 0) == 0

def test_triangle_area_floating_point():
    assert triangle_area(3.5, 2.5) == 4.375
    assert triangle_area(7.2, 1.8) == 6.48

def test_triangle_area_negative_input():
    with pytest.raises(ValueError):
        triangle_area(-5, 3)
    with pytest.raises(ValueError):
        triangle_area(5, -3)

@pytest.mark.parametrize("side,height,expected", [
    (5, 3, 7.5),
    (10, 4, 20.0),
    (2.5, 6.0, 7.5),
    (0, 5, 0),
    (5, 0, 0)
])
def test_triangle_area_parametrized(side, height, expected):
    assert triangle_area(side, height) == expected