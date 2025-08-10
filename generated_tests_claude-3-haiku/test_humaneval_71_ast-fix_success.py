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

def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)

def test_triangle_area_valid_triangle():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(5, 12, 13) == 30.00
    assert triangle_area(7, 8, 9) == 26.83

def test_triangle_area_invalid_triangle():
    assert triangle_area(1, 2, 5) == -1
    assert triangle_area(3, 4, 12) == -1
    assert triangle_area(6, 6, 12) == -1

@pytest.mark.parametrize("a, b, c, expected", [
    (3.0, 4.0, 5.0, 6.00),
    (5.0, 12.0, 13.0, 30.00),
    (7.0, 8.0, 9.0, 26.83),
    (1.0, 2.0, 5.0, -1),
    (3.0, 4.0, 12.0, -1),
    (6.0, 6.0, 12.0, -1),
    (0.0, 4.0, 5.0, -1),
    (3.0, 0.0, 5.0, -1),
    (3.0, 4.0, 0.0, -1),
    (-3.0, 4.0, 5.0, -1),
    (3.0, -4.0, 5.0, -1),
    (3.0, 4.0, -5.0, -1)
])
def test_triangle_area_parametrized(a, b, c, expected):
    assert triangle_area(a, b, c) == expected