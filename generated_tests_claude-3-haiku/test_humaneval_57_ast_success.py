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
    assert monotonic([]) == True

def test_monotonic_single_element_list():
    assert monotonic([1]) == True

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], True),
    ([3, 2, 1], True),
    ([1, 2, 2], True),
    ([1, 3, 2], False),
    ([1, 1, 2, 2, 3, 3], True),
    ([3, 2, 1, 1], True),
    ([1, 1, 2, 3, 3], True),
    ([3, 3, 2, 1, 1], True),
    ([1, 2, 3, 2], False),
    ([3, 2, 1, 3], False)
])
def test_monotonic_various_inputs(input, expected):
    assert monotonic(input) == expected

def test_monotonic_non_list_input():
    with pytest.raises(TypeError):
        monotonic(1)

def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False
