# Test cases for HumanEval/96
# Generated using Claude API


def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes



# Generated test cases:
import pytest

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    if not isinstance(n, int) or n < 0:
        return []
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

def test_count_up_to_normal_cases():
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]

def test_count_up_to_edge_cases():
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(2) == [2]
    assert count_up_to(3) == [2, 3]

@pytest.mark.parametrize("input,expected", [
    (-1, []),
    (1.5, []),
    ('test', []),
    (None, [])
])
def test_count_up_to_error_conditions(input, expected):
    assert count_up_to(input) == expected