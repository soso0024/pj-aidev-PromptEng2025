# Test cases for HumanEval/97
# Generated using Claude API


def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """

    return abs(a % 10) * abs(b % 10)


# Generated test cases:
import pytest

def multiply(a, b):
    return abs(a % 10) * abs(b % 10)

class TestMultiply:
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0),
        (1, 1, 1),
        (2, 3, 6),
        (5, 4, 20),
        (9, 9, 81),
        (10, 20, 0),
        (11, 22, 2),
        (15, 27, 35),
        (123, 456, 18),
        (999, 888, 72),
    ])
    def test_positive_integers(self, a, b, expected):
        assert multiply(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (-1, -1, 81),
        (-2, -3, 56),
        (-5, -4, 30),
        (-9, -9, 1),
        (-10, -20, 0),
        (-11, -22, 72),
        (-15, -27, 15),
        (-123, -456, 28),
        (-999, -888, 2),
    ])
    def test_negative_integers(self, a, b, expected):
        assert multiply(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (5, -3, 35),
        (-7, 4, 12),
        (12, -8, 4),
        (-25, 6, 30),
        (100, -200, 0),
        (-150, 37, 0),
        (999, -111, 81),
        (-444, 777, 42),
    ])
    def test_mixed_sign_integers(self, a, b, expected):
        assert multiply(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 5, 0),
        (5, 0, 0),
        (0, -5, 0),
        (-5, 0, 0),
        (10, 7, 0),
        (7, 10, 0),
        (100, 200, 0),
        (-100, -200, 0),
        (1000, 2000, 0),
    ])
    def test_zero_cases(self, a, b, expected):
        assert multiply(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 2),
        (2, 1, 2),
        (3, 7, 21),
        (7, 3, 21),
        (-4, 6, 36),
        (6, -4, 36),
        (-8, -9, 2),
        (-9, -8, 2),
    ])
    def test_single_digit_numbers(self, a, b, expected):
        assert multiply(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (12345, 67890, 0),
        (98765, 43210, 0),
        (11111, 22222, 2),
        (13579, 24681, 9),
        (-12345, -67890, 0),
        (-98765, -43210, 0),
        (12345, -67890, 0),
        (-13579, 24681, 1),
    ])
    def test_large_numbers(self, a, b, expected):
        assert multiply(a, b) == expected
    
    def test_very_large_numbers(self):
        assert multiply(123456789, 987654321) == 9
        assert multiply(-123456789, -987654321) == 9
        assert multiply(1000000000, 2000000000) == 0
        assert multiply(-1000000000, 2000000000) == 0
    
    def test_edge_case_modulo_ten(self):
        assert multiply(10, 10) == 0
        assert multiply(20, 30) == 0
        assert multiply(100, 200) == 0
        assert multiply(-10, -10) == 0
        assert multiply(-20, -30) == 0
        assert multiply(10, -20) == 0