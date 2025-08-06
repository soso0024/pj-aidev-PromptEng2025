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

def test_triangle_area_valid():
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(5, 12, 13) == 30.00
    assert triangle_area(8, 15, 17) == 60.00

def test_triangle_area_equilateral():
    assert triangle_area(5, 5, 5) == 10.83
    assert triangle_area(10, 10, 10) == 43.30

def test_triangle_area_isosceles():
    assert triangle_area(5, 5, 8) == 12.00
    assert triangle_area(10, 10, 12) == 48.00

@pytest.mark.parametrize("a, b, c", [
    (1, 2, 10),
    (0, 4, 5),
    (-1, 4, 5),
    (3, -4, 5),
    (3, 4, -5),
    (0, 0, 0),
])
def test_triangle_area_invalid(a, b, c):
    assert triangle_area(a, b, c) == -1

def test_triangle_area_decimal_sides():
    assert triangle_area(3.5, 4.5, 5.5) == 7.85
    assert triangle_area(2.5, 3.5, 4.5) == 4.35

def test_triangle_area_small_numbers():
    assert triangle_area(0.1, 0.1, 0.1) == 0.00
    assert triangle_area(0.5, 0.5, 0.5) == 0.11

def test_triangle_area_large_numbers():
    assert triangle_area(1000, 1000, 1000) == 433012.70
    assert triangle_area(100, 100, 150) == 4960.78

@pytest.mark.parametrize("a, b, c", [
    (3, 4, 7),
    (2, 3, 5),
    (1, 1, 3),
    (10, 2, 8),
])
def test_triangle_area_boundary_cases(a, b, c):
    assert triangle_area(a, b, c) == -1