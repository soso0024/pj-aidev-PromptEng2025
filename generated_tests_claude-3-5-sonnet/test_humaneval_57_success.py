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
    ([], True),
    ([1], True),
    ([1, 1], True),
    ([1, 2, 3], True),
    ([3, 2, 1], True),
    ([1, 2, 2, 3], True),
    ([3, 2, 2, 1], True),
    ([1, 1, 1, 1], True),
    ([1, 2, 1], False),
    ([2, 1, 3], False),
    ([1, 3, 2, 4], False),
    ([-1, -2, -3], True),
    ([-3, -2, -1], True),
    ([0.5, 1.0, 1.5], True),
    ([1.5, 1.0, 0.5], True),
    (['a', 'b', 'c'], True),
    (['c', 'b', 'a'], True),
    (['a', 'c', 'b'], False)
])
def test_monotonic_valid_inputs(input_list, expected):
    assert monotonic(input_list) == expected

def test_monotonic_none_input():
    with pytest.raises(TypeError):
        monotonic(None)

def test_monotonic_non_list_input():
    with pytest.raises(TypeError):
        monotonic(123)

def test_monotonic_nested_list():
    with pytest.raises(TypeError):
        monotonic([1, [2, 3], 4])

@pytest.mark.parametrize("input_list", [
    ([1, 'a']),
    ([1.0, 'b', 2]),
    (['x', 1, 'y'])
])
def test_monotonic_mixed_types(input_list):
    with pytest.raises(TypeError):
        monotonic(input_list)
