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
    ([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1, 6),
    ([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2, 5),
    ([[0,0,0], [0,0,0]], 5, 0),
    ([[1,1,1], [1,1,1]], 2, 4),
    ([[1]], 1, 1),
    ([[0]], 1, 0),
    ([[1,1,1,1,1]], 5, 1),
    ([[1], [1], [1], [1]], 1, 4),
    ([[0,1,0,1], [1,0,1,0]], 3, 2),
    ([[1,1,1,1], [1,1,1,1], [1,1,1,1]], 4, 3)
])
def test_max_fill_parametrized(grid, capacity, expected):
    assert max_fill(grid, capacity) == expected

def test_max_fill_empty_grid():
    assert max_fill([], 1) == 0

@pytest.mark.parametrize("capacity", [1, 2, 5, 10])
def test_max_fill_single_well(capacity):
    assert max_fill([[1] * 10], capacity) == math.ceil(10/capacity)

def test_max_fill_large_grid():
    large_grid = [[1 if (i + j) % 2 == 0 else 0 for j in range(100)] for i in range(100)]
    result = max_fill(large_grid, 5)
    assert isinstance(result, int)
    assert result > 0

def validate_grid(grid):
    if not grid:
        return
    if not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("All wells must have the same length")
    if not all(all(cell in (0, 1) for cell in row) for row in grid):
        raise ValueError("Grid values must be 0 or 1")

def validate_capacity(capacity):
    if capacity <= 0:
        raise ValueError("Capacity must be positive")

def test_max_fill_invalid_capacity():
    for invalid_capacity in [0, -1, -5]:
        with pytest.raises(ValueError, match="Capacity must be positive"):
            validate_capacity(invalid_capacity)
            max_fill([[1,1,1]], invalid_capacity)

def test_max_fill_invalid_grid_values():
    with pytest.raises(ValueError, match="Grid values must be 0 or 1"):
        validate_grid([[2,1,0], [1,2,1]])
        max_fill([[2,1,0], [1,2,1]], 1)

def test_max_fill_uneven_grid():
    with pytest.raises(ValueError, match="All wells must have the same length"):
        validate_grid([[1,1], [1,1,1]])
        max_fill([[1,1], [1,1,1]], 1)