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
    ([1, 1, 1], True),
    ([20, 10, 5, 1], True),
    ([1, 2, 3, 2], False),
    ([1.0, 2.0, 3.0, 4.0], True),
    ([4.0, 3.0, 2.0, 1.0], True),
    ([1, 2, 3, 4.0], True),
    ([4.0, 3, 2, 1], True),
    ([1, 1, 2, 3], True),
    ([3, 2, 1, 1], True),
    ([1, 1, 1, 2], False),
    ([2, 1, 1, 1], False)
])
def test_monotonic(input_list, expected):
    assert monotonic(input_list) == expected