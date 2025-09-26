# Test cases for HumanEval/75
# Generated using Claude API


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False


# Generated test cases:
import pytest

def is_multiply_prime(a):
    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True

    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False

def test_is_multiply_prime_example():
    assert is_multiply_prime(30) == True

def test_is_multiply_prime_smallest_case():
    assert is_multiply_prime(8) == True

def test_is_multiply_prime_same_primes():
    assert is_multiply_prime(27) == True

def test_is_multiply_prime_large_valid():
    assert is_multiply_prime(70) == True

def test_is_multiply_prime_invalid_cases():
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(3) == False
    assert is_multiply_prime(4) == False
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(6) == False
    assert is_multiply_prime(7) == False

def test_is_multiply_prime_two_primes_only():
    assert is_multiply_prime(6) == False
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(14) == False
    assert is_multiply_prime(15) == False

def test_is_multiply_prime_four_primes():
    assert is_multiply_prime(16) == False

def test_is_multiply_prime_composite_not_three_primes():
    assert is_multiply_prime(9) == False
    assert is_multiply_prime(12) == True
    assert is_multiply_prime(18) == True
    assert is_multiply_prime(20) == True

@pytest.mark.parametrize("input_val,expected", [
    (8, True),
    (12, True),
    (18, True),
    (20, True),
    (27, True),
    (28, True),
    (30, True),
    (44, True),
    (45, True),
    (50, True),
    (52, True),
    (63, True),
    (68, True),
    (70, True),
    (75, True),
    (76, True),
    (92, True),
    (98, True),
    (99, True),
    (1, False),
    (2, False),
    (3, False),
    (4, False),
    (5, False),
    (6, False),
    (7, False),
    (9, False),
    (10, False),
    (11, False),
    (13, False),
    (14, False),
    (15, False),
    (16, False),
    (17, False),
    (19, False),
    (21, False),
    (22, False),
    (23, False),
    (24, False),
    (25, False),
    (26, False),
    (29, False)
])
def test_is_multiply_prime_parametrized(input_val, expected):
    assert is_multiply_prime(input_val) == expected

def test_is_multiply_prime_edge_cases():
    assert is_multiply_prime(0) == False

def test_is_multiply_prime_boundary():
    assert is_multiply_prime(99) == True