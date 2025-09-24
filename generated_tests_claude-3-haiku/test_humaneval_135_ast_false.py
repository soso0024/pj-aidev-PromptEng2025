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

def test_can_arrange():
    assert can_arrange([1, 2, 3, 4]) == -1
    assert can_arrange([4, 3, 2, 1]) == 0
    assert can_arrange([1, 3, 2, 4]) == 2
    assert can_arrange([]) == -1
    assert can_arrange([1]) == -1
    assert can_arrange([1, 1, 1, 1]) == -1
    assert can_arrange([4, 3, 2, 1, 5]) == 3
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([5, 4, 3, 2, 1]) == 0

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4], -1),
    ([4, 3, 2, 1], 0),
    ([1, 3, 2, 4], 2),
    ([], -1),
    ([1], -1),
    ([1, 1, 1, 1], -1),
    ([4, 3, 2, 1, 5], 3),
    ([1, 2, 4, 3, 5], 3),
    ([5, 4, 3, 2, 1], 0)
])
def test_can_arrange_parametrized(input, expected):
    assert can_arrange(input) == expected