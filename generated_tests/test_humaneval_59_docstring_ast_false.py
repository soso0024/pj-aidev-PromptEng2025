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

def test_basic_composite_number():
    assert largest_prime_factor(13195) == 29

def test_power_of_two():
    assert largest_prime_factor(2048) == 2

def test_product_of_primes():
    assert largest_prime_factor(21) == 7

def test_square_of_prime():
    assert largest_prime_factor(25) == 5

@pytest.mark.parametrize("input_n,expected", [
    (100, 5),
    (147, 7),
    (330, 11),
    (13195, 29),
    (2048, 2),
    (45, 5),
    (128, 2),
    (27, 3)
])
def test_various_numbers(input_n, expected):
    assert largest_prime_factor(input_n) == expected

@pytest.mark.parametrize("input_n", [
    4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20
])
def test_result_is_factor(input_n):
    result = largest_prime_factor(input_n)
    assert input_n % result == 0

def test_result_is_prime():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    test_numbers = [15, 21, 28, 35, 100]
    for n in test_numbers:
        result = largest_prime_factor(n)
        assert is_prime(result)

@pytest.mark.parametrize("invalid_input", [
    0, -1, -100
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(ValueError):
        largest_prime_factor(invalid_input)

def test_large_number():
    assert largest_prime_factor(123456) == 643

def test_product_of_same_prime():
    assert largest_prime_factor(343) == 7  # 7^3

def test_consecutive_numbers():
    results = [largest_prime_factor(n) for n in range(4, 11)]
    assert results == [2, 5, 3, 7, 2, 3, 5]