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

def test_minSubArraySum_positive_numbers():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1

def test_minSubArraySum_negative_numbers():
    assert minSubArraySum([-1, -2, -3]) == -6

def test_minSubArraySum_mixed_numbers():
    assert minSubArraySum([-1, 2, -3, 4]) == -3

def test_minSubArraySum_single_element():
    assert minSubArraySum([5]) == 5
    assert minSubArraySum([-5]) == -5

def test_minSubArraySum_all_positive():
    assert minSubArraySum([1, 2, 3, 4]) == 1

def test_minSubArraySum_large_numbers():
    assert minSubArraySum([1000, -500, 2000, -1500]) == -1500

@pytest.mark.parametrize("input_array,expected", [
    ([2, 3, 4, 1, 2, 4], 1),
    ([-1, -2, -3], -6),
    ([-1, 2, -3, 4], -3),
    ([5], 5),
    ([-5], -5),
    ([1, 2, 3, 4], 1),
    ([1000, -500, 2000, -1500], -1500)
])
def test_minSubArraySum_parametrized(input_array, expected):
    assert minSubArraySum(input_array) == expected

def test_minSubArraySum_empty_array():
    with pytest.raises(ValueError):
        minSubArraySum([])