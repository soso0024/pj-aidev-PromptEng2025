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
from math import isclose
from typing import Union

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 0),
    (2, 2),
    (3, 0),
    (4, 2),
    (5, 4),
    (6, 8),
    (7, 14),
    (8, 24),
    (-1, IndexError),
    (3.14, TypeError),
    ("4", TypeError)
])
def test_fib4(n, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
            fib4(n)
    else:
        assert isclose(fib4(n), expected, rel_tol=1e-9)

def fib4(n: int) -> Union[int, float]:
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(sum(results[-4:]))
        results.pop(0)

    return results[-1]