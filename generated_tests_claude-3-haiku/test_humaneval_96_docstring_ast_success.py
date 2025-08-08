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

def test_count_up_to_zero():
    assert count_up_to(0) == []

def test_count_up_to_one():
    assert count_up_to(1) == []

@pytest.mark.parametrize("n,expected", [
    (5, [2, 3]),
    (11, [2, 3, 5, 7]),
    (20, [2, 3, 5, 7, 11, 13, 17, 19]),
    (18, [2, 3, 5, 7, 11, 13, 17])
])
def test_count_up_to_valid_inputs(n, expected):
    assert count_up_to(n) == expected

def test_count_up_to_negative_input():
    with pytest.raises(ValueError):
        count_up_to(-1)

def test_count_up_to_float_input():
    with pytest.raises(TypeError):
        count_up_to(3.14)

def test_count_up_to_string_input():
    with pytest.raises(TypeError):
        count_up_to("5")

def count_up_to(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    
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
