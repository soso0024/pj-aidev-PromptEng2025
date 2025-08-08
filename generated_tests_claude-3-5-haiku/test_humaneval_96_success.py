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

def test_count_up_to_basic_primes():
    assert count_up_to(10) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_count_up_to_edge_cases():
    assert count_up_to(2) == []
    assert count_up_to(1) == []
    assert count_up_to(0) == []

def test_count_up_to_large_number():
    result = count_up_to(50)
    assert len(result) > 10
    assert result[0] == 2
    assert result[-1] == 47

@pytest.mark.parametrize("input_n,expected_length", [
    (10, 4),
    (20, 8),
    (30, 10),
    (100, 25)
])
def test_count_up_to_parametrized(input_n, expected_length):
    result = count_up_to(input_n)
    assert len(result) == expected_length

def test_count_up_to_negative_input():
    assert count_up_to(-5) == []

def test_count_up_to_prime_properties():
    result = count_up_to(30)
    for prime in result:
        for divisor in range(2, int(prime**0.5) + 1):
            assert prime % divisor != 0
