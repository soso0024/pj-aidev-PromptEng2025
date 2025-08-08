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

def test_multiply_prime_30():
    assert is_multiply_prime(30) == True

def test_multiply_prime_42():
    assert is_multiply_prime(42) == True

def test_multiply_prime_66():
    assert is_multiply_prime(66) == True

def test_multiply_prime_not_product_of_three_primes():
    assert is_multiply_prime(20) == True
    assert is_multiply_prime(25) == False
    assert is_multiply_prime(35) == False

def test_multiply_prime_prime_numbers():
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(3) == False
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(7) == False

def test_multiply_prime_product_of_two_primes():
    assert is_multiply_prime(6) == False
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(15) == False

def test_multiply_prime_non_prime_numbers():
    assert is_multiply_prime(4) == False
    assert is_multiply_prime(8) == False
    assert is_multiply_prime(9) == False

def test_multiply_prime_edge_cases():
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(0) == False
    assert is_multiply_prime(100) == False

@pytest.mark.parametrize("number,expected", [
    (30, True),   # 2 * 3 * 5
    (42, True),   # 2 * 3 * 7
    (66, True),   # 2 * 3 * 11
    (70, True),   # 2 * 5 * 7
    (20, True),   # 2 * 2 * 5
    (25, False),  # 5 * 5
    (12, False),  # 2 * 2 * 3 (not three distinct primes)
    (1, False),
    (97, False),
    (0, False)
])
def test_multiply_prime_parametrized(number, expected):
    assert is_multiply_prime(number) == expected

def test_multiply_prime_larger_than_limit():
    assert is_multiply_prime(101) == False
    assert is_multiply_prime(150) == False