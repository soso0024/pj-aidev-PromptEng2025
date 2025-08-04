# Test cases for HumanEval/59
# Generated using Claude API



def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest


# Generated test cases:
import pytest

def test_largest_prime_factor_basic():
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(12) == 3
    assert largest_prime_factor(28) == 7

@pytest.mark.parametrize("number,expected", [
    (2, 2),
    (3, 3),
    (4, 2),
    (100, 5),
    (2048, 2)
])
def test_largest_prime_factor_parametrized(number, expected):
    assert largest_prime_factor(number) == expected

def test_largest_prime_factor_edge_cases():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    -100
])
def test_largest_prime_factor_negative_numbers(invalid_input):
    try:
        largest_prime_factor(invalid_input)
        pytest.fail("Expected ValueError for invalid input")
    except ValueError:
        pass

def test_largest_prime_factor_special_cases():
    assert largest_prime_factor(25) == 5
    assert largest_prime_factor(49) == 7
    assert largest_prime_factor(997) == 997
    assert largest_prime_factor(1000) == 5

def test_largest_prime_factor_consecutive_numbers():
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(16) == 2
    assert largest_prime_factor(17) == 17
    assert largest_prime_factor(18) == 3

@pytest.mark.parametrize("input_num,expected", [
    (2310, 11),
    (9699690, 19),
    (510510, 17)
])
def test_largest_prime_factor_large_composites(input_num, expected):
    assert largest_prime_factor(input_num) == expected