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

def test_get_row_empty_list():
    assert get_row([], 1) == []

def test_get_row_single_element():
    assert get_row([[1]], 1) == [(0, 0)]
    assert get_row([[2]], 1) == []

def test_get_row_single_row():
    assert get_row([[1, 2, 1]], 1) == [(0, 2), (0, 0)]
    assert get_row([[1, 2, 3]], 4) == []

def test_get_row_single_column():
    assert get_row([[1], [2], [1]], 1) == [(0, 0), (2, 0)]

@pytest.mark.parametrize("matrix, x, expected", [
    ([[1, 2], [3, 1]], 1, [(0, 0), (1, 1)]),
    ([[1, 1], [1, 1]], 1, [(0, 1), (0, 0), (1, 1), (1, 0)]),
    ([[1, 2, 3], [4, 1, 6], [7, 8, 1]], 1, [(0, 0), (1, 1), (2, 2)]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10, []),
])
def test_get_row_parametrized(matrix, x, expected):
    assert get_row(matrix, x) == expected

def test_get_row_different_row_lengths():
    matrix = [[1, 2], [3, 1, 5], [1]]
    assert get_row(matrix, 1) == [(0, 0), (1, 1), (2, 0)]

def test_get_row_with_negative_numbers():
    matrix = [[-1, 2], [3, -1]]
    assert get_row(matrix, -1) == [(0, 0), (1, 1)]

def test_get_row_with_zero():
    matrix = [[0, 1], [1, 0]]
    assert get_row(matrix, 0) == [(0, 0), (1, 1)]

def test_get_row_with_float():
    matrix = [[1.0, 2.0], [3.0, 1.0]]
    assert get_row(matrix, 1.0) == [(0, 0), (1, 1)]

@pytest.mark.parametrize("invalid_input", [
    None,
    42,
    [1, 2, 3],
])
def test_get_row_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        get_row(invalid_input, 1)