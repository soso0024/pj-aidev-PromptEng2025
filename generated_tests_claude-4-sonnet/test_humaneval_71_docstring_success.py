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
import math

def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

def test_valid_triangle_3_4_5():
    assert triangle_area(3, 4, 5) == 6.00

def test_valid_triangle_1_2_10():
    assert triangle_area(1, 2, 10) == -1

def test_equilateral_triangle():
    assert triangle_area(5, 5, 5) == 10.83

def test_isosceles_triangle():
    assert triangle_area(5, 5, 8) == 12.00

def test_right_triangle():
    assert triangle_area(6, 8, 10) == 24.00

def test_invalid_triangle_sum_equals():
    assert triangle_area(1, 2, 3) == -1

def test_invalid_triangle_one_side_too_long():
    assert triangle_area(1, 1, 5) == -1

def test_invalid_triangle_zero_side():
    assert triangle_area(0, 5, 5) == -1

def test_invalid_triangle_negative_side():
    assert triangle_area(-1, 5, 5) == -1

def test_small_valid_triangle():
    assert triangle_area(0.1, 0.1, 0.1) == 0.00

def test_large_valid_triangle():
    assert triangle_area(100, 100, 100) == 4330.13

def test_scalene_triangle():
    assert triangle_area(7, 8, 9) == 26.83

def test_barely_valid_triangle():
    assert triangle_area(2, 3, 4.9) == 1.19

def test_barely_invalid_triangle():
    assert triangle_area(2, 3, 5) == -1

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 4, 5, 6.00),
    (1, 2, 10, -1),
    (5, 5, 5, 10.83),
    (0, 1, 1, -1),
    (1, 1, 1, 0.43),
    (10, 10, 10, 43.30),
    (1, 1, 2, -1),
    (2, 2, 3, 1.98)
])
def test_triangle_area_parametrized(a, b, c, expected):
    assert triangle_area(a, b, c) == expected