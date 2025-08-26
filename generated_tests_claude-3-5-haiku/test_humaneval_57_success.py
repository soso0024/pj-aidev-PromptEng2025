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

def test_monotonic_increasing():
    assert monotonic([1, 2, 3, 4, 5]) == True

def test_monotonic_decreasing():
    assert monotonic([5, 4, 3, 2, 1]) == True

def test_monotonic_equal_elements():
    assert monotonic([2, 2, 2, 2]) == True

def test_monotonic_mixed_not_monotonic():
    assert monotonic([1, 3, 2, 4]) == False

def test_monotonic_empty_list():
    assert monotonic([]) == True

def test_monotonic_single_element():
    assert monotonic([42]) == True

@pytest.mark.parametrize("input_list,expected", [
    ([1, 1, 2, 3, 4], True),
    ([5, 5, 4, 3, 2], True),
    ([1, 2, 2, 3, 4], True),
    ([4, 3, 3, 2, 1], True),
    ([1, 3, 2, 4, 5], False),
    ([-1, -2, -3, -4], True),
    ([-4, -3, -2, -1], True)
])
def test_monotonic_parametrized(input_list, expected):
    assert monotonic(input_list) == expected
