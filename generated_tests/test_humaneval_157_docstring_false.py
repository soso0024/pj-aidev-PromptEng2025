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

def test_right_angle_triangle_345():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_123():
    assert right_angle_triangle(1, 2, 3) == False

@pytest.mark.parametrize("a,b,c,expected", [
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (20, 21, 29, False),
    (1, 1, 1, False),
    (2, 3, 4, False),
    (10, 10, 10, False),
    (5, 5, 8, False),
])
def test_right_angle_triangle_various_cases(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize("a,b,c", [
    (0, 4, 5),
    (3, 0, 5),
    (3, 4, 0),
    (0, 0, 0)
])
def test_right_angle_triangle_with_zero(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        assert right_angle_triangle(a, b, c) == False

@pytest.mark.parametrize("a,b,c", [
    (-3, 4, 5),
    (3, -4, 5),
    (3, 4, -5),
    (-3, -4, -5)
])
def test_right_angle_triangle_negative_numbers(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        assert right_angle_triangle(a, b, c) == False

def test_right_angle_triangle_floating_point():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(300, 400, 500) == True
    assert right_angle_triangle(3000, 4000, 5000) == True