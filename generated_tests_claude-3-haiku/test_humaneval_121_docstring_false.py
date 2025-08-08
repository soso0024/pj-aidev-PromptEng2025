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

def test_empty_list():
    assert solution([]) == 0

def test_all_even_positions_odd():
    assert solution([1, 2, 3, 4, 5]) == 12

def test_all_odd_positions_odd():
    assert solution([1, 3, 5, 7]) == 16

def test_mixed_even_odd_positions():
    assert solution([5, 8, 7, 1]) == 12

def test_all_even_positions_even():
    assert solution([2, 4, 6, 8]) == 0

def test_all_odd_positions_even():
    assert solution([2, 3, 4, 5]) == 3

def test_single_element_list():
    assert solution([1]) == 1

def test_single_element_even_list():
    assert solution([2]) == 0

@pytest.mark.parametrize("input,expected", [
    ([30, 13, 24, 321], 13),
    ([3, 3, 3, 3, 3], 9),
    ([1, 1, 1, 1, 1], 3),
    ([2, 2, 2, 2, 2], 0)
])
def test_various_inputs(input, expected):
    assert solution(input) == expected