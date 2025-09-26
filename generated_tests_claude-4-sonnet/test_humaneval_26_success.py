# Test cases for HumanEval/26
# Generated using Claude API

from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


# Generated test cases:
import pytest
from typing import List
import collections

def remove_duplicates(numbers: List[int]):
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]

class TestRemoveDuplicates:
    
    def test_empty_list(self):
        assert remove_duplicates([]) == []
    
    def test_single_element(self):
        assert remove_duplicates([1]) == [1]
    
    def test_no_duplicates(self):
        assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_all_duplicates(self):
        assert remove_duplicates([1, 1, 1, 1]) == []
    
    def test_some_duplicates(self):
        assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]
    
    def test_mixed_duplicates(self):
        assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [3, 4, 5]
    
    def test_preserves_order(self):
        assert remove_duplicates([5, 1, 3, 7, 2]) == [5, 1, 3, 7, 2]
    
    def test_negative_numbers(self):
        assert remove_duplicates([-1, -2, -2, -3]) == [-1, -3]
    
    def test_zero_values(self):
        assert remove_duplicates([0, 0, 1, 2]) == [1, 2]
    
    def test_large_numbers(self):
        assert remove_duplicates([1000000, 1000000, 999999]) == [999999]
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 1, 2, 2, 3], [3]),
        ([1, 2, 1, 3, 2, 4], [3, 4]),
        ([5, 5, 5, 5, 5], []),
        ([1, 2, 3, 1, 2, 3, 4], [4]),
        ([-1, 0, 1, -1, 0, 2], [1, 2])
    ])
    def test_parametrized_cases(self, input_list, expected):
        assert remove_duplicates(input_list) == expected
    
    def test_maintains_original_order_complex(self):
        input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 7]
        result = remove_duplicates(input_list)
        assert result == [4, 9, 2, 6, 7]
        
    def test_two_element_duplicate(self):
        assert remove_duplicates([1, 1]) == []
    
    def test_two_element_no_duplicate(self):
        assert remove_duplicates([1, 2]) == [1, 2]
    
    def test_alternating_pattern(self):
        assert remove_duplicates([1, 2, 1, 2, 3]) == [3]
