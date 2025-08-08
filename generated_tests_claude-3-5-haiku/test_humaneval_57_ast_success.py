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

def test_monotonic_increasing_list():
    assert monotonic([1, 2, 3, 4, 5]) == True

def test_monotonic_decreasing_list():
    assert monotonic([5, 4, 3, 2, 1]) == True

def test_monotonic_equal_elements():
    assert monotonic([2, 2, 2, 2]) == True

def test_monotonic_empty_list():
    assert monotonic([]) == True

def test_monotonic_single_element_list():
    assert monotonic([42]) == True

def test_monotonic_non_monotonic_list():
    assert monotonic([1, 3, 2, 4]) == False

def test_monotonic_mixed_types():
    assert monotonic([1, 2, 2.5, 3]) == True

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], True),
    ([2, 2, 2, 2], True),
    ([], True),
    ([42], True),
    ([1, 3, 2, 4], False),
    ([1, 2, 2.5, 3], True),
    ([-1, -2, -3], True),
    ([-3, -2, -1], True)
])
def test_monotonic_parametrized(input_list, expected):
    assert monotonic(input_list) == expected