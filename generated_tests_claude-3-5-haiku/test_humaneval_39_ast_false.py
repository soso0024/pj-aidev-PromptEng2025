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
import math

def test_prime_fib_first_few_values():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13

@pytest.mark.parametrize("n,expected", [
    (5, 89),
    (6, 233),
    (7, 1597),
    (10, 4181)
])
def test_prime_fib_multiple_values(n, expected):
    assert prime_fib(n) == expected

def test_prime_fib_zero_input():
    with pytest.raises(ValueError):
        prime_fib(0)

def test_prime_fib_negative_input():
    with pytest.raises(ValueError):
        prime_fib(-1)

def test_prime_fib_large_input():
    result = prime_fib(20)
    assert result > 10000
    assert is_prime_helper(result)

def is_prime_helper(p):
    if p < 2:
        return False
    for k in range(2, min(int(math.sqrt(p)) + 1, p)):
        if p % k == 0:
            return False
    return True