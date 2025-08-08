# Test cases for HumanEval/71
# Generated using Claude API


def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''

    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area


# Generated test cases:
import pytest
from math import isclose

def test_triangle_area_valid_triangle():
    assert triangle_area(3, 4, 5) == 6.0
    assert triangle_area(5, 12, 13) == 30.0
    assert isclose(triangle_area(7.5, 8.5, 10), 31.07, rel_tol=1e-2)

def test_triangle_area_impossible_triangle():
    assert triangle_area(1, 1, 10) == -1
    assert triangle_area(1, 2, 3) == -1
    assert triangle_area(0, 0, 0) == -1

def test_triangle_area_floating_point():
    assert isclose(triangle_area(3.5, 4.2, 5.1), 7.35, rel_tol=1e-2)

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 4, 5, 6.0),
    (5, 12, 13, 30.0),
    (1, 1, 10, -1),
    (0, 0, 0, -1),
    (7.5, 8.5, 10, 31.07)
])
def test_triangle_area_parametrized(a, b, c, expected):
    assert isclose(triangle_area(a, b, c), expected, rel_tol=1e-2)

def test_triangle_area_negative_sides():
    assert triangle_area(-3, 4, 5) == -1
    assert triangle_area(3, -4, 5) == -1
    assert triangle_area(3, 4, -5) == -1