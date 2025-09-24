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
import pytest

def is_prime(p):
    if p < 2:
        return False
    for k in range(2, min(int(math.sqrt(p)) + 1, p)):
        if p % k == 0:
            return False
    return True

def prime_fib(n: int):
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    f = [0, 1]
    while len(f) <= n:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]
    raise ValueError("n is greater than the number of prime Fibonacci numbers")

def test_prime_fib_negative_input():
    with pytest.raises(ValueError):
        prime_fib(-1)

def test_prime_fib_zero_input():
    with pytest.raises(ValueError):
        prime_fib(0)

def test_prime_fib_one_input():
    assert prime_fib(1) == 2

def test_prime_fib_two_input():
    assert prime_fib(2) == 3

def test_prime_fib_three_input():
    assert prime_fib(3) == 5

@pytest.mark.parametrize("input,expected", [
    (4, 13),
    (5, 89),
    (6, 233),
    (7, 1597),
    (8, 28657),
    (9, 514229),
    (10, 433494437)
])
def test_prime_fib_multiple_inputs(input, expected):
    assert prime_fib(input) == expected