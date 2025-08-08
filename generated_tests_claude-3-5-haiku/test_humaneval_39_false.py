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

def test_prime_fib_larger_values():
    assert prime_fib(5) == 89
    assert prime_fib(10) == 1597

@pytest.mark.parametrize("n,expected", [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89),
    (10, 1597)
])
def test_prime_fib_parametrized(n, expected):
    assert prime_fib(n) == expected

def test_prime_fib_invalid_input():
    with pytest.raises(TypeError):
        prime_fib("not an integer")
    with pytest.raises(TypeError):
        prime_fib(1.5)
    with pytest.raises(ValueError):
        prime_fib(0)
    with pytest.raises(ValueError):
        prime_fib(-1)

def test_prime_fib_type_hints():
    assert isinstance(prime_fib(1), int)

def test_prime_fib_performance():
    result = prime_fib(10)
    assert result == 1597