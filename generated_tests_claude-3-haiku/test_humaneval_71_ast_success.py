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

def test_triangle_area_valid_triangle():
    assert round(triangle_area(3, 4, 5), 2) == 6.00
    assert round(triangle_area(5, 12, 13), 2) == 30.00
    assert round(triangle_area(7, 8, 9), 2) == 26.83

def test_triangle_area_invalid_triangle():
    assert triangle_area(1, 2, 5) == -1
    assert triangle_area(3, 4, 12) == -1
    assert round(triangle_area(6, 8, 3), 2) == 7.64

@pytest.mark.parametrize("a, b, c, expected", [
    (3.0, 4.0, 5.0, 6.00),
    (5.0, 12.0, 13.0, 30.00),
    (7.0, 8.0, 9.0, 26.83),
    (1.0, 2.0, 5.0, -1),
    (3.0, 4.0, 12.0, -1),
    (6.0, 8.0, 3.0, 7.64)
])
def test_triangle_area_parametrized(a, b, c, expected):
    assert round(triangle_area(a, b, c), 2) == expected

def test_triangle_area_zero_sides():
    assert triangle_area(0, 0, 0) == -1

def test_triangle_area_negative_sides():
    assert triangle_area(-1, 2, 3) == -1
    assert triangle_area(1, -2, 3) == -1
    assert triangle_area(1, 2, -3) == -1