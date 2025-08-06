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

def test_fib4_base_cases():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0

@pytest.mark.parametrize("n,expected", [
    (4, 2),
    (5, 4),
    (6, 8),
    (7, 14),
    (8, 28),
    (9, 54),
    (10, 104)
])
def test_fib4_sequence(n, expected):
    assert fib4(n) == expected

@pytest.mark.parametrize("invalid_input", [
    -1,
    -100,
    -1000
])
def test_fib4_negative_input(invalid_input):
    with pytest.raises((ValueError, IndexError)):
        fib4(invalid_input)

def test_fib4_large_input():
    assert fib4(15) > 1000
    assert isinstance(fib4(20), int)

@pytest.mark.parametrize("invalid_type", [
    "1",
    None,
    3.14,
    [],
    {}
])
def test_fib4_invalid_types(invalid_type):
    with pytest.raises((TypeError, ValueError)):
        fib4(invalid_type)

def test_fib4_zero_and_one():
    assert fib4(0) == 0
    assert fib4(1) == 0

def test_fib4_consecutive_values():
    results = [fib4(i) for i in range(8)]
    for i in range(4, len(results)):
        assert results[i] == results[i-1] + results[i-2] + results[i-3] + results[i-4]