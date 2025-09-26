# Test cases for HumanEval/138
# Generated using Claude API


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    return n%2 == 0 and n >= 8


# Generated test cases:
import pytest

def is_equal_to_sum_even(n):
    return n%2 == 0 and n >= 8

class TestIsEqualToSumEven:
    
    @pytest.mark.parametrize("n,expected", [
        (8, True),
        (10, True),
        (12, True),
        (100, True),
        (1000, True),
    ])
    def test_even_numbers_greater_equal_8(self, n, expected):
        assert is_equal_to_sum_even(n) == expected
    
    @pytest.mark.parametrize("n,expected", [
        (0, False),
        (2, False),
        (4, False),
        (6, False),
    ])
    def test_even_numbers_less_than_8(self, n, expected):
        assert is_equal_to_sum_even(n) == expected
    
    @pytest.mark.parametrize("n,expected", [
        (1, False),
        (3, False),
        (5, False),
        (7, False),
        (9, False),
        (11, False),
        (13, False),
        (99, False),
        (101, False),
    ])
    def test_odd_numbers(self, n, expected):
        assert is_equal_to_sum_even(n) == expected
    
    @pytest.mark.parametrize("n,expected", [
        (-2, False),
        (-4, False),
        (-8, False),
        (-10, False),
        (-1, False),
        (-3, False),
        (-7, False),
        (-9, False),
    ])
    def test_negative_numbers(self, n, expected):
        assert is_equal_to_sum_even(n) == expected
    
    def test_boundary_values(self):
        assert is_equal_to_sum_even(8) == True
        assert is_equal_to_sum_even(6) == False
        assert is_equal_to_sum_even(7) == False
        assert is_equal_to_sum_even(9) == False
    
    def test_zero(self):
        assert is_equal_to_sum_even(0) == False
    
    @pytest.mark.parametrize("n", [
        8.0,
        10.0,
        6.0,
        7.0,
    ])
    def test_float_inputs(self, n):
        if n >= 8 and int(n) % 2 == 0:
            assert is_equal_to_sum_even(n) == True
        else:
            assert is_equal_to_sum_even(n) == False
