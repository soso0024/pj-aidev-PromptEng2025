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

def test_triangle_area_positive_numbers():
    assert isclose(triangle_area(5, 3), 7.5, rel_tol=1e-9)
    assert isclose(triangle_area(10, 4), 20.0, rel_tol=1e-9)

def test_triangle_area_zero():
    assert isclose(triangle_area(0, 5), 0.0, rel_tol=1e-9)
    assert isclose(triangle_area(5, 0), 0.0, rel_tol=1e-9)
    assert isclose(triangle_area(0, 0), 0.0, rel_tol=1e-9)

def test_triangle_area_decimal_numbers():
    assert isclose(triangle_area(2.5, 3.5), 4.375, rel_tol=1e-9)
    assert isclose(triangle_area(0.1, 0.2), 0.01, rel_tol=1e-9)

def test_triangle_area_large_numbers():
    assert isclose(triangle_area(1000000, 2000000), 1000000000000.0, rel_tol=1e-9)

def test_triangle_area_negative_numbers():
    assert isclose(triangle_area(-1, 5), -2.5, rel_tol=1e-9)
    assert isclose(triangle_area(5, -1), -2.5, rel_tol=1e-9)
    assert isclose(triangle_area(-1, -1), 0.5, rel_tol=1e-9)

@pytest.mark.parametrize("side,height", [
    (None, 5),
    (5, None),
    ("string", 5),
    (5, "string"),
    ([], 5),
    (5, [])
])
def test_triangle_area_invalid_types(side, height):
    with pytest.raises((TypeError, ValueError)):
        triangle_area(side, height)

def triangle_area(a, h):
    return a * h / 2.0