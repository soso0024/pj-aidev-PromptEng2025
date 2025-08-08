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

def test_minSubArraySum_normal_positive_array():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1

def test_minSubArraySum_all_negative_array():
    assert minSubArraySum([-1, -2, -3]) == -6

def test_minSubArraySum_mixed_array():
    assert minSubArraySum([-1, 2, -3, 4]) == -4

def test_minSubArraySum_single_element_positive():
    assert minSubArraySum([5]) == 5

def test_minSubArraySum_single_element_negative():
    assert minSubArraySum([-5]) == -5

def test_minSubArraySum_empty_array():
    with pytest.raises(ValueError):
        minSubArraySum([])

@pytest.mark.parametrize("input_array,expected", [
    ([1, 2, 3, 4], 1),
    ([-1, -2, -3, -4], -10),
    ([10, -5, 7, -3], -8),
    ([0, 0, 0], 0)
])
def test_minSubArraySum_parametrized(input_array, expected):
    assert minSubArraySum(input_array) == expected