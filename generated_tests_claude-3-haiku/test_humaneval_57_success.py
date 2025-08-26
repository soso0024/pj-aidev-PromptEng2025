# Test cases for HumanEval/57
# Generated using Claude API



def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


# Generated test cases:
import pytest

def test_monotonic_empty_list():
    assert monotonic([])

def test_monotonic_single_element_list():
    assert monotonic([1])

def test_monotonic_increasing_list():
    assert monotonic([1, 2, 3, 4, 5])

def test_monotonic_decreasing_list():
    assert monotonic([5, 4, 3, 2, 1])

def test_monotonic_constant_list():
    assert monotonic([1, 1, 1, 1, 1])

def test_monotonic_non_monotonic_list():
    assert not monotonic([1, 2, 3, 2, 4])

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], True),
    ([1, 1, 1, 1, 1], True),
    ([1, 2, 3, 2, 4], False),
    ([], True),
    ([1], True)
])
def test_monotonic_parametrized(input, expected):
    assert monotonic(input) == expected

def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False
