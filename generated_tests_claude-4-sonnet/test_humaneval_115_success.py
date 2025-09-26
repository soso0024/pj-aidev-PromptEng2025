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
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])

class TestMaxFill:
    
    def test_empty_grid(self):
        assert max_fill([], 5) == 0
    
    def test_single_row_empty(self):
        assert max_fill([[]], 5) == 0
    
    def test_single_row_single_element(self):
        assert max_fill([[3]], 5) == 1
    
    def test_single_row_exact_capacity(self):
        assert max_fill([[5]], 5) == 1
    
    def test_single_row_over_capacity(self):
        assert max_fill([[7]], 5) == 2
    
    def test_multiple_rows_under_capacity(self):
        assert max_fill([[1, 2], [3, 1], [2, 2]], 5) == 3
    
    def test_multiple_rows_exact_capacity(self):
        assert max_fill([[2, 3], [5], [1, 4]], 5) == 3
    
    def test_multiple_rows_over_capacity(self):
        assert max_fill([[3, 4, 2], [1, 6, 3], [2, 8]], 10) == 3
    
    def test_zero_capacity_with_empty_rows(self):
        with pytest.raises(ZeroDivisionError):
            max_fill([[]], 0)
    
    def test_zero_capacity_with_non_empty_rows(self):
        with pytest.raises(ZeroDivisionError):
            max_fill([[1, 2]], 0)
    
    def test_negative_capacity(self):
        assert max_fill([[1, 2]], -1) == -3
    
    def test_rows_with_zeros(self):
        assert max_fill([[0, 0], [0, 1], [2, 0]], 3) == 2
    
    def test_all_zero_rows(self):
        assert max_fill([[0, 0], [0, 0], [0, 0]], 5) == 0
    
    def test_large_numbers(self):
        assert max_fill([[100, 200], [150, 250]], 100) == 7
    
    def test_fractional_result_ceiling(self):
        assert max_fill([[1], [1], [1]], 2) == 3
    
    def test_mixed_row_sizes(self):
        assert max_fill([[1], [1, 2, 3], [4, 5]], 3) == 6
    
    @pytest.mark.parametrize("grid,capacity,expected", [
        ([[1, 2, 3]], 6, 1),
        ([[1, 2, 3]], 5, 2),
        ([[1, 2, 3]], 3, 2),
        ([[1, 2, 3]], 2, 3),
        ([[1, 2, 3]], 1, 6)
    ])
    def test_parametrized_single_row(self, grid, capacity, expected):
        assert max_fill(grid, capacity) == expected
    
    def test_float_values(self):
        assert max_fill([[1.5, 2.5], [3.2, 1.8]], 4) == 3
    
    def test_negative_values(self):
        assert max_fill([[-1, -2], [3, 4]], 5) == 2
    
    def test_capacity_one(self):
        assert max_fill([[1, 2], [3]], 1) == 6