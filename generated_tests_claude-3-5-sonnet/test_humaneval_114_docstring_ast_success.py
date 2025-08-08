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

def test_basic_positive_array():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1

def test_all_negative_array():
    assert minSubArraySum([-1, -2, -3]) == -6

def test_single_element():
    assert minSubArraySum([5]) == 5
    assert minSubArraySum([-5]) == -5

def test_two_elements():
    assert minSubArraySum([1, 2]) == 1
    assert minSubArraySum([-1, -2]) == -3

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4, 5], 1),
    ([-1, -2, -3, -4, -5], -15),
    ([0, 0, 0, 0], 0),
    ([1, -2, 3, -4], -4),
    ([10, -5, 7, -8, 6], -8),
    ([100, 200, -300, 400], -300),
    ([1, 1, 1, -5, 1, 1], -5),
])
def test_various_arrays(nums, expected):
    assert minSubArraySum(nums) == expected

def test_alternating_signs():
    assert minSubArraySum([1, -1, 1, -1]) == -1

def test_zero_with_positives():
    assert minSubArraySum([0, 1, 2, 0, 3]) == 0

def test_zero_with_negatives():
    assert minSubArraySum([0, -1, -2, 0, -3]) == -6

@pytest.mark.parametrize("invalid_input", [
    [],
    None,
    "string",
    [1, "2", 3],
    [1, None, 3]
])
def test_invalid_inputs(invalid_input):
    with pytest.raises((ValueError, TypeError, AttributeError)):
        minSubArraySum(invalid_input)

def test_large_numbers():
    assert minSubArraySum([1000000, -2000000, 3000000]) == -2000000

def test_repeated_numbers():
    assert minSubArraySum([5, 5, 5, 5, 5]) == 5

def test_mixed_large_and_small():
    assert minSubArraySum([1000000, -1, 2, -5, 1000000]) == -5