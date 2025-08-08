# Test cases for HumanEval/87
# Generated using Claude API


def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """

    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])


# Generated test cases:
import pytest

def test_get_row_normal_case():
    lst = [[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]]
    assert get_row(lst, 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

def test_get_row_empty_list():
    assert get_row([], 1) == []

def test_get_row_single_element_lists():
    assert get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]

@pytest.mark.parametrize("lst,x,expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, [(1, 1)]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10, []),
    ([[], [1], [1, 2, 3]], 1, [(1, 0), (2, 0)]),
    ([[], [1], [1, 2, 3]], 2, [(2, 1)]),
    ([[], [1], [1, 2, 3]], 3, [(2, 2)]),
    ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], 4, [(0, 3)]),
    ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], 15, [(2, 4)]),
])
def test_get_row_parametrized(lst, x, expected):
    assert get_row(lst, x) == expected

def test_get_row_raises_error():
    with pytest.raises(TypeError):
        get_row(123, 1)

def get_row(lst, x):
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
