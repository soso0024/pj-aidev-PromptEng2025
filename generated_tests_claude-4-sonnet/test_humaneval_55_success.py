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

def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def test_fib_base_case_zero():
    assert fib(0) == 0

def test_fib_base_case_one():
    assert fib(1) == 1

def test_fib_small_positive_numbers():
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5

@pytest.mark.parametrize("n,expected", [
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
])
def test_fib_parametrized_positive(n, expected):
    assert fib(n) == expected

def test_fib_negative_numbers():
    with pytest.raises(RecursionError):
        fib(-1)

def test_fib_large_negative():
    with pytest.raises(RecursionError):
        fib(-10)

def test_fib_type_error_string():
    with pytest.raises(TypeError):
        fib("5")

def test_fib_type_error_float():
    with pytest.raises(RecursionError):
        fib(5.5)

def test_fib_type_error_none():
    with pytest.raises(TypeError):
        fib(None)

def test_fib_sequence_property():
    for i in range(2, 8):
        assert fib(i) == fib(i-1) + fib(i-2)