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

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 4, 5, 6.0),  # standard right triangle
    (5, 5, 5, 10.83),  # equilateral triangle
    (8, 15, 17, 60.0),  # larger triangle
    (1, 1, 3, -1),  # invalid triangle - sum of two sides <= third side
    (3, 1, 1, -1),  # invalid triangle
    (1, 3, 1, -1),  # invalid triangle
    (0, 4, 5, -1),  # zero side length
    (-1, 4, 5, -1),  # negative side length
    (2.5, 3.5, 4.5, 4.35),  # decimal side lengths
    (1e-10, 1e-10, 1e-10, 0),  # very small triangle
    (10000, 10000, 10000, 43301270.19),  # very large triangle
])
def test_triangle_area(a, b, c, expected):
    result = triangle_area(a, b, c)
    assert result == expected

@pytest.mark.parametrize("a,b,c", [
    ("a", 4, 5),  # non-numeric input
    (3, "b", 5),
    (3, 4, "c"),
    (None, 4, 5),  # None input
    (3, None, 5),
    (3, 4, None),
    ([], 4, 5),  # invalid type input
    (3, {}, 5),
    (3, 4, set()),
])
def test_triangle_area_invalid_input(a, b, c):
    with pytest.raises((TypeError, ValueError)):
        triangle_area(a, b, c)

def test_triangle_area_no_args():
    with pytest.raises(TypeError):
        triangle_area()

def test_triangle_area_too_many_args():
    with pytest.raises(TypeError):
        triangle_area(1, 2, 3, 4)