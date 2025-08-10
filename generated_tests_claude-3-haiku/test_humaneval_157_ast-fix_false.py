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

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, True),
    (6, 8, 10, True),
    (5, 12, 13, True),
    (8, 15, 17, True),
    (7, 24, 25, True),
    (0, 0, 0, False),
    (-3, 4, 5, False),
    (3, -4, 5, False),
    (3, 4, -5, False),
    (3.14, 4.0, 5.0, True),
    (3.14, 4.0, 5.1, False),
    ('a', 4, 5, TypeError),
    (3, 'b', 5, TypeError),
    (3, 4, 'c', TypeError)
])
def test_right_angle_triangle(a, b, c, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            assert right_angle_triangle(a, b, c)
    else:
        assert right_angle_triangle(a, b, c) == expected

def right_angle_triangle(a, b, c):
    return a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2