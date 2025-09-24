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
        raise ValueError
    return a * h / 2.0

def test_triangle_area_positive_values():
    assert round(triangle_area(5, 3), 2) == 7.5
    assert round(triangle_area(10, 6), 2) == 30.0
    assert round(triangle_area(3.5, 4.2), 2) == 7.35

def test_triangle_area_zero_values():
    assert triangle_area(0, 10) == 0.0
    assert triangle_area(5, 0) == 0.0
    assert triangle_area(0, 0) == 0.0

@pytest.mark.parametrize("a, h, expected", [
    (-5, 3, ValueError),
    (5, -3, ValueError),
    (-5, -3, ValueError)
])
def test_triangle_area_negative_values(a, h, expected):
    with pytest.raises(expected):
        triangle_area(a, h)

def test_triangle_area_float_values():
    assert round(triangle_area(3.14, 2.71), 4) == 4.2547
    assert round(triangle_area(7.5, 4.2), 2) == 15.75
    assert round(triangle_area(1.0, 1.0), 1) == 0.5