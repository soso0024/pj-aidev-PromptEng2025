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


def remove_duplicates(numbers: List[int]) -> List[int]:
    import collections
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
        assert remove_duplicates([1, 1, 2, 2, 3, 3]) == []
    
    def test_some_duplicates(self):
        assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    
    def test_multiple_duplicates_same_element(self):
        assert remove_duplicates([1, 1, 1, 2, 3]) == [2, 3]
    
    def test_order_preservation(self):
        assert remove_duplicates([5, 1, 3, 1, 4, 2, 3]) == [5, 4, 2]
    
    def test_negative_numbers(self):
        assert remove_duplicates([-1, -2, -1, 3, -2]) == [3]
    
    def test_mixed_positive_negative(self):
        assert remove_duplicates([-1, 1, -1, 2, 1, 3]) == [2, 3]
    
    def test_zeros(self):
        assert remove_duplicates([0, 1, 0, 2]) == [1, 2]
    
    def test_large_numbers(self):
        assert remove_duplicates([1000000, 999999, 1000000, 888888]) == [999999, 888888]
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1, 2, 1], [2]),
        ([1, 1], []),
        ([1, 2, 3, 4, 5, 1], [2, 3, 4, 5]),
        ([7, 7, 7, 7], []),
        ([1, 2, 3, 4, 3, 2, 1, 5], [4, 5])
    ])
    def test_parametrized_cases(self, input_list, expected):
        assert remove_duplicates(input_list) == expected
    
    def test_consecutive_duplicates(self):
        assert remove_duplicates([1, 1, 2, 3, 3, 4]) == [2, 4]
    
    def test_non_consecutive_duplicates(self):
        assert remove_duplicates([1, 2, 3, 1, 4, 2]) == [3, 4]
    
    def test_long_list_with_pattern(self):
        input_list = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8]
        expected = [3, 4, 5, 6, 7, 8]
        assert remove_duplicates(input_list) == expected
