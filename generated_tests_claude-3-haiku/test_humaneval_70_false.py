# Test cases for HumanEval/70
# Generated using Claude API


def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res


# Generated test cases:
import pytest

def test_strange_sort_list_empty():
    assert strange_sort_list([]) == []

def test_strange_sort_list_single_element():
    assert strange_sort_list([5]) == [5]

def test_strange_sort_list_two_elements():
    assert strange_sort_list([5, 3]) == [3, 5]
    assert strange_sort_list([5, 10]) == [5, 10]

def test_strange_sort_list_multiple_elements():
    assert strange_sort_list([5, 3, 7, 1, 9]) == [1, 9, 3, 7, 5]
    assert strange_sort_list([10, 5, 15, 2, 8]) == [2, 15, 5, 10, 8]

@pytest.mark.parametrize("input,expected", [
    ([5, 3, 7, 1, 9], [1, 9, 3, 7, 5]),
    ([10, 5, 15, 2, 8], [2, 15, 5, 10, 8]),
    ([-2, 0, 4, -1, 3], [-2, 4, -1, 3, 0]),
    ([100, 50, 75, 25, 125], [25, 100, 50, 75, 125]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1])
])
def test_strange_sort_list_parametrized(input, expected):
    assert strange_sort_list(input) == expected

def test_strange_sort_list_duplicate_elements():
    assert strange_sort_list([5, 3, 5, 1, 9]) == [1, 9, 3, 5, 5]
    assert strange_sort_list([10, 5, 10, 2, 8]) == [2, 10, 5, 10, 8]

def test_strange_sort_list_negative_elements():
    assert strange_sort_list([-5, 3, -7, 1, -9]) == [-9, 3, -7, 1, -5]
    assert strange_sort_list([-10, 5, -15, 2, -8]) == [-15, 5, -10, 2, -8]