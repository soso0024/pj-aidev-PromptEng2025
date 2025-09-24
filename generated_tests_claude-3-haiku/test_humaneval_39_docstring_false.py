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
    for k in range(2, int(math.sqrt(p)) + 1):
        if p % k == 0:
            return False
    return True

def prime_fib(n: int):
    if n <= 0:
        return 0
    f = [0, 1]
    count = 0
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            count += 1
            if count == n:
                return f[-1]

def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89

def test_prime_fib_edge_cases():
    with pytest.raises(TypeError):
        prime_fib("1")
    assert prime_fib(0) == 0
    assert prime_fib(-1) == 0

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89),
    (6, 233),
    (7, 1597),
    (8, 28657),
    (9, 514229),
    (10, 2971)
])
def test_prime_fib_values(input, expected):
    assert prime_fib(input) == expected