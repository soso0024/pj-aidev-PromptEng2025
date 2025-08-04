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

def test_is_multiply_prime_basic():
    assert is_multiply_prime(30) == True  # 2 * 3 * 5
    assert is_multiply_prime(42) == True  # 2 * 3 * 7
    assert is_multiply_prime(66) == True  # 2 * 3 * 11

def test_is_multiply_prime_large():
    assert is_multiply_prime(230) == False  # Out of range (>100)
    assert is_multiply_prime(286) == False  # Out of range (>100)

def test_is_multiply_prime_false():
    assert is_multiply_prime(16) == False  # 2^4
    assert is_multiply_prime(25) == False  # 5^2
    assert is_multiply_prime(100) == False  # 2^2 * 5^2

def test_is_multiply_prime_edge_cases():
    assert is_multiply_prime(1) == False
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(3) == False
    assert is_multiply_prime(4) == False

@pytest.mark.parametrize("number,expected", [
    (8, False),  # 2 * 2 * 2
    (12, False),  # 2 * 2 * 3
    (18, False),  # 2 * 3 * 3
    (20, False),  # 2 * 2 * 5
    (24, False),  # 2 * 2 * 2 * 3
    (28, False),  # 2 * 2 * 7
    (35, False),  # 5 * 7
    (40, False),  # 2 * 2 * 2 * 5
    (44, False),  # 2 * 2 * 11
    (50, False),  # 2 * 5 * 5
    (98, False),  # 2 * 7 * 7
    (99, False),  # 3 * 3 * 11
])
def test_is_multiply_prime_parametrized(number, expected):
    assert is_multiply_prime(number) == expected

def test_is_multiply_prime_out_of_range():
    with pytest.raises(ValueError):
        is_multiply_prime(-1)
    with pytest.raises(ValueError):
        is_multiply_prime(0)
    with pytest.raises(ValueError):
        is_multiply_prime(101)
    with pytest.raises(ValueError):
        is_multiply_prime(1000000)

@pytest.mark.parametrize("invalid_input", [
    1.5,
    "30",
    None,
    [],
    {},
    True
])
def test_is_multiply_prime_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        is_multiply_prime(invalid_input)