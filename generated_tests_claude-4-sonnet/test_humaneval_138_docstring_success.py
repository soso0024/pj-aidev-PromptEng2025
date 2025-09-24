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
    
    def test_example_cases(self):
        assert is_equal_to_sum_even(4) == False
        assert is_equal_to_sum_even(6) == False
        assert is_equal_to_sum_even(8) == True
    
    @pytest.mark.parametrize("n,expected", [
        (0, False),
        (1, False),
        (2, False),
        (3, False),
        (4, False),
        (5, False),
        (6, False),
        (7, False),
        (8, True),
        (9, False),
        (10, True),
        (11, False),
        (12, True),
        (13, False),
        (14, True),
        (15, False),
        (16, True),
        (18, True),
        (20, True),
        (100, True),
        (101, False),
        (1000, True),
        (1001, False)
    ])
    def test_various_numbers(self, n, expected):
        assert is_equal_to_sum_even(n) == expected
    
    def test_negative_numbers(self):
        assert is_equal_to_sum_even(-1) == False
        assert is_equal_to_sum_even(-2) == False
        assert is_equal_to_sum_even(-8) == False
        assert is_equal_to_sum_even(-10) == False
    
    def test_large_numbers(self):
        assert is_equal_to_sum_even(10000) == True
        assert is_equal_to_sum_even(10001) == False
        assert is_equal_to_sum_even(999998) == True
        assert is_equal_to_sum_even(999999) == False
    
    def test_boundary_cases(self):
        assert is_equal_to_sum_even(8) == True
        assert is_equal_to_sum_even(6) == False
        assert is_equal_to_sum_even(7) == False
        assert is_equal_to_sum_even(9) == False
