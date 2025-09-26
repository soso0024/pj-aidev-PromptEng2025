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
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]

def test_prime_fib_first_few():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89

def test_prime_fib_larger_values():
    assert prime_fib(6) == 233
    assert prime_fib(7) == 1597
    assert prime_fib(8) == 28657

@pytest.mark.parametrize("n,expected", [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89),
    (6, 233),
    (7, 1597)
])
def test_prime_fib_parametrized(n, expected):
    assert prime_fib(n) == expected

def test_prime_fib_sequence_correctness():
    results = []
    for i in range(1, 6):
        results.append(prime_fib(i))
    
    expected = [2, 3, 5, 13, 89]
    assert results == expected

def test_prime_fib_single_case():
    result = prime_fib(1)
    assert result == 2
    assert result > 1

def test_prime_fib_returns_prime():
    for i in range(1, 8):
        result = prime_fib(i)
        assert is_prime_helper(result), f"prime_fib({i}) = {result} should be prime"

def is_prime_helper(p):
    if p < 2:
        return False
    for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
        if p % k == 0:
            return False
    return True

def test_prime_fib_returns_fibonacci():
    fib_sequence = [0, 1]
    for _ in range(50):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    for i in range(1, 6):
        result = prime_fib(i)
        assert result in fib_sequence, f"prime_fib({i}) = {result} should be in Fibonacci sequence"
