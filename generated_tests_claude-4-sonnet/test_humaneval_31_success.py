# Test cases for HumanEval/31
# Generated using Claude API



def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """

    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True


# Generated test cases:
import pytest

def is_prime(n):
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True

class TestIsPrime:
    
    def test_negative_numbers(self):
        assert is_prime(-1) == False
        assert is_prime(-5) == False
        assert is_prime(-100) == False
    
    def test_zero_and_one(self):
        assert is_prime(0) == False
        assert is_prime(1) == False
    
    def test_small_primes(self):
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(7) == True
        assert is_prime(11) == True
        assert is_prime(13) == True
        assert is_prime(17) == True
        assert is_prime(19) == True
        assert is_prime(23) == True
    
    def test_small_composites(self):
        assert is_prime(4) == False
        assert is_prime(6) == False
        assert is_prime(8) == False
        assert is_prime(9) == False
        assert is_prime(10) == False
        assert is_prime(12) == False
        assert is_prime(14) == False
        assert is_prime(15) == False
        assert is_prime(16) == False
        assert is_prime(18) == False
        assert is_prime(20) == False
    
    def test_larger_primes(self):
        assert is_prime(29) == True
        assert is_prime(31) == True
        assert is_prime(37) == True
        assert is_prime(41) == True
        assert is_prime(43) == True
        assert is_prime(47) == True
        assert is_prime(53) == True
        assert is_prime(59) == True
        assert is_prime(61) == True
        assert is_prime(67) == True
        assert is_prime(71) == True
        assert is_prime(73) == True
        assert is_prime(79) == True
        assert is_prime(83) == True
        assert is_prime(89) == True
        assert is_prime(97) == True
    
    def test_larger_composites(self):
        assert is_prime(25) == False
        assert is_prime(27) == False
        assert is_prime(33) == False
        assert is_prime(35) == False
        assert is_prime(39) == False
        assert is_prime(49) == False
        assert is_prime(51) == False
        assert is_prime(55) == False
        assert is_prime(57) == False
        assert is_prime(63) == False
        assert is_prime(65) == False
        assert is_prime(69) == False
        assert is_prime(75) == False
        assert is_prime(77) == False
        assert is_prime(81) == False
        assert is_prime(85) == False
        assert is_prime(87) == False
        assert is_prime(91) == False
        assert is_prime(93) == False
        assert is_prime(95) == False
        assert is_prime(99) == False
    
    def test_perfect_squares(self):
        assert is_prime(4) == False
        assert is_prime(9) == False
        assert is_prime(16) == False
        assert is_prime(25) == False
        assert is_prime(36) == False
        assert is_prime(49) == False
        assert is_prime(64) == False
        assert is_prime(81) == False
        assert is_prime(100) == False
    
    @pytest.mark.parametrize("n,expected", [
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True)
    ])
    def test_parametrized_small_numbers(self, n, expected):
        assert is_prime(n) == expected
    
    @pytest.mark.parametrize("n", [-10, -5, -1, 0, 1])
    def test_parametrized_non_prime_edge_cases(self, n):
        assert is_prime(n) == False
    
    def test_float_inputs(self):
        with pytest.raises(TypeError):
            is_prime(2.5)
        with pytest.raises(TypeError):
            is_prime(3.0)
    
    def test_string_inputs(self):
        with pytest.raises(TypeError):
            is_prime("2")
        with pytest.raises(TypeError):
            is_prime("prime")
    
    def test_none_input(self):
        with pytest.raises(TypeError):
            is_prime(None)
    
    def test_boolean_inputs(self):
        assert is_prime(True) == False
        assert is_prime(False) == False
