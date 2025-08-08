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

def test_right_angle_triangle_basic():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(1, 2, 3) == False

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 4, 5, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (1, 2, 3, False),
    (2, 3, 4, False),
    (5, 5, 5, False),
    (0, 0, 0, False),
    (1, 1, 1, False),
    (10, 6, 8, True),
    (6, 10, 8, True),
    (8, 6, 10, True)
])
def test_right_angle_triangle_parametrized(a, b, c, expected):
    result = right_angle_triangle(a, b, c)
    if a <= 0 or b <= 0 or c <= 0:
        assert result == False
    else:
        assert result == expected

@pytest.mark.parametrize("a,b,c", [
    (-1, 4, 5),
    (3, -4, 5),
    (3, 4, -5)
])
def test_right_angle_triangle_negative_inputs(a, b, c):
    assert right_angle_triangle(a, b, c) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(300, 400, 500) == True
    assert right_angle_triangle(30000, 40000, 50000) == True

def test_right_angle_triangle_floating_point():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(2.5, 6.0, 6.5) == True

def test_right_angle_triangle_zero_length():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 1, 1) == False

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(2, 2, 2) == False
    assert right_angle_triangle(10, 10, 10) == False