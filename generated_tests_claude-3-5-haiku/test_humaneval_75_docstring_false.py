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
        if n < 2:
            return False
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i): continue
        for j in range(i, 101):
            if not is_prime(j): continue
            for k in range(j, 101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False

def test_is_multiply_prime_valid_cases():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(42) == True
    assert is_multiply_prime(60) == True
    assert is_multiply_prime(90) == True

def test_is_multiply_prime_invalid_cases():
    assert is_multiply_prime(31) == False
    assert is_multiply_prime(17) == False
    assert is_multiply_prime(100) == False

def test_is_multiply_prime_edge_cases():
    assert is_multiply_prime(2 * 3 * 5) == True
    assert is_multiply_prime(2 * 2 * 7) == True
    assert is_multiply_prime(2 * 3 * 7) == True

@pytest.mark.parametrize("input,expected", [
    (30, True),
    (42, True),
    (60, True),
    (90, True),
    (31, False),
    (17, False),
    (100, False),
    (2 * 3 * 5, True),
    (2 * 2 * 7, True),
    (2 * 3 * 7, True)
])
def test_is_multiply_prime_parametrized(input, expected):
    assert is_multiply_prime(input) == expected