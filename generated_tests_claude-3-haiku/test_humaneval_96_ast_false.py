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

def test_count_up_to_empty():
    assert count_up_to(2) == []

def test_count_up_to_single_digit():
    assert count_up_to(10) == [2, 3, 5, 7]

def test_count_up_to_negative():
    with pytest.raises(ValueError):
        count_up_to(-5)

@pytest.mark.parametrize("input,expected", [
    (0, []),
    (1, []),
    (5, [2, 3]),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
])
def test_count_up_to_parametrized(input, expected):
    assert count_up_to(input) == expected

def count_up_to(n):
    if n <= 1:
        return []
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