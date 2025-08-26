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

def test_strange_sort_list_normal_case():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]

def test_strange_sort_list_repeated_values():
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]

def test_strange_sort_list_empty_list():
    assert strange_sort_list([]) == []

def test_strange_sort_list_single_element():
    assert strange_sort_list([42]) == [42]

def test_strange_sort_list_negative_numbers():
    assert strange_sort_list([-1, -3, -2, -4]) == [-4, -1, -3, -2]

def test_strange_sort_list_mixed_numbers():
    assert strange_sort_list([10, -5, 7, 0, 3]) == [-5, 10, 0, 7, 3]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([5, 5, 5, 5], [5, 5, 5, 5]),
    ([], []),
    ([42], [42]),
    ([-1, -3, -2, -4], [-4, -1, -3, -2]),
    ([10, -5, 7, 0, 3], [-5, 10, 0, 7, 3])
])
def test_strange_sort_list_parametrized(input_list, expected):
    assert strange_sort_list(input_list) == expected
