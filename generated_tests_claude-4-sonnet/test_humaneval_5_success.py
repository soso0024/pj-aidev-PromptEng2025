# Test cases for HumanEval/5
# Generated using Claude API

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result


# Generated test cases:
import pytest
from typing import List

def intersperse(numbers: List[int], delimeter: int):
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result

class TestIntersperse:
    
    def test_empty_list(self):
        assert intersperse([], 0) == []
        assert intersperse([], 5) == []
        assert intersperse([], -1) == []
    
    def test_single_element(self):
        assert intersperse([1], 0) == [1]
        assert intersperse([5], 9) == [5]
        assert intersperse([-3], 2) == [-3]
    
    def test_two_elements(self):
        assert intersperse([1, 2], 0) == [1, 0, 2]
        assert intersperse([5, 10], 99) == [5, 99, 10]
        assert intersperse([-1, -2], 3) == [-1, 3, -2]
    
    def test_multiple_elements(self):
        assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
        assert intersperse([1, 2, 3, 4], 5) == [1, 5, 2, 5, 3, 5, 4]
        assert intersperse([10, 20, 30, 40, 50], 99) == [10, 99, 20, 99, 30, 99, 40, 99, 50]
    
    def test_negative_numbers(self):
        assert intersperse([-1, -2, -3], -5) == [-1, -5, -2, -5, -3]
        assert intersperse([-10, 5, -15], 0) == [-10, 0, 5, 0, -15]
    
    def test_zero_delimiter(self):
        assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
        assert intersperse([0, 1, 0], 0) == [0, 0, 1, 0, 0]
    
    def test_same_numbers_and_delimiter(self):
        assert intersperse([5, 5, 5], 5) == [5, 5, 5, 5, 5]
        assert intersperse([1, 1], 1) == [1, 1, 1]
    
    def test_large_numbers(self):
        assert intersperse([1000000, 2000000], 999999) == [1000000, 999999, 2000000]
        assert intersperse([999, 888, 777], 111) == [999, 111, 888, 111, 777]
    
    @pytest.mark.parametrize("numbers,delimiter,expected", [
        ([1], 0, [1]),
        ([1, 2], 9, [1, 9, 2]),
        ([1, 2, 3], 0, [1, 0, 2, 0, 3]),
        ([4, 5, 6, 7], 8, [4, 8, 5, 8, 6, 8, 7]),
        ([], 5, []),
        ([100], 200, [100]),
        ([-1, -2], -3, [-1, -3, -2])
    ])
    def test_parametrized_cases(self, numbers, delimiter, expected):
        assert intersperse(numbers, delimiter) == expected
