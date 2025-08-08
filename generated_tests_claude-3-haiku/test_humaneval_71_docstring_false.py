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
from math import isclose
import pytest
from triangle_area import triangle_area

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, 6.00),
    (1, 2, 10, -1),
    (5, 12, 13, 30.00),
    (7, 8, 9, -1),
    (6, 6, 6, 14.70),
    (0, 4, 5, -1),
    (-1, 2, 3, -1),
    (2.5, 3.5, 4.0, 5.83),
])
def test_triangle_area(a, b, c, expected):
    assert isclose(triangle_area(a, b, c), expected, rel_tol=1e-2)