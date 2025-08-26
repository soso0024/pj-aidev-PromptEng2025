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

def right_angle_triangle(a, b, c):
    return abs(a*a - (b*b + c*c)) < 1e-9 or abs(b*b - (a*a + c*c)) < 1e-9 or abs(c*c - (a*a + b*b)) < 1e-9

def test_right_angle_triangle_valid_cases():
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(6, 8, 10) is True
    assert right_angle_triangle(5, 12, 13) is True

def test_right_angle_triangle_invalid_cases():
    assert right_angle_triangle(3, 4, 6) is False
    assert right_angle_triangle(5, 5, 7) is False
    assert right_angle_triangle(7, 8, 9) is False

@pytest.mark.parametrize("a, b, c, expected", [
    (0, 3, 4, True),
    (3, 0, 4, True),
    (3, 4, 0, True),
    (-3, 4, 5, False),
    (3, -4, 5, False),
    (3, 4, -5, False),
    (0, 0, 0, False),
    (1, 1, 1, False)
])
def test_right_angle_triangle_edge_cases(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

def test_right_angle_triangle_type_errors():
    with pytest.raises(TypeError):
        right_angle_triangle('a', 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 'b', 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, 'c')