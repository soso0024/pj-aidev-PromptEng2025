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

def test_next_smallest_normal_case():
    assert next_smallest([1, 2, 3, 4]) == 2
    assert next_smallest([5, 3, 1, 2, 4]) == 2

def test_next_smallest_with_duplicates():
    assert next_smallest([1, 1, 2, 3, 4]) == 2
    assert next_smallest([5, 5, 3, 3, 1, 1, 2, 4]) == 2

def test_next_smallest_single_element():
    assert next_smallest([1]) is None

def test_next_smallest_empty_list():
    assert next_smallest([]) is None

def test_next_smallest_negative_numbers():
    assert next_smallest([-5, -3, -1, 0, 2]) == -3

def test_next_smallest_mixed_numbers():
    assert next_smallest([-1, 0, 1, 2, 3]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([10, 20, 30, 40], 20),
    ([100, 50, 75, 25], 50),
    ([7, 7, 7, 7], None),
    ([0, 0, 1, 1], 1)
])
def test_next_smallest_parametrized(input_list, expected):
    assert next_smallest(input_list) == expected
