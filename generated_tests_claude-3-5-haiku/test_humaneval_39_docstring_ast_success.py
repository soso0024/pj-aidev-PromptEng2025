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

def prime_fib(n: int):
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True
    
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]

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

def test_prime_fib_is_prime():
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p)):
            if p % k == 0:
                return False
        return True
    
    for i in range(1, 10):
        assert is_prime(prime_fib(i)), f"prime_fib({i}) should be prime"

def test_prime_fib_invalid_input():
    with pytest.raises(TypeError):
        prime_fib(None)
    with pytest.raises(TypeError):
        prime_fib("not a number")
    with pytest.raises(ValueError):
        prime_fib(0)
    with pytest.raises(ValueError):
        prime_fib(-1)