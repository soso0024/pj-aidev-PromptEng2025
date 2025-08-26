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
        raise IndexError("Cannot find minimum sum of an empty list")
    
    min_sum = float('inf')
    current_sum = 0
    
    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    
    return -min_sum

def test_minSubArraySum_normal_case():
    assert minSubArraySum([3, -1, 2, 1, -2]) == -1
    assert minSubArraySum([1, 2, 3, 4]) == -10
    assert minSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3]) == -1

def test_minSubArraySum_all_negative():
    assert minSubArraySum([-1, -2, -3, -4]) == -1
    assert minSubArraySum([-5]) == -5

def test_minSubArraySum_single_element():
    assert minSubArraySum([0]) == 0
    assert minSubArraySum([10]) == -10
    assert minSubArraySum([-10]) == -10

def test_minSubArraySum_empty_list():
    with pytest.raises(IndexError):
        minSubArraySum([])

@pytest.mark.parametrize("nums,expected", [
    ([1, -2, 3, 10, -5], -11),
    ([5, -3, 5], -7),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], -1)
])
def test_minSubArraySum_parametrized(nums, expected):
    assert minSubArraySum(nums) == expected

def test_minSubArraySum_large_numbers():
    assert minSubArraySum([10**6, -10**6, 10**6]) == -10**6
    assert minSubArraySum([-10**9, 10**9, -10**9]) == -10**9