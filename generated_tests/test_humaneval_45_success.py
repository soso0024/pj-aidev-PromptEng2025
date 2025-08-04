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
    assert triangle_area(4, 3) == 6.0
    assert triangle_area(2, 5) == 5.0

def test_triangle_area_zero():
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(5, 0) == 0.0
    assert triangle_area(0, 0) == 0.0

def test_triangle_area_decimal_numbers():
    assert triangle_area(2.5, 4.0) == 5.0
    assert triangle_area(1.5, 3.0) == 2.25
    assert math.isclose(triangle_area(1.3333, 2.5), 1.666625, rel_tol=1e-9)

def test_triangle_area_large_numbers():
    assert triangle_area(1000000, 2000000) == 1000000000000.0

@pytest.mark.parametrize("base,height,expected", [
    (4, 3, 6.0),
    (2, 5, 5.0),
    (1.5, 2, 1.5),
    (10, 0.5, 2.5)
])
def test_triangle_area_parametrized(base, height, expected):
    assert triangle_area(base, height) == expected

def test_triangle_area_negative_numbers():
    assert triangle_area(-4, 3) == -6.0
    assert triangle_area(4, -3) == -6.0
    assert triangle_area(-4, -3) == 6.0

@pytest.mark.xfail(raises=TypeError)
def test_triangle_area_invalid_types():
    triangle_area("4", 3)

@pytest.mark.xfail(raises=TypeError)
def test_triangle_area_none_values():
    triangle_area(None, None)

@pytest.mark.xfail(raises=TypeError)
def test_triangle_area_invalid_types_mixed():
    triangle_area(4, "3")
