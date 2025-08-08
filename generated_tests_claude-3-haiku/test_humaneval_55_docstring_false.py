# Test cases for HumanEval/55
# Generated using Claude API



def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# Generated test cases:
import pytest

def test_fib_zero():
    assert fib(0) == 0

def test_fib_one():
    assert fib(1) == 1

@pytest.mark.parametrize("n,expected", [(2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)])
def test_fib_normal_cases(n, expected):
    assert fib(n) == expected

def test_fib_negative_input():
    with pytest.raises(TypeError):
        fib(-1)

def test_fib_float_input():
    with pytest.raises(TypeError):
        fib(3.14)

def test_fib_string_input():
    with pytest.raises(TypeError):
        fib("10")
