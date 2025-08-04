# Test cases for HumanEval/157
# Generated using Claude API


def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''

    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b


# Generated test cases:
import pytest
import math

def test_right_angle_triangle_basic():
    assert right_angle_triangle(5, 4, 3) == True
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(4, 3, 5) == True

@pytest.mark.parametrize("a,b,c,expected", [
    (5, 4, 3, True),    # 3-4-5 triangle
    (13, 12, 5, True),  # 5-12-13 triangle
    (7, 8, 9, False),   # not a right triangle
    (0, 0, 0, False),   # zero case
    (1, 1, 1, False),   # equal sides, not right
    (10, 6, 8, True),   # 6-8-10 triangle
    (-3, 4, 5, False),  # negative number
    (0.5, 0.4, 0.3, True),  # decimal numbers
    (1000000, 800000, 600000, True),  # large numbers
    (2, 1, 2, False),   # invalid triangle
])
def test_right_angle_triangle_parametrized(a, b, c, expected):
    if any(x <= 0 for x in [a, b, c]):
        assert right_angle_triangle(a, b, c) == False
    else:
        assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_floating_point():
    assert abs(2.5**2 - (2.0**2 + 1.5**2)) < 1e-10
    assert right_angle_triangle(2.5, 2.0, 1.5) == True

def test_right_angle_triangle_non_right():
    assert right_angle_triangle(2, 2, 2) == False
    assert right_angle_triangle(3, 3, 3) == False

def test_right_angle_triangle_zero_values():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(5, 0, 4) == False
    assert right_angle_triangle(4, 5, 0) == False

def test_right_angle_triangle_negative_values():
    assert right_angle_triangle(-3, -4, -5) == False
    assert right_angle_triangle(-5, 4, 3) == False

def test_right_angle_triangle_very_large_values():
    assert right_angle_triangle(1000000, 800000, 600000) == True
    assert right_angle_triangle(1000001, 800000, 600000) == False