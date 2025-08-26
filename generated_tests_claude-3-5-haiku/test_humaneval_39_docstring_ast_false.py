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
    assert prime_fib(5) == 89

@pytest.mark.parametrize("n,expected", [
    (6, 233),
    (7, 1597),
    (8, 28657),
    (9, 514229)
])
def test_prime_fib_larger_values(n, expected):
    assert prime_fib(n) == expected

def test_prime_fib_type_error():
    with pytest.raises(TypeError):
        prime_fib("not an integer")

def test_prime_fib_negative_input():
    with pytest.raises(ValueError):
        prime_fib(-1)

def test_prime_fib_zero_input():
    with pytest.raises(ValueError):
        prime_fib(0)

def test_prime_fib_large_input():
    result = prime_fib(20)
    assert result > 10000
    assert is_prime(result)

def is_prime(p):
    if p < 2:
        return False
    for k in range(2, int(math.sqrt(p)) + 1):
        if p % k == 0:
            return False
    return True

def prime_fib(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p)):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    prime_count = 0
    while True:
        next_fib = f[-1] + f[-2]
        f.append(next_fib)
        if is_prime(next_fib):
            prime_count += 1
            if prime_count == n:
                return next_fib