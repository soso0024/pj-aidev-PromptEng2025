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

def strange_sort_list(lst):
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

def test_strange_sort_list_empty():
    assert strange_sort_list([]) == []

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([5, 5, 5, 5], [5, 5, 5, 5]),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([2, 1], [1, 2]),
    ([3, 1, 2], [1, 3, 2]),
    ([4, 2, 1, 3], [1, 4, 2, 3]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([-1, 0, 1], [-1, 1, 0]),
    ([10, 5, 2, 7], [2, 10, 5, 7]),
])
def test_strange_sort_list(input, expected):
    assert strange_sort_list(input) == expected
