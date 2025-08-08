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
    assert is_multiply_prime(30) == True  # 2 * 3 * 5

def test_multiply_prime_42():
    assert is_multiply_prime(42) == True  # 2 * 3 * 7

def test_multiply_prime_66():
    assert is_multiply_prime(66) == True  # 2 * 3 * 11

@pytest.mark.parametrize("input_num,expected", [
    (1, False),    # Too small
    (4, False),    # Not product of 3 primes
    (6, False),    # Product of 2 primes only
    (8, False),    # Product of 2 * 2 * 2
    (12, False),   # Product of 2 * 2 * 3
    (25, False),   # Product of 5 * 5
    (99, False),   # Product of 3 * 3 * 11
    (100, False),  # Product of 2 * 2 * 5 * 5
])
def test_multiply_prime_false_cases(input_num, expected):
    result = is_multiply_prime(input_num)
    assert result == expected, f"Failed for input {input_num}, got {result}, expected {expected}"

@pytest.mark.parametrize("input_num,expected", [
    (30, True),   # 2 * 3 * 5
    (42, True),   # 2 * 3 * 7
    (66, True),   # 2 * 3 * 11
    (70, True),   # 2 * 5 * 7
    (78, True),   # 2 * 3 * 13
])
def test_multiply_prime_true_cases(input_num, expected):
    result = is_multiply_prime(input_num)
    assert result == expected, f"Failed for input {input_num}, got {result}, expected {expected}"

def test_multiply_prime_edge_cases():
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(3) == False
    assert is_multiply_prime(97) == False
    assert is_multiply_prime(98) == False
    assert is_multiply_prime(99) == False

@pytest.mark.parametrize("input_num", [
    -1, 0, 101, 150, 1000
])
def test_multiply_prime_out_of_range(input_num):
    result = is_multiply_prime(input_num)
    assert result == False, f"Failed for input {input_num}, got {result}, expected False"

def test_multiply_prime_special_cases():
    assert is_multiply_prime(90) == True  # 2 * 3 * 5 * 3 (valid as it contains 2 * 3 * 5)
    assert is_multiply_prime(50) == False  # 2 * 5 * 5 (not valid as needs 3 different primes)
    assert is_multiply_prime(49) == False  # 7 * 7 (not product of 3 primes)