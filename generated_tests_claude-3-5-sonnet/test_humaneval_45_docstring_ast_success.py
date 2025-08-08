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

def test_triangle_area_positive_numbers():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 20.0
    assert triangle_area(7, 8) == 28.0

def test_triangle_area_zero():
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(5, 0) == 0.0
    assert triangle_area(0, 0) == 0.0

def test_triangle_area_decimal_numbers():
    assert math.isclose(triangle_area(2.5, 3.5), 4.375, rel_tol=1e-9)
    assert math.isclose(triangle_area(0.1, 0.2), 0.01, rel_tol=1e-9)

def test_triangle_area_large_numbers():
    assert triangle_area(1000000, 2000000) == 1000000000000.0

@pytest.mark.parametrize("side,height,expected", [
    (5, 3, 7.5),
    (10, 4, 20.0),
    (2.5, 3.5, 4.375),
    (0, 0, 0.0),
    (1000, 2000, 1000000.0)
])
def test_triangle_area_parametrized(side, height, expected):
    assert math.isclose(triangle_area(side, height), expected, rel_tol=1e-9)

def test_triangle_area_negative_numbers():
    assert triangle_area(-5, 3) == -7.5
    assert triangle_area(5, -3) == -7.5
    assert triangle_area(-5, -3) == 7.5

@pytest.mark.xfail(raises=TypeError)
def test_triangle_area_invalid_input():
    triangle_area("a", 3)

@pytest.mark.xfail(raises=TypeError)
def test_triangle_area_none_input():
    triangle_area(None, None)

@pytest.mark.xfail(raises=TypeError)
def test_triangle_area_missing_args():
    triangle_area()
