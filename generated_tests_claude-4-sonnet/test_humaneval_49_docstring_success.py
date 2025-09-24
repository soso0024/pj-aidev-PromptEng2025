# Test cases for HumanEval/49
# Generated using Claude API



def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """

    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret


# Generated test cases:
import pytest

def modp(n: int, p: int):
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret

class TestModp:
    
    @pytest.mark.parametrize("n,p,expected", [
        (3, 5, 3),
        (1101, 101, 2),
        (0, 101, 1),
        (3, 11, 8),
        (100, 101, 1),
    ])
    def test_docstring_examples(self, n, p, expected):
        assert modp(n, p) == expected
    
    def test_zero_exponent(self):
        assert modp(0, 7) == 1
        assert modp(0, 2) == 1
        assert modp(0, 1000) == 1
    
    def test_small_values(self):
        assert modp(1, 3) == 2
        assert modp(2, 3) == 1
        assert modp(1, 2) == 0
        assert modp(2, 2) == 0
        assert modp(3, 2) == 0
    
    def test_modulo_one(self):
        assert modp(0, 1) == 1
        assert modp(1, 1) == 0
        assert modp(10, 1) == 0
        assert modp(100, 1) == 0
    
    def test_large_values(self):
        assert modp(10, 7) == 2
        assert modp(20, 13) == 9
        assert modp(50, 17) == 4
    
    def test_prime_modulus(self):
        assert modp(5, 7) == 4
        assert modp(6, 7) == 1
        assert modp(4, 13) == 3
        assert modp(12, 13) == 1
    
    def test_power_of_two_modulus(self):
        assert modp(3, 8) == 0
        assert modp(4, 16) == 0
        assert modp(2, 4) == 0
        assert modp(1, 4) == 2
    
    def test_fermat_little_theorem_cases(self):
        assert modp(6, 7) == 1
        assert modp(10, 11) == 1
        assert modp(12, 13) == 1
    
    def test_negative_zero_edge_cases(self):
        assert modp(0, 2) == 1
        assert modp(0, 3) == 1
        assert modp(0, 100) == 1