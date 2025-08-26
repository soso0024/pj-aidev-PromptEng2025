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

def test_minSubArraySum_basic_positive_case():
    assert minSubArraySum([1, 2, 3, 4]) == -10

def test_minSubArraySum_mixed_numbers():
    assert minSubArraySum([-1, 2, -3, 4]) == -4

def test_minSubArraySum_all_negative():
    assert minSubArraySum([-1, -2, -3]) == -1

def test_minSubArraySum_single_element():
    assert minSubArraySum([5]) == -5

def test_minSubArraySum_empty_list():
    with pytest.raises(ValueError):
        minSubArraySum([])

def test_minSubArraySum_zero_elements():
    assert minSubArraySum([0]) == 0

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], -10),
    ([-1, 2, -3, 4], -4),
    ([-1, -2, -3], -1),
    ([5], -5),
    ([0], 0)
])
def test_minSubArraySum_parametrized(input_list, expected):
    assert minSubArraySum(input_list) == expected