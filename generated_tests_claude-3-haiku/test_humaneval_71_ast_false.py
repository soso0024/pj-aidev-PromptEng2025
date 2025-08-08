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
from triangle_area import triangle_area

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, 6.00),
    (6, 8, 10, 24.00),
    (5, 12, 13, 30.00),
    (7, 8, 15, -1),
    (3, 4, 12, -1),
    (5, 5, 10, -1),
    (0, 3, 4, -1),
    (-3, 4, 5, -1),
    (3.5, 4.2, 5.1, 6.73),
])
def test_triangle_area(a, b, c, expected):
    result = triangle_area(a, b, c)
    assert isclose(result, expected, rel_tol=1e-2)

def test_triangle_area_invalid_input():
    assert triangle_area(1, 1, 3) == -1
    assert triangle_area(1, 2, -1) == -1
    assert triangle_area(-1, 2, 3) == -1