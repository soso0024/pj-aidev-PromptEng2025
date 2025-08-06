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
def test_fib_various_inputs(n, expected):
    assert fib(n) == expected

def test_fib_negative():
    with pytest.raises(ValueError, match="Input must be non-negative"):
        fib(-1)

@pytest.mark.parametrize("invalid_input", [
    1.5,
    "string",
    None,
    [],
    {}
])
def test_fib_invalid_types(invalid_input):
    with pytest.raises(TypeError, match="Input must be an integer"):
        fib(invalid_input)

def test_fib_large_number():
    with pytest.raises(RecursionError):
        fib(1000)

def test_fib_sequence_validity():
    results = [fib(n) for n in range(5)]
    for i in range(2, len(results)):
        assert results[i] == results[i-1] + results[i-2]

def fib(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)