# Test cases for HumanEval/63
# Generated using Claude API



def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """

    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)


# Generated test cases:
import pytest

def test_fibfib_zero():
    assert fibfib(0) == 0

def test_fibfib_one():
    assert fibfib(1) == 0

def test_fibfib_two():
    assert fibfib(2) == 1

@pytest.mark.parametrize("n,expected", [
    (3, 1),
    (4, 2),
    (5, 4),
    (6, 7),
    (7, 13)
])
def test_fibfib_sequence(n, expected):
    assert fibfib(n) == expected

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    1.5,
    "string",
    None,
    [],
    {}
])
def test_fibfib_invalid_input(invalid_input):
    with pytest.raises((TypeError, ValueError)):
        fibfib(invalid_input)

def test_fibfib_large_input():
    with pytest.raises(RecursionError):
        fibfib(1000)

def test_fibfib_type_error():
    with pytest.raises(TypeError):
        fibfib("3")

def test_fibfib_float_error():
    with pytest.raises(TypeError):
        fibfib(3.14)

def test_fibfib_none_error():
    with pytest.raises(TypeError):
        fibfib(None)
