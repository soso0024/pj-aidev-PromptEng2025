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
    (7, 13)
])
def test_fib_sequence(n, expected):
    assert fib(n) == expected

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    1.5,
    "string",
    None,
    [],
    {}
])
def test_fib_invalid_input(invalid_input):
    if isinstance(invalid_input, (int, float)) and invalid_input < 0:
        with pytest.raises(ValueError):
            fib(invalid_input)
    else:
        with pytest.raises(TypeError):
            fib(invalid_input)

def test_fib_large_number():
    assert fib(10) == 55

def test_fib_type():
    result = fib(5)
    assert isinstance(result, int)

def test_fib_recursive_depth():
    with pytest.raises(RecursionError):
        fib(1000)