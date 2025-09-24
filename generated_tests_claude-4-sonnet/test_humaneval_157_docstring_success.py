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
        (1, 2, 3, False),
        (2, 3, 4, False),
        (1, 1, 1, False),
        (2, 2, 2, False),
        (6, 8, 9, False),
        (10, 10, 10, False)
    ])
    def test_right_angle_triangle_parametrized(self, a, b, c, expected):
        assert right_angle_triangle(a, b, c) == expected
    
    def test_classic_345_triangle(self):
        assert right_angle_triangle(3, 4, 5) == True
    
    def test_classic_345_triangle_different_order(self):
        assert right_angle_triangle(5, 4, 3) == True
        assert right_angle_triangle(4, 3, 5) == True
    
    def test_pythagorean_triples(self):
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(9, 40, 41) == True
    
    def test_not_right_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(5, 6, 7) == False
    
    def test_equilateral_triangle(self):
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(5, 5, 5) == False
        assert right_angle_triangle(10, 10, 10) == False
    
    def test_isosceles_triangle(self):
        assert right_angle_triangle(2, 2, 3) == False
        assert right_angle_triangle(5, 5, 7) == False
    
    def test_zero_values(self):
        assert right_angle_triangle(0, 0, 0) == True
        assert right_angle_triangle(0, 3, 4) == False
        assert right_angle_triangle(3, 0, 4) == False
        assert right_angle_triangle(3, 4, 0) == False
    
    def test_negative_values(self):
        assert right_angle_triangle(-3, -4, -5) == True
        assert right_angle_triangle(-3, 4, 5) == True
        assert right_angle_triangle(3, -4, 5) == True
        assert right_angle_triangle(3, 4, -5) == True
        assert right_angle_triangle(-1, -2, -3) == False
    
    def test_decimal_values(self):
        assert right_angle_triangle(1.5, 2.0, 2.5) == True
        assert right_angle_triangle(0.6, 0.8, 1.0) == True
        assert right_angle_triangle(1.1, 1.2, 1.3) == False
    
    def test_large_values(self):
        assert right_angle_triangle(300, 400, 500) == True
        assert right_angle_triangle(3000, 4000, 5000) == True
        assert right_angle_triangle(1000, 1001, 1002) == False
    
    def test_single_unit_values(self):
        assert right_angle_triangle(1, 1, 1.414213562373095) == False
        assert right_angle_triangle(1, 0, 1) == True
