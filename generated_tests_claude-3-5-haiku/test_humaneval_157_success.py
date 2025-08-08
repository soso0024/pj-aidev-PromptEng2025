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

def right_angle_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b

def test_right_angle_triangle_valid_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(5, 4, 3) == True

def test_right_angle_triangle_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(7, 8, 9) == False

def test_right_angle_triangle_zero_values():
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_negative_values():
    assert right_angle_triangle(-3, -4, -5) == False

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 4, 5, True),
    (5, 3, 4, True),
    (4, 5, 3, True),
    (1, 2, 3, False),
    (0, 0, 0, False),
    (-3, -4, -5, False)
])
def test_right_angle_triangle_parametrized(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_floating_point():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(3.1, 4.1, 5.2) == False