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

@pytest.mark.parametrize("nums,expected", [
    ([1, -2, 3, 10, -4, 7, 2, -5], -2),
    ([-2, -3, 4, -1, -2, 1, 5, -3], -1),
    ([1], 1),
    ([-1], -1),
    ([0, 0, 0], 0),
    ([-1, -2, -3, -4, -5], -1),
    ([10, -10, 10, -10, 10], -10),
])
def test_minSubArraySum(nums, expected):
    assert minSubArraySum(nums) == expected

def minSubArraySum(nums):
    max_sum = 0
    s = 0
    for num in nums:
        s += num
        if s < 0:
            s = 0
        max_sum = max(s, max_sum)
    min_sum = -max_sum
    return min_sum