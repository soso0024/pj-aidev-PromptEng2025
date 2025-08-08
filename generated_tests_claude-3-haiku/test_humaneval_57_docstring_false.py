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
    ([1, 2, 4, 20], True),
    ([1, 20, 4, 10], False),
    ([4, 1, 0, -10], True),
    ([], True),
    ([1], True),
    ([20, 10, 5, 1], True),
    ([1, 1, 1, 1], True),
    ([20, 20, 20, 20], True),
    ([20, 10, 5, 20], False),
    ([20, 10, 5, 5], False),
    ([20, 10, 10, 5], False)
])
def test_monotonic(input_list, expected):
    assert monotonic(input_list) == expected