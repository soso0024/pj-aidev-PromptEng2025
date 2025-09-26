# Test cases for HumanEval/121
# Generated using Claude API


def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])


# Generated test cases:
import pytest

def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])

class TestSolution:
    
    def test_empty_list(self):
        assert solution([]) == 0
    
    def test_single_odd_element(self):
        assert solution([1]) == 1
    
    def test_single_even_element(self):
        assert solution([2]) == 0
    
    def test_two_elements_first_odd(self):
        assert solution([1, 2]) == 1
    
    def test_two_elements_first_even(self):
        assert solution([2, 3]) == 0
    
    def test_all_odd_numbers(self):
        assert solution([1, 3, 5, 7, 9]) == 15
    
    def test_all_even_numbers(self):
        assert solution([2, 4, 6, 8, 10]) == 0
    
    def test_mixed_numbers_pattern1(self):
        assert solution([1, 2, 3, 4, 5]) == 9
    
    def test_mixed_numbers_pattern2(self):
        assert solution([2, 1, 4, 3, 6, 5]) == 0
    
    def test_zeros_in_list(self):
        assert solution([0, 1, 0, 3, 0]) == 0
    
    def test_negative_odd_numbers(self):
        assert solution([-1, -2, -3, -4, -5]) == -9
    
    def test_negative_even_numbers(self):
        assert solution([-2, -4, -6, -8]) == 0
    
    def test_mixed_positive_negative(self):
        assert solution([-1, 2, 3, -4, 5]) == 7
    
    def test_large_numbers(self):
        assert solution([1001, 1002, 1003, 1004]) == 2004
    
    def test_long_list(self):
        lst = list(range(1, 21))
        expected = sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])
        assert solution(lst) == expected
    
    @pytest.mark.parametrize("input_list,expected", [
        ([1], 1),
        ([2], 0),
        ([1, 2, 3], 4),
        ([0, 1, 2, 3, 4, 5], 0),
        ([-1, -3, -5], -6),
        ([1, 1, 1, 1, 1], 3)
    ])
    def test_parametrized_cases(self, input_list, expected):
        assert solution(input_list) == expected