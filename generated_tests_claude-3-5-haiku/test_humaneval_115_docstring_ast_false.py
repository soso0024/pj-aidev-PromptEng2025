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
import pytest
import math

def max_fill(grid, capacity):
    return sum([math.ceil(sum(row)/capacity) for row in grid])

def test_max_fill_normal_cases():
    assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
    assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5

def test_max_fill_empty_grid():
    assert max_fill([[0,0,0], [0,0,0]], 5) == 0

def test_max_fill_single_row():
    assert max_fill([[1,1,1]], 2) == 2

def test_max_fill_single_column():
    assert max_fill([[1],[1],[1]], 1) == 3

@pytest.mark.parametrize("grid,capacity,expected", [
    ([[0,1,0], [1,1,1]], 2, 3),
    ([[1,1,1,1]], 3, 2),
    ([[0,0,0,1], [1,1,1,1]], 2, 3)
])
def test_max_fill_parametrized(grid, capacity, expected):
    assert max_fill(grid, capacity) == expected

def test_max_fill_max_capacity():
    assert max_fill([[1,1,1], [1,1,1]], 10) == 1

def test_max_fill_uneven_rows():
    assert max_fill([[1,1], [1,1,1], [1]], 2) == 3