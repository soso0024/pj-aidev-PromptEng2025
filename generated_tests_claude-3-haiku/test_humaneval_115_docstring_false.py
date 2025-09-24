# Test cases for HumanEval/115
# Generated using Claude API


def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """

    return sum([math.ceil(sum(arr)/capacity) for arr in grid])


# Generated test cases:
import math
import pytest

@pytest.mark.parametrize("grid, capacity, expected", [
    ([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1, 6),
    ([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2, 5),
    ([[0,0,0], [0,0,0]], 5, 0),
    ([[1,1,1,1], [1,1,1,1], [1,1,1,1]], 1, 12),
    ([[0,0,0,0], [0,0,0,0], [0,0,0,0]], 10, 0),
    ([[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]], 2, 8),
    ([[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]], 3, 0),
    ([[1,0,1,0,1], [0,1,0,1,0], [1,0,1,0,1]], 2, 6),
    ([[1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1]], 3, 8),
    ([[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]], 7, 0)
])
def test_max_fill(grid, capacity, expected):
    assert max_fill(grid, capacity) == expected

def test_empty_grid():
    assert max_fill([[]], 1) == 0

def test_single_row_grid():
    assert max_fill([[1,1,1,1]], 2) == 2

def test_single_column_grid():
    assert max_fill([[1],[1],[1],[1]], 1) == 4

def test_negative_capacity():
    with pytest.raises(ValueError):
        max_fill([[1,1],[1,1]], -1)

def test_zero_capacity():
    with pytest.raises(ValueError):
        max_fill([[1,1],[1,1]], 0)

def max_fill(grid, capacity):
    if capacity <= 0:
        raise ValueError("Capacity must be greater than 0")
    return sum([math.ceil(sum(row) / capacity) for row in grid])