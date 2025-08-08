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

def test_prime_fib_first_five():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89

@pytest.mark.parametrize("n,expected", [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89)
])
def test_prime_fib_parametrized(n, expected):
    assert prime_fib(n) == expected

@pytest.mark.parametrize("invalid_input", [
    0,
    -1,
    -100
])
def test_prime_fib_negative_input(invalid_input):
    with pytest.raises(ValueError):
        prime_fib(invalid_input)

def test_prime_fib_type_error():
    with pytest.raises(TypeError):
        prime_fib("1")
    with pytest.raises(TypeError):
        prime_fib(1.5)
    with pytest.raises(TypeError):
        prime_fib(None)

def test_prime_fib_large_input():
    result = prime_fib(8)
    assert result > 0
    assert isinstance(result, int)

def test_prime_fib_sequence_properties():
    result1 = prime_fib(1)
    result2 = prime_fib(2)
    result3 = prime_fib(3)
    assert result1 < result2 < result3

def test_prime_fib_primality():
    result = prime_fib(1)
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    assert is_prime(result)

def prime_fib(n: int):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be positive")
        

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