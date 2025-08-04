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

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 4, 5, 6.00),
    (5, 12, 13, 30.00),
    (1, 1, 1, 0.43),
    (10, 10, 10, 43.30),
    (2.5, 3.5, 4.5, 4.35),
    (0, 0, 0, -1),
    (-1, 2, 3, -1),
    (1, -2, 3, -1),
    (1, 2, -3, -1),
    (1, 2, 4, -1),
    (2, 8, 3, -1),
    (0.1, 0.2, 0.3, 0.00),
    (100, 100, 200, -1),
    (1e-10, 1e-10, 1e-10, 0.00),
    (1000000, 1000000, 1000000, 433012701892.22)
])
def test_triangle_area(a, b, c, expected):
    assert triangle_area(a, b, c) == expected

def test_triangle_area_zero_input():
    assert triangle_area(0, 1, 1) == -1
    assert triangle_area(1, 0, 1) == -1
    assert triangle_area(1, 1, 0) == -1

def test_triangle_area_negative_input():
    assert triangle_area(-1, -1, -1) == -1
    assert triangle_area(-5, 2, 3) == -1

def test_triangle_area_invalid_triangle():
    assert triangle_area(1, 1, 3) == -1
    assert triangle_area(1, 3, 1) == -1
    assert triangle_area(3, 1, 1) == -1

def test_triangle_area_float_precision():
    assert abs(triangle_area(2.5, 3.5, 4.5) - 4.35) < 0.01
    assert abs(triangle_area(1.23, 2.34, 2.55) - 1.43) < 0.01

def test_triangle_area_equilateral():
    assert triangle_area(5, 5, 5) == 10.83

def test_triangle_area_isosceles():
    assert triangle_area(5, 5, 6) == 12.00

def test_triangle_area_large_numbers():
    assert triangle_area(1000, 1000, 1000) == 433012.70