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
        raise ValueError("Side length and height must be non-negative")
    return a * h / 2.0

def test_triangle_area_positive_values():
    assert round(triangle_area(5, 3), 2) == 7.5
    assert round(triangle_area(10, 6), 2) == 30.0
    assert round(triangle_area(3.5, 4.2), 2) == 7.35

def test_triangle_area_zero_values():
    assert triangle_area(0, 10) == 0.0
    assert triangle_area(5, 0) == 0.0
    assert triangle_area(0, 0) == 0.0

def test_triangle_area_negative_values():
    with pytest.raises(ValueError):
        triangle_area(-5, 3)
    with pytest.raises(ValueError):
        triangle_area(5, -3)
    with pytest.raises(ValueError):
        triangle_area(-5, -3)

@pytest.mark.parametrize("a, h, expected", [
    (5, 3, 7.5),
    (10, 6, 30.0),
    (3.5, 4.2, 7.35),
    (0, 10, 0.0),
    (5, 0, 0.0),
    (0, 0, 0.0),
])
def test_triangle_area_parametrized(a, h, expected):
    assert round(triangle_area(a, h), 2) == expected