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

def test_empty_list():
    assert get_row([], 1) == []

def test_empty_sublists():
    assert get_row([[], [], []], 1) == []

def test_single_element_found():
    assert get_row([[1]], 1) == [(0, 0)]

def test_single_element_not_found():
    assert get_row([[1]], 2) == []

def test_multiple_occurrences_same_row():
    assert get_row([[1, 2, 1, 3, 1]], 1) == [(0, 4), (0, 2), (0, 0)]

def test_multiple_occurrences_different_rows():
    assert get_row([[1, 2], [3, 1], [1, 4]], 1) == [(0, 0), (1, 1), (2, 0)]

def test_no_occurrences():
    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10) == []

def test_mixed_data_types():
    assert get_row([['a', 1, 'b'], [1, 'a', 2]], 'a') == [(0, 0), (1, 1)]

def test_sorting_by_row_then_column_desc():
    lst = [
        [1, 2, 1, 4],
        [5, 1, 7, 1],
        [1, 9, 1, 1]
    ]
    expected = [(0, 2), (0, 0), (1, 3), (1, 1), (2, 3), (2, 2), (2, 0)]
    assert get_row(lst, 1) == expected

def test_jagged_array():
    lst = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [1, 2, 3, 1]
    ]
    assert get_row(lst, 1) == [(0, 0), (1, 0), (2, 3), (2, 0)]

def test_negative_numbers():
    assert get_row([[-1, -2, -1], [-3, -1, -4]], -1) == [(0, 2), (0, 0), (1, 1)]

def test_zero_values():
    assert get_row([[0, 1, 0], [2, 0, 3]], 0) == [(0, 2), (0, 0), (1, 1)]

def test_string_values():
    lst = [['hello', 'world', 'hello'], ['test', 'hello', 'case']]
    assert get_row(lst, 'hello') == [(0, 2), (0, 0), (1, 1)]

def test_boolean_values():
    lst = [[True, False, True], [False, True, False]]
    assert get_row(lst, True) == [(0, 2), (0, 0), (1, 1)]

def test_none_values():
    lst = [[None, 1, None], [2, None, 3]]
    assert get_row(lst, None) == [(0, 2), (0, 0), (1, 1)]

def test_single_row_multiple_columns():
    assert get_row([[5, 3, 5, 3, 5]], 5) == [(0, 4), (0, 2), (0, 0)]

def test_single_column_multiple_rows():
    lst = [[1], [2], [1], [3], [1]]
    assert get_row(lst, 1) == [(0, 0), (2, 0), (4, 0)]

def test_large_coordinates():
    lst = []
    for i in range(5):
        row = []
        for j in range(10):
            if i == 2 and j in [1, 5, 8]:
                row.append('target')
            else:
                row.append('other')
        lst.append(row)
    assert get_row(lst, 'target') == [(2, 8), (2, 5), (2, 1)]
