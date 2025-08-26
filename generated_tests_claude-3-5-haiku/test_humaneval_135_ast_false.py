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
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) <= 1:
        return -1
    
    ind = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            ind = i
    
    return ind

def test_can_arrange_normal_case():
    assert can_arrange([1, 2, 3, 4]) == -1
    assert can_arrange([4, 3, 2, 1]) == 1
    assert can_arrange([1, 3, 2, 4]) == 2

def test_can_arrange_edge_cases():
    assert can_arrange([]) == -1
    assert can_arrange([1]) == -1
    assert can_arrange([2, 1]) == 1

@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3, 4], -1),
    ([4, 3, 2, 1], 1),
    ([1, 3, 2, 4], 2),
    ([], -1),
    ([1], -1),
    ([2, 1], 1),
    ([5, 4, 3, 2, 1], 1),
    ([1, 5, 3, 4, 2], 2)
])
def test_can_arrange_parametrized(arr, expected):
    assert can_arrange(arr) == expected

def test_can_arrange_type_error():
    with pytest.raises(TypeError):
        can_arrange(None)
    with pytest.raises(TypeError):
        can_arrange("not a list")