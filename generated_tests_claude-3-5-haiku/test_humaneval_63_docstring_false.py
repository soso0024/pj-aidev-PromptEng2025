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

def test_fibfib_five():
    assert fibfib(5) == 4

def test_fibfib_eight():
    assert fibfib(8) == 24

def test_fibfib_negative_input():
    with pytest.raises(ValueError):
        fibfib(-1)

def test_fibfib_non_integer_input():
    with pytest.raises(TypeError):
        fibfib(3.5)