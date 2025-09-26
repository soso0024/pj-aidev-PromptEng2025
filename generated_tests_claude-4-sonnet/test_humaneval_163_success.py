# Test cases for HumanEval/163
# Generated using Claude API


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


# Generated test cases:
import pytest

def generate_integers(a, b):
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))
    return [i for i in range(int(lower), int(upper)+1) if i % 2 == 0]

class TestGenerateIntegers:
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 8, [2, 4, 6, 8]),
        (8, 2, [2, 4, 6, 8]),
        (3, 7, [4, 6]),
        (7, 3, [4, 6]),
        (1, 9, [2, 4, 6, 8]),
        (9, 1, [2, 4, 6, 8]),
        (2, 2, [2]),
        (8, 8, [8]),
        (4, 4, [4]),
        (3, 3, []),
        (5, 5, []),
        (7, 7, []),
    ])
    def test_normal_cases(self, a, b, expected):
        assert generate_integers(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 10, [2, 4, 6, 8]),
        (-5, 15, [2, 4, 6, 8]),
        (-10, -5, []),
        (10, 15, []),
        (1, 1, []),
        (0, 0, []),
        (-1, -1, []),
    ])
    def test_boundary_cases(self, a, b, expected):
        assert generate_integers(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (9, 10, []),
        (10, 9, []),
        (15, 20, []),
        (-10, 0, []),
        (-5, 1, []),
        (0, 1, []),
        (1, 0, []),
    ])
    def test_edge_cases(self, a, b, expected):
        assert generate_integers(a, b) == expected
    
    def test_same_values(self):
        assert generate_integers(6, 6) == [6]
        assert generate_integers(1, 1) == []
        assert generate_integers(9, 9) == []
    
    def test_negative_values(self):
        assert generate_integers(-5, -3) == []
        assert generate_integers(-10, -8) == []
        assert generate_integers(-1, 5) == [2, 4]
    
    def test_large_values(self):
        assert generate_integers(100, 200) == []
        assert generate_integers(1000, 2000) == []
        assert generate_integers(-1000, 1000) == [2, 4, 6, 8]
    
    def test_float_values(self):
        assert generate_integers(2.5, 7.8) == [2, 4, 6]
        assert generate_integers(1.1, 8.9) == [2, 4, 6, 8]
    
    def test_zero_values(self):
        assert generate_integers(0, 0) == []
        assert generate_integers(0, 5) == [2, 4]
        assert generate_integers(5, 0) == [2, 4]