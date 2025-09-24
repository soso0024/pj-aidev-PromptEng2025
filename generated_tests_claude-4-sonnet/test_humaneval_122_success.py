# Test cases for HumanEval/122
# Generated using Claude API


def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)


# Generated test cases:
import pytest

def add_elements(arr, k):
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

class TestAddElements:
    
    def test_empty_array(self):
        assert add_elements([], 0) == 0
        assert add_elements([], 5) == 0
    
    def test_k_zero(self):
        assert add_elements([1, 2, 3], 0) == 0
        assert add_elements([100, 200, 300], 0) == 0
    
    def test_k_greater_than_array_length(self):
        assert add_elements([1, 2, 3], 10) == 6
        assert add_elements([11, 22], 5) == 33
    
    def test_all_single_digit_positive(self):
        assert add_elements([1, 2, 3, 4, 5], 3) == 6
        assert add_elements([9, 8, 7, 6], 2) == 17
    
    def test_all_two_digit_positive(self):
        assert add_elements([11, 22, 33, 44], 2) == 33
        assert add_elements([99, 88, 77], 3) == 264
    
    def test_all_three_digit_positive(self):
        assert add_elements([111, 222, 333], 2) == 0
        assert add_elements([100, 200, 300, 400], 3) == 0
    
    def test_mixed_digit_lengths(self):
        assert add_elements([1, 22, 333, 4, 55], 3) == 23
        assert add_elements([9, 100, 8, 200, 7], 4) == 17
    
    def test_negative_single_digit(self):
        assert add_elements([-1, -2, -3], 2) == -3
        assert add_elements([-9, -8, -7], 3) == -24
    
    def test_negative_two_digit(self):
        assert add_elements([-11, -22, -33], 2) == 0
        assert add_elements([-99, -88], 2) == 0
    
    def test_negative_three_digit(self):
        assert add_elements([-111, -222, -333], 2) == 0
        assert add_elements([-100, -200], 1) == 0
    
    def test_mixed_positive_negative(self):
        assert add_elements([1, -2, 3, -4], 3) == 2
        assert add_elements([-11, 22, -33, 44], 2) == 22
    
    def test_zero_values(self):
        assert add_elements([0, 0, 0], 2) == 0
        assert add_elements([0, 1, 2], 3) == 3
    
    def test_k_equals_array_length(self):
        assert add_elements([1, 2, 3], 3) == 6
        assert add_elements([11, 22, 33], 3) == 66
    
    def test_large_numbers(self):
        assert add_elements([1000, 2000, 3000], 2) == 0
        assert add_elements([1, 1000, 2], 3) == 3
    
    @pytest.mark.parametrize("arr,k,expected", [
        ([1, 2, 3, 4, 5], 1, 1),
        ([10, 20, 30], 2, 30),
        ([100, 1, 2], 3, 3),
        ([-1, -10, -100], 3, -1),
        ([0], 1, 0),
        ([99, 100, 1], 2, 99),
        ([5, 4, 3, 2, 1], 5, 15)
    ])
    def test_parametrized_cases(self, arr, k, expected):
        assert add_elements(arr, k) == expected