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

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], True),
    ([1, 2, 2, 3, 4], True),
    ([1, 3, 2, 4, 5], False),
    ([5, 4, 6, 2, 1], False),
    ([], True),
    ([1], True),
])
def test_monotonic(input_list, expected):
    assert monotonic(input_list) == expected

def test_monotonic_with_non_list_input():
    with pytest.raises(TypeError):
        monotonic(123)

def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False
