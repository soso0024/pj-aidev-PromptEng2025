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

def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

class TestGreatestCommonDivisor:
    
    @pytest.mark.parametrize("a,b,expected", [
        (3, 5, 1),
        (25, 15, 5),
        (12, 8, 4),
        (48, 18, 6),
        (100, 25, 25),
        (17, 13, 1),
        (54, 24, 6),
        (1071, 462, 21),
    ])
    def test_positive_integers(self, a, b, expected):
        assert greatest_common_divisor(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 5, 5),
        (7, 0, 7),
        (0, 0, 0),
    ])
    def test_with_zero(self, a, b, expected):
        assert greatest_common_divisor(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (-12, 8, 4),
        (12, -8, 4),
        (-12, -8, 4),
        (-25, 15, 5),
        (25, -15, 5),
        (-25, -15, 5),
    ])
    def test_negative_integers(self, a, b, expected):
        result = greatest_common_divisor(a, b)
        assert abs(result) == expected
    
    @pytest.mark.parametrize("a,b", [
        (1, 1),
        (7, 7),
        (100, 100),
        (-5, -5),
    ])
    def test_identical_numbers(self, a, b):
        result = greatest_common_divisor(a, b)
        assert abs(result) == abs(a)
    
    @pytest.mark.parametrize("a,b", [
        (1, 17),
        (23, 1),
        (1, 1000),
        (999, 1),
    ])
    def test_with_one(self, a, b):
        assert greatest_common_divisor(a, b) == 1
    
    def test_large_numbers(self):
        assert greatest_common_divisor(123456789, 987654321) == 9
        assert greatest_common_divisor(1000000007, 1000000009) == 1
    
    def test_prime_numbers(self):
        assert greatest_common_divisor(17, 19) == 1
        assert greatest_common_divisor(97, 101) == 1
        assert greatest_common_divisor(2, 3) == 1
    
    def test_powers_of_two(self):
        assert greatest_common_divisor(16, 32) == 16
        assert greatest_common_divisor(64, 128) == 64
        assert greatest_common_divisor(8, 12) == 4
