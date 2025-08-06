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

def test_empty_array():
    assert pluck([]) == []

def test_no_even_numbers():
    assert pluck([1, 3, 5, 7]) == []

def test_single_even_number():
    assert pluck([1, 2, 3]) == [2, 1]

def test_multiple_even_numbers():
    assert pluck([4, 2, 6, 8]) == [2, 1]

def test_zeros():
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

def test_large_numbers():
    assert pluck([999, 1000, 998, 996]) == [996, 3]

@pytest.mark.parametrize("input_arr,expected", [
    ([4, 2, 3], [2, 1]),
    ([1, 2, 3], [2, 1]),
    ([2, 2, 2], [2, 0]),
    ([1, 3, 5, 7, 9], []),
    ([0, 0, 0], [0, 0]),
    ([10, 8, 6, 4, 2], [2, 4]),
    ([100, 98, 96, 94], [94, 3]),
])
def test_pluck_parametrized(input_arr, expected):
    assert pluck(input_arr) == expected

def test_single_element_even():
    assert pluck([2]) == [2, 0]

def test_single_element_odd():
    assert pluck([1]) == []

def test_all_same_even_number():
    assert pluck([4, 4, 4, 4]) == [4, 0]

def test_large_array():
    large_arr = list(range(1, 10001, 2)) + [2]  # Odd numbers and one even
    assert pluck(large_arr) == [2, 5000]

def test_alternating_even_odd():
    assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]

def test_even_numbers_at_edges():
    assert pluck([2, 3, 5, 7, 4]) == [2, 0]
