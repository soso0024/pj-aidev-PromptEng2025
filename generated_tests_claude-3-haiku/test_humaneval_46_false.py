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

def test_fib4_negative_input():
    with pytest.raises(ValueError):
        fib4(-1)

def test_fib4_zero_input():
    assert fib4(0) == 0

def test_fib4_one_input():
    assert fib4(1) == 0

def test_fib4_two_input():
    assert fib4(2) == 0

def test_fib4_three_input():
    assert fib4(3) == 2

@pytest.mark.parametrize("n,expected", [(4, 2), (5, 4), (6, 8), (7, 14), (8, 26), (9, 46), (10, 82)])
def test_fib4_normal_cases(n, expected):
    assert fib4(n) == expected

def fib4(n: int):
    if n < 0:
        raise ValueError("Input must be non-negative")
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for i in range(4, n + 1):
        next_num = results[-1] + results[-2] + results[-3] + results[-4]
        results.append(next_num)
        results.pop(0)

    return results[-1]