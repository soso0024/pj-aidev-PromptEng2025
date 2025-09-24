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

def fibfib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

def test_fibfib_base_cases():
    assert fibfib(0) == 0
    assert fibfib(1) == 0
    assert fibfib(2) == 1

def test_fibfib_small_values():
    assert fibfib(3) == 1
    assert fibfib(4) == 2
    assert fibfib(5) == 4
    assert fibfib(6) == 7

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 4),
    (6, 7),
    (7, 13),
    (8, 24),
    (9, 44),
    (10, 81)
])
def test_fibfib_parametrized(n, expected):
    assert fibfib(n) == expected

def test_fibfib_sequence_property():
    for n in range(3, 15):
        assert fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

def test_fibfib_negative_input():
    with pytest.raises(RecursionError):
        fibfib(-1)

def test_fibfib_large_negative():
    with pytest.raises(RecursionError):
        fibfib(-10)

def test_fibfib_type_error():
    with pytest.raises(TypeError):
        fibfib("string")
    
    with pytest.raises(TypeError):
        fibfib(None)
    
    with pytest.raises(TypeError):
        fibfib([1, 2, 3])

def test_fibfib_float_input():
    with pytest.raises(RecursionError):
        fibfib(3.5)

def test_fibfib_increasing_sequence():
    values = [fibfib(i) for i in range(3, 12)]
    for i in range(len(values) - 1):
        assert values[i] < values[i + 1]