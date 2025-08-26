# Test cases for HumanEval/68
# Generated using Claude API


def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """

    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]


# Generated test cases:
import pytest

def test_pluck_empty_list():
    assert pluck([]) == []

def test_pluck_list_with_no_evens():
    assert pluck([1, 3, 5, 7]) == []

@pytest.mark.parametrize("input,expected", [
    ([2, 4, 6, 8], [2, 0]),
    ([1, 2, 3, 4, 5, 6], [2, 1]),
    ([10, 8, 6, 4, 2], [2, 4]),
    ([11, 22, 33, 44, 55], [22, 1])
])
def test_pluck_list_with_evens(input, expected):
    assert pluck(input) == expected

def test_pluck_list_with_duplicate_evens():
    assert pluck([2, 4, 4, 6, 8]) == [2, 0]

def test_pluck_list_with_negative_numbers():
    assert pluck([-2, -4, 6, 8]) == [-4, 1]

def pluck(arr):
    if not arr:
        return []
    evens = [x for x in arr if x % 2 == 0]
    if not evens:
        return []
    return [min(evens), arr.index(min(evens))]