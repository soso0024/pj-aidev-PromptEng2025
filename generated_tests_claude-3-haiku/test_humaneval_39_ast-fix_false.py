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
import math

def is_prime(p):
    if p < 2:
        return False
    for k in range(2, min(int(math.sqrt(p)) + 1, p)):
        if p % k == 0:
            return False
    return True

def prime_fib(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    f = [0, 1]
    while len(f) <= n:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]

import pytest

def test_prime_fib_positive_values():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89

def test_prime_fib_zero():
    with pytest.raises(ValueError):
        prime_fib(0)

def test_prime_fib_negative_values():
    with pytest.raises(ValueError):
        prime_fib(-1)
        prime_fib(-5)

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89),
    (0, pytest.raises(ValueError)),
    (-1, pytest.raises(ValueError)),
    (-5, pytest.raises(ValueError))
])
def test_prime_fib_all_cases(input, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected:
            prime_fib(input)
    else:
        assert prime_fib(input) == expected