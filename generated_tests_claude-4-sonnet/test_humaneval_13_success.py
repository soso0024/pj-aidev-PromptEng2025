# Test cases for HumanEval/13
# Generated using Claude API



def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    while b:
        a, b = b, a % b
    return a


# Generated test cases:
import pytest

def greatest_common_divisor(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

class TestGreatestCommonDivisor:
    
    @pytest.mark.parametrize("a,b,expected", [
        (12, 8, 4),
        (48, 18, 6),
        (17, 13, 1),
        (100, 25, 25),
        (7, 14, 7),
        (1, 1, 1),
        (0, 5, 5),
        (5, 0, 5),
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (21, 14, 7),
        (35, 15, 5),
        (144, 60, 12),
        (252, 105, 21),
        (1071, 462, 21),
        (2, 3, 1),
        (10, 15, 5),
        (24, 36, 12),
        (97, 89, 1)
    ])
    def test_gcd_positive_cases(self, a, b, expected):
        assert greatest_common_divisor(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (-12, 8, 4),
        (12, -8, 4),
        (-12, -8, 4),
        (-48, 18, 6),
        (48, -18, 6),
        (-48, -18, 6),
        (-17, 13, 1),
        (17, -13, 1),
        (-17, -13, 1),
        (-100, 25, 25),
        (100, -25, 25),
        (-100, -25, 25),
        (-5, 0, 5),
        (5, 0, 5),
        (0, -5, 5),
        (-1, 0, 1),
        (0, -1, 1)
    ])
    def test_gcd_negative_cases(self, a, b, expected):
        result = greatest_common_divisor(a, b)
        assert abs(result) == expected
    
    def test_gcd_large_numbers(self):
        assert greatest_common_divisor(123456789, 987654321) == 9
        assert greatest_common_divisor(1000000007, 1000000009) == 1
        assert greatest_common_divisor(2**20, 2**15) == 2**15
    
    def test_gcd_prime_numbers(self):
        assert greatest_common_divisor(7, 11) == 1
        assert greatest_common_divisor(13, 17) == 1
        assert greatest_common_divisor(23, 29) == 1
    
    def test_gcd_same_numbers(self):
        assert greatest_common_divisor(5, 5) == 5
        assert greatest_common_divisor(42, 42) == 42
        assert greatest_common_divisor(1, 1) == 1
        assert greatest_common_divisor(100, 100) == 100
    
    def test_gcd_one_as_argument(self):
        assert greatest_common_divisor(1, 5) == 1
        assert greatest_common_divisor(5, 1) == 1
        assert greatest_common_divisor(1, 100) == 1
        assert greatest_common_divisor(100, 1) == 1
    
    def test_gcd_multiples(self):
        assert greatest_common_divisor(6, 3) == 3
        assert greatest_common_divisor(15, 5) == 5
        assert greatest_common_divisor(20, 4) == 4
        assert greatest_common_divisor(100, 10) == 10
