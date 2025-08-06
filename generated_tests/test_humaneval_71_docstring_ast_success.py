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

def test_valid_triangle():
    assert triangle_area(3, 4, 5) == 6.00
    
def test_equilateral_triangle():
    assert triangle_area(5, 5, 5) == 10.83

def test_isosceles_triangle():
    assert triangle_area(5, 5, 8) == 12.00

@pytest.mark.parametrize("a,b,c,expected", [
    (1, 2, 10, -1),
    (10, 2, 1, -1),
    (1, 10, 2, -1),
    (0, 4, 5, -1),
    (-1, 4, 5, -1),
    (3, -4, 5, -1),
    (0, 0, 0, -1)
])
def test_invalid_triangles(a, b, c, expected):
    assert triangle_area(a, b, c) == expected

@pytest.mark.parametrize("a,b,c,expected", [
    (5, 12, 13, 30.00),
    (8, 15, 17, 60.00),
    (7, 24, 25, 84.00),
    (20, 21, 29, 210.00)
])
def test_right_triangles(a, b, c, expected):
    assert triangle_area(a, b, c) == expected

def test_small_triangle():
    assert triangle_area(0.5, 0.5, 0.5) == 0.11

def test_large_triangle():
    assert triangle_area(1000, 1000, 1000) == 433012.70

@pytest.mark.parametrize("a,b,c", [
    (3.14159, 2.71828, 5.0),
    (2.5, 3.5, 4.5),
    (1.23456, 2.34567, 3.45678)
])
def test_decimal_sides(a, b, c):
    result = triangle_area(a, b, c)
    assert result > 0
    assert isinstance(result, float)
    assert len(str(result).split('.')[-1]) <= 2

def test_almost_invalid_triangle():
    assert triangle_area(2, 3, 4.99) > 0

def test_float_precision():
    result = triangle_area(1.23456789, 2.34567890, 3.45678901)
    assert len(str(result).split('.')[-1]) <= 2