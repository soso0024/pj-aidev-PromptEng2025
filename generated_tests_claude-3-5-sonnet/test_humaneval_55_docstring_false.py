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

def test_fib_two():
    assert fib(2) == 1

@pytest.mark.parametrize("n,expected", [
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
])
def test_fib_various_numbers(n, expected):
    assert fib(n) == expected

@pytest.mark.parametrize("invalid_input", [
    -1,
    -10,
    -100
])
def test_fib_negative_numbers(invalid_input):
    with pytest.raises(ValueError, match="Input must be non-negative"):
        fib(invalid_input)

def test_fib_float_input():
    with pytest.raises(TypeError, match="Input must be an integer"):
        fib(3.14)

def test_fib_string_input():
    with pytest.raises(TypeError):
        fib("10")

def test_fib_none_input():
    with pytest.raises(TypeError):
        fib(None)

def test_fib_large_number():
    assert fib(15) == 610

def test_fib_sequence_correctness():
    results = [fib(n) for n in range(10)]
    assert results == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]