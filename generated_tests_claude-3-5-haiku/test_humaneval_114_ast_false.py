# Test cases for HumanEval/114
# Generated using Claude API


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum


# Generated test cases:
import pytest

def minSubArraySum(nums):
    if not nums:
        raise TypeError("Input list cannot be empty")
    
    min_sum = float('inf')
    current_sum = 0
    
    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    
    return -sum(nums) if sum(nums) > 0 else -min_sum

def test_minSubArraySum_empty_list():
    with pytest.raises(TypeError):
        minSubArraySum([])

def test_minSubArraySum_single_element():
    assert minSubArraySum([5]) == -5
    assert minSubArraySum([-3]) == -3

def test_minSubArraySum_positive_numbers():
    assert minSubArraySum([1, 2, 3, 4]) == -10

def test_minSubArraySum_negative_numbers():
    assert minSubArraySum([-1, -2, -3, -4]) == -10

def test_minSubArraySum_mixed_numbers():
    assert minSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == -1

def test_minSubArraySum_all_zeros():
    assert minSubArraySum([0, 0, 0]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], -6),
    ([-1, -2, -3], -6),
    ([5, -4, 3, -2], -4),
    ([10, -5, 7, -3], -5)
])
def test_minSubArraySum_parametrized(input_list, expected):
    assert minSubArraySum(input_list) == expected

def test_minSubArraySum_large_numbers():
    assert minSubArraySum([1000, 2000, 3000]) == -6000

def test_minSubArraySum_alternating_signs():
    assert minSubArraySum([-1, 1, -1, 1]) == -2