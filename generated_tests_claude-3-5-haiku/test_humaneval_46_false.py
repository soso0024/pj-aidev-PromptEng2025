# Test cases for HumanEval/46
# Generated using Claude API



def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """

    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]


# Generated test cases:
import pytest

def fib4(n: int):
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]

def test_fib4_base_cases():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0

def test_fib4_normal_cases():
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28

def test_fib4_larger_numbers():
    assert fib4(10) == 104
    assert fib4(15) == 2764
    assert fib4(20) == 17716

def test_fib4_negative_input():
    with pytest.raises(ValueError):
        fib4(-1)

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 0),
    (2, 2),
    (3, 0),
    (4, 2),
    (5, 4),
    (10, 104),
    (15, 2764)
])
def test_fib4_parametrized(n, expected):
    assert fib4(n) == expected