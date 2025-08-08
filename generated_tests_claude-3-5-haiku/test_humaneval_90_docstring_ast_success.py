# Test cases for HumanEval/90
# Generated using Claude API


def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]


# Generated test cases:
import pytest

def test_next_smallest_normal_cases():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([10, 5, 3, 7, 2]) == 3

def test_next_smallest_edge_cases():
    assert next_smallest([]) is None
    assert next_smallest([1, 1]) is None
    assert next_smallest([1]) is None

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 2),
    ([5, 1, 4, 3, 2], 2),
    ([10, 5, 3, 7, 2], 3),
    ([], None),
    ([1, 1], None),
    ([1], None),
    ([0, 0, 1, 2], 1),
    ([-5, -3, -1, 0], -3)
])
def test_next_smallest_parametrized(input_list, expected):
    assert next_smallest(input_list) == expected
