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

def test_multiply_prime_basic():
    assert is_multiply_prime(8) == True  # 2 * 2 * 2
    assert is_multiply_prime(30) == True  # 2 * 3 * 5
    assert is_multiply_prime(105) == True  # 3 * 5 * 7
    
def test_multiply_prime_false_cases():
    assert is_multiply_prime(16) == False  # 2 * 2 * 2 * 2
    assert is_multiply_prime(25) == False  # 5 * 5
    assert is_multiply_prime(100) == False  # 2 * 2 * 5 * 5
    
def test_multiply_prime_edge_cases():
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(4) == False
    
@pytest.mark.parametrize("input_val,expected", [
    (8, True),
    (30, True),
    (105, True),
    (16, False),
    (25, False),
    (100, False),
    (1, False),
    (2, False),
    (4, False),
    (1000, False),
    (210, False),
    (49, False),
    (125, True)  # Changed to True since 5 * 5 * 5 is a product of 3 prime numbers
])
def test_multiply_prime_parametrized(input_val, expected):
    assert is_multiply_prime(input_val) == expected

@pytest.mark.parametrize("input_val", [-1, 0, -100])
def test_multiply_prime_negative_numbers(input_val):
    assert is_multiply_prime(input_val) == False

def test_multiply_prime_large_numbers():
    assert is_multiply_prime(1000000) == False
    assert is_multiply_prime(999999) == False

@pytest.mark.parametrize("input_val", [2.5, 3.14, -1.5])
def test_multiply_prime_float_numbers(input_val):
    assert is_multiply_prime(input_val) == False