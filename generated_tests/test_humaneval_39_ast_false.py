# Test cases for HumanEval/39
# Generated using Claude API



def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """

    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]


# Generated test cases:
import pytest
from typing import Union
from prime_fib import prime_fib

def test_prime_fib_first_prime():
    assert prime_fib(1) == 2

def test_prime_fib_second_prime():
    assert prime_fib(2) == 3

def test_prime_fib_third_prime():
    assert prime_fib(3) == 5

def test_prime_fib_fourth_prime():
    assert prime_fib(4) == 13

@pytest.mark.parametrize("n,expected", [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89)
])
def test_prime_fib_multiple_values(n, expected):
    assert prime_fib(n) == expected

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    -100
])
def test_prime_fib_negative_input(invalid_input):
    with pytest.raises(ValueError):
        prime_fib(invalid_input)

def test_prime_fib_large_input():
    result = prime_fib(8)
    assert result > 1000

@pytest.mark.parametrize("invalid_type", [
    "1",
    None,
    3.14,
    [],
    {}
])
def test_prime_fib_invalid_type(invalid_type):
    with pytest.raises(TypeError):
        prime_fib(invalid_type)

def test_prime_fib_sequence_correctness():
    results = [prime_fib(i) for i in range(1, 5)]
    assert results == [2, 3, 5, 13]
    assert all(isinstance(x, int) for x in results)

def test_prime_fib_is_fibonacci():
    result = prime_fib(3)
    assert result in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_prime_fib_is_prime():
    result = prime_fib(3)
    assert result > 1
    for i in range(2, int(result ** 0.5) + 1):
        assert result % i != 0

if __name__ == '__main__':
    pytest.main([__file__])