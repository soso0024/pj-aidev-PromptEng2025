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
    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b

class TestRightAngleTriangle:
    
    @pytest.mark.parametrize("a,b,c,expected", [
        (3, 4, 5, True),
        (5, 3, 4, True),
        (4, 5, 3, True),
        (5, 12, 13, True),
        (13, 5, 12, True),
        (12, 13, 5, True),
        (8, 15, 17, True),
        (7, 24, 25, True),
        (20, 21, 29, True),
        (9, 40, 41, True)
    ])
    def test_valid_right_triangles(self, a, b, c, expected):
        assert right_angle_triangle(a, b, c) == expected
    
    @pytest.mark.parametrize("a,b,c,expected", [
        (1, 2, 3, False),
        (2, 3, 4, False),
        (1, 1, 1, False),
        (2, 2, 2, False),
        (6, 8, 9, False),
        (10, 10, 10, False),
        (1, 2, 4, False),
        (5, 5, 5, False)
    ])
    def test_invalid_right_triangles(self, a, b, c, expected):
        assert right_angle_triangle(a, b, c) == expected
    
    @pytest.mark.parametrize("a,b,c,expected", [
        (0, 0, 0, True),
        (0, 3, 4, False),
        (3, 0, 4, False),
        (3, 4, 0, False),
        (0, 0, 5, False),
        (0, 5, 0, False),
        (5, 0, 0, False)
    ])
    def test_zero_values(self, a, b, c, expected):
        assert right_angle_triangle(a, b, c) == expected
    
    @pytest.mark.parametrize("a,b,c,expected", [
        (-3, -4, -5, True),
        (-5, -3, -4, True),
        (-4, -5, -3, True),
        (3, -4, 5, True),
        (-3, 4, 5, True),
        (3, 4, -5, True),
        (-3, -4, 5, True),
        (-1, -2, -3, False)
    ])
    def test_negative_values(self, a, b, c, expected):
        assert right_angle_triangle(a, b, c) == expected
    
    @pytest.mark.parametrize("a,b,c,expected", [
        (0.3, 0.4, 0.5, True),
        (1.5, 2.0, 2.5, True),
        (0.6, 0.8, 1.0, True),
        (0.1, 0.2, 0.3, False),
        (1.1, 1.2, 1.3, False)
    ])
    def test_decimal_values(self, a, b, c, expected):
        assert right_angle_triangle(a, b, c) == expected
    
    def test_large_numbers(self):
        assert right_angle_triangle(300, 400, 500) == True
        assert right_angle_triangle(3000, 4000, 5000) == True
        assert right_angle_triangle(1000000, 1000001, 1000002) == False
    
    def test_very_small_numbers(self):
        assert right_angle_triangle(0.003, 0.004, 0.005) == False
        assert right_angle_triangle(0.0001, 0.0002, 0.0003) == False