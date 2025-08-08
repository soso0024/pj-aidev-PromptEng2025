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
import time
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
    (5, 89),
    (6, 233),
    (7, 1597)
])
def test_prime_fib_parametrized(n, expected):
    assert prime_fib(n) == expected

def test_prime_fib_type_error():
    with pytest.raises(TypeError):
        prime_fib("1")
    with pytest.raises(TypeError):
        prime_fib([1])
    with pytest.raises(TypeError):
        prime_fib(1.5)

def test_prime_fib_value_error():
    with pytest.raises(ValueError):
        prime_fib(0)
    with pytest.raises(ValueError):
        prime_fib(-1)
    with pytest.raises(ValueError):
        prime_fib(-100)

def test_prime_fib_large_numbers():
    assert prime_fib(8) == 28657

def test_prime_fib_consecutive_calls():
    result1 = prime_fib(3)
    result2 = prime_fib(3)
    assert result1 == result2
    assert result1 == 5

def test_prime_fib_performance():
    start_time = time.time()
    prime_fib(7)
    end_time = time.time()
    assert end_time - start_time < 1

def is_prime(p):
    if p < 2:
        return False
    for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
        if p % k == 0:
            return False
    return True

def prime_fib(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")
        
    f = [0, 1]
    count = 0
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            count += 1
            if count == n:
                return f[-1]