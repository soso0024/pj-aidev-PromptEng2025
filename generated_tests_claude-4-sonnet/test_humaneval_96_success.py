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

def count_up_to(n):
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

def test_count_up_to_zero():
    assert count_up_to(0) == []

def test_count_up_to_one():
    assert count_up_to(1) == []

def test_count_up_to_two():
    assert count_up_to(2) == []

def test_count_up_to_three():
    assert count_up_to(3) == [2]

def test_count_up_to_four():
    assert count_up_to(4) == [2, 3]

def test_count_up_to_ten():
    assert count_up_to(10) == [2, 3, 5, 7]

def test_count_up_to_twenty():
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_count_up_to_thirty():
    assert count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

@pytest.mark.parametrize("n,expected", [
    (0, []),
    (1, []),
    (2, []),
    (3, [2]),
    (5, [2, 3]),
    (11, [2, 3, 5, 7]),
    (12, [2, 3, 5, 7, 11])
])
def test_count_up_to_parametrized(n, expected):
    assert count_up_to(n) == expected

def test_count_up_to_negative():
    assert count_up_to(-1) == []
    assert count_up_to(-10) == []

def test_count_up_to_large_number():
    result = count_up_to(100)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert result == expected

def test_count_up_to_returns_list():
    result = count_up_to(5)
    assert isinstance(result, list)

def test_count_up_to_all_elements_are_prime():
    result = count_up_to(50)
    for prime in result:
        is_prime = True
        for i in range(2, int(prime**0.5) + 1):
            if prime % i == 0:
                is_prime = False
                break
        assert is_prime

def test_count_up_to_no_duplicates():
    result = count_up_to(100)
    assert len(result) == len(set(result))

def test_count_up_to_sorted_order():
    result = count_up_to(50)
    assert result == sorted(result)
