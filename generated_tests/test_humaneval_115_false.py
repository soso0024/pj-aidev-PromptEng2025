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

@pytest.mark.parametrize("grid, capacity, expected", [
    ([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1, 6),
    ([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2, 5),
    ([[0, 0, 0], [0, 0, 0]], 5, 0),
    ([[1]], 1, 1),
    ([[1, 1, 1]], 2, 2),
    ([[1, 1, 1, 1], [1, 1, 1, 1]], 3, 4),
    ([], 5, 0),
    ([[]], 5, 0)
])
def test_max_fill_normal_cases(grid, capacity, expected):
    assert max_fill(grid, capacity) == expected

@pytest.mark.parametrize("grid, capacity", [
    ([[1, 2, 3]], 0),
    ([[1, 2, 3]], -1),
])
def test_max_fill_invalid_capacity(grid, capacity):
    with pytest.raises((ZeroDivisionError, ValueError)):
        max_fill(grid, capacity)

@pytest.mark.parametrize("grid, capacity", [
    ("not a grid", 5),
    (None, 5),
    (123, 5),
])
def test_max_fill_invalid_grid(grid, capacity):
    with pytest.raises(TypeError):
        max_fill(grid, capacity)

@pytest.mark.parametrize("grid, capacity", [
    ([[1, "2", 3]], 5),
    ([[None, 2, 3]], 5),
    ([[1, [], 3]], 5),
])
def test_max_fill_invalid_grid_elements(grid, capacity):
    with pytest.raises(TypeError):
        max_fill(grid, capacity)

def test_max_fill_large_numbers():
    grid = [[1] * 10] * 10
    capacity = 1
    assert max_fill(grid, capacity) == 100

def test_max_fill_single_element_arrays():
    grid = [[1], [1], [1]]
    capacity = 1
    assert max_fill(grid, capacity) == 3