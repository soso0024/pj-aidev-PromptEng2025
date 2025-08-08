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

def test_strange_sort_list_empty_list():
    assert strange_sort_list([]) == []

def test_strange_sort_list_single_element():
    assert strange_sort_list([5]) == [5]

def test_strange_sort_list_already_sorted():
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

def test_strange_sort_list_reverse_sorted():
    assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]

def test_strange_sort_list_duplicate_elements():
    assert strange_sort_list([1, 2, 2, 3, 3]) == [1, 3, 2, 3, 2]

@pytest.mark.parametrize("input,expected", [
    ([10, 5, 2, 8, 1, 7], [1, 10, 2, 8, 5, 7]),
    ([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 9, 1, 6, 2, 5, 3, 5, 4]),
    ([0, -1, 0, 1, -2, 2], [0, 2, -1, 1, -2, 0])
])
def test_strange_sort_list_various_inputs(input, expected):
    assert strange_sort_list(input) == expected

def test_strange_sort_list_non_numeric_elements():
    with pytest.raises(TypeError):
        strange_sort_list([1, 2, 'a', 4, 5])

def strange_sort_list(lst):
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res