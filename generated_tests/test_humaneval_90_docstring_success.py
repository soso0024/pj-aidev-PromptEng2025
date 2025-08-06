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

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 2),
    ([5, 1, 4, 3, 2], 2),
    ([5, 5, 5, 1, 1], 5),
    ([1, 1, 1, 2, 2], 2),
    ([], None),
    ([1], None),
    ([1, 1], None),
    ([1, 1, 1], None),
    ([0, -1, -2, -3], -2),
    ([100, 200, 300], 200),
    ([3.14, 2.71, 1.41], 2.71),
    ([10, 10, 10, 20, 20, 30], 20),
    ([-5, -5, -4, -4, -3], -4),
    ([999, 999, 1000, 1000], 1000),
    ([0, 0, 0, 1], 1),
])
def test_next_smallest_parametrized(input_list, expected):
    assert next_smallest(input_list) == expected

def test_next_smallest_single_element():
    assert next_smallest([42]) is None

def test_next_smallest_empty_list():
    assert next_smallest([]) is None

def test_next_smallest_duplicate_elements():
    assert next_smallest([3, 3, 3, 3]) is None

def test_next_smallest_negative_numbers():
    assert next_smallest([-10, -20, -30, -40]) == -30

def test_next_smallest_mixed_numbers():
    assert next_smallest([-1, 0, 1, -2]) == -1

def test_next_smallest_large_numbers():
    assert next_smallest([1000000, 999999, 999998]) == 999999

def test_next_smallest_float_numbers():
    assert next_smallest([1.5, 1.1, 1.3, 1.2]) == 1.2
