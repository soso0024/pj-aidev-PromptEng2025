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
from test_humaneval_70_docstring import strange_sort_list

@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([5, 5, 5, 5], [5, 5, 5, 5]),
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([2, 1], [1, 2]),
    ([3, 1, 4, 2], [1, 4, 2, 3]),
    ([-1, 0, 1, -2], [-2, 1, -1, 0]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([5, 4, 3, 2, 1], [1, 5, 2, 4, 3])
])
def test_strange_sort_list(input_list, expected_output):
    assert strange_sort_list(input_list) == expected_output

def test_strange_sort_list_empty_input():
    assert strange_sort_list([]) == []

def test_strange_sort_list_single_element():
    assert strange_sort_list([1]) == [1]

def test_strange_sort_list_duplicate_elements():
    assert strange_sort_list([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_strange_sort_list_negative_elements():
    assert strange_sort_list([-1, 0, 1, -2]) == [-2, 1, -1, 0]