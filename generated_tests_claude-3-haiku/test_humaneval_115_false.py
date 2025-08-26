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

def max_fill(grid, capacity):
    return sum([math.ceil(sum(row)/capacity) for row in grid])

def test_max_fill_normal_case():
    grid = [[1, 2, 3], [4, 5, 6]]
    capacity = 5
    assert max_fill(grid, capacity) == 3

def test_max_fill_single_row():
    grid = [[1, 2, 3]]
    capacity = 2
    assert max_fill(grid, capacity) == 2

def test_max_fill_single_element():
    grid = [[5]]
    capacity = 5
    assert max_fill(grid, capacity) == 1

def test_max_fill_zero_capacity():
    grid = [[1, 2, 3], [4, 5, 6]]
    capacity = 0
    with pytest.raises(ZeroDivisionError):
        max_fill(grid, capacity)

@pytest.mark.parametrize("grid,capacity,expected", [
    ([[1, 2, 3], [4, 5, 6]], 2, 6),
    ([[1, 1, 1], [1, 1, 1]], 1, 6),
    ([[10, 10, 10], [10, 10, 10]], 10, 2),
    ([[0, 0, 0], [0, 0, 0]], 1, 6),
])
def test_max_fill_parametrized(grid, capacity, expected):
    assert max_fill(grid, capacity) == expected