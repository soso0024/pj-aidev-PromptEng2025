# Test cases for HumanEval/135
# Generated using Claude API


def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind


# Generated test cases:
import pytest

def can_arrange(arr):
    ind = -1
    i = 1
    while i < len(arr):
        if arr[i] < arr[i-1]:
            ind = i
            break
        i += 1
    return ind

@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 3], -1),
    ([3, 2, 1], 0),
    ([2, 1, 3], 1),
    ([1, 1, 1], -1),
    ([], -1),
    ([1], -1),
    ([1, 1, 2, 2], -1),
    ([2, 2, 1, 1], 2),
    ([float('inf'), 1, 2], -1),
    ([1, float('inf'), 2], 1),
    ([1, 2, float('inf')], -1),
    ([float('nan'), 1, 2], -1),
    ([1, float('nan'), 2], -1),
    ([1, 2, float('nan')], -1),
    ([None, 1, 2], TypeError),
    ([1, None, 2], TypeError),
    ([1, 2, None], TypeError),
])
def test_can_arrange(arr, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            can_arrange(arr)
    else:
        assert can_arrange(arr) == expected