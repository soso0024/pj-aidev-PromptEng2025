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
import math

def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

class TestTriangleArea:
    
    def test_valid_triangle_basic(self):
        assert triangle_area(3, 4, 5) == 6.0
    
    def test_valid_triangle_equilateral(self):
        assert triangle_area(5, 5, 5) == 10.83
    
    def test_valid_triangle_isosceles(self):
        assert triangle_area(5, 5, 6) == 12.0
    
    def test_valid_triangle_scalene(self):
        assert triangle_area(6, 8, 10) == 24.0
    
    def test_valid_triangle_decimal_sides(self):
        assert triangle_area(3.5, 4.2, 5.1) == 7.29
    
    def test_valid_triangle_small_area(self):
        assert triangle_area(1, 1, 1) == 0.43
    
    def test_invalid_triangle_sum_equals_third_side(self):
        assert triangle_area(1, 2, 3) == -1
    
    def test_invalid_triangle_sum_less_than_third_side(self):
        assert triangle_area(1, 2, 4) == -1
    
    def test_invalid_triangle_zero_side(self):
        assert triangle_area(0, 1, 1) == -1
    
    def test_invalid_triangle_negative_side(self):
        assert triangle_area(-1, 2, 2) == -1
    
    def test_invalid_triangle_all_zero(self):
        assert triangle_area(0, 0, 0) == -1
    
    def test_invalid_triangle_two_sides_equal_third(self):
        assert triangle_area(5, 5, 10) == -1
    
    def test_invalid_triangle_one_side_much_larger(self):
        assert triangle_area(1, 1, 10) == -1
    
    @pytest.mark.parametrize("a,b,c,expected", [
        (3, 4, 5, 6.0),
        (5, 12, 13, 30.0),
        (8, 15, 17, 60.0),
        (7, 24, 25, 84.0)
    ])
    def test_right_triangles(self, a, b, c, expected):
        assert triangle_area(a, b, c) == expected
    
    @pytest.mark.parametrize("a,b,c", [
        (1, 1, 2),
        (2, 3, 5),
        (1, 10, 12),
        (0.5, 0.5, 1)
    ])
    def test_invalid_triangles_parametrized(self, a, b, c):
        assert triangle_area(a, b, c) == -1
    
    def test_large_triangle(self):
        assert triangle_area(100, 200, 250) == 9499.18
    
    def test_very_small_triangle(self):
        assert triangle_area(0.1, 0.1, 0.1) == 0.00
    
    def test_triangle_with_floating_point_precision(self):
        result = triangle_area(3.333, 4.444, 5.555)
        assert isinstance(result, float)
        assert result > 0