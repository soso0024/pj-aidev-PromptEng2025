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

def get_row(lst, x):
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

def test_get_row_example_case():
    lst = [
        [1,2,3,4,5,6],
        [1,2,3,4,1,6],
        [1,2,3,4,5,1]
    ]
    result = get_row(lst, 1)
    expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    assert result == expected

def test_get_row_empty_list():
    result = get_row([], 1)
    assert result == []

def test_get_row_with_empty_sublists():
    lst = [[], [1], [1, 2, 3]]
    result = get_row(lst, 3)
    expected = [(2, 2)]
    assert result == expected

def test_get_row_element_not_found():
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = get_row(lst, 10)
    assert result == []

def test_get_row_single_element():
    lst = [[5]]
    result = get_row(lst, 5)
    expected = [(0, 0)]
    assert result == expected

def test_get_row_single_row_multiple_matches():
    lst = [[1, 2, 1, 3, 1]]
    result = get_row(lst, 1)
    expected = [(0, 4), (0, 2), (0, 0)]
    assert result == expected

def test_get_row_multiple_rows_single_match_each():
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = get_row(lst, 5)
    expected = [(1, 1)]
    assert result == expected

def test_get_row_irregular_matrix():
    lst = [[1, 2], [3, 4, 5, 6], [7]]
    result = get_row(lst, 4)
    expected = [(1, 1)]
    assert result == expected

def test_get_row_all_same_elements():
    lst = [[2, 2, 2], [2, 2], [2]]
    result = get_row(lst, 2)
    expected = [(0, 2), (0, 1), (0, 0), (1, 1), (1, 0), (2, 0)]
    assert result == expected

def test_get_row_negative_numbers():
    lst = [[-1, 2, -1], [3, -1, 5]]
    result = get_row(lst, -1)
    expected = [(0, 2), (0, 0), (1, 1)]
    assert result == expected

def test_get_row_zero_element():
    lst = [[0, 1, 0], [2, 0, 3], [0]]
    result = get_row(lst, 0)
    expected = [(0, 2), (0, 0), (1, 1), (2, 0)]
    assert result == expected

def test_get_row_mixed_length_rows():
    lst = [[1, 2, 3, 4, 5], [1, 2], [1, 2, 3, 4, 5, 6, 7, 1]]
    result = get_row(lst, 1)
    expected = [(0, 0), (1, 0), (2, 7), (2, 0)]
    assert result == expected

def test_get_row_large_numbers():
    lst = [[1000, 2000, 1000], [3000, 1000]]
    result = get_row(lst, 1000)
    expected = [(0, 2), (0, 0), (1, 1)]
    assert result == expected
