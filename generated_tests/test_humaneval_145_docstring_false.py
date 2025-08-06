# Test cases for HumanEval/145
# Generated using Claude API


def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)


# Generated test cases:
import pytest

@pytest.mark.parametrize("nums,expected", [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([], []),
    ([1], [1]),
    ([-1], [-1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10, 20, 30, 40], [10, 20, 30, 40]),
    ([-10, -20, -30, -40], [-40, -30, -20, -10]),
    ([11, 11, 11], [11, 11, 11]),
    ([-22, 22], [-22, 22]),
    ([999, -999, 0], [0, -999, 999]),
    ([42, -42, 24, -24], [-42, -24, 24, 42]),
    ([100, 200, 300], [100, 200, 300]),
    ([-15, 15, -51, 51], [-51, -15, 15, 51]),
    ([1234, 4321, -1234, -4321], [-4321, -1234, 1234, 4321])
])
def test_order_by_points_parametrized(nums, expected):
    result = order_by_points(nums)
    assert len(result) == len(expected)
    for i in range(len(result)):
        assert result[i] == expected[i]

def test_order_by_points_single_digit():
    assert order_by_points([5]) == [5]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_same_digit_sum():
    nums = [11, 11]
    result = order_by_points(nums.copy())
    assert result == [11, 11]
    assert result[0] is not result[1]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -2, -3]) == [-1, -2, -3]

def test_order_by_points_mixed_numbers():
    assert order_by_points([1, -1, 2, -2]) == [-1, 1, -2, 2]

def test_order_by_points_large_numbers():
    assert order_by_points([1000, 2000, 3000]) == [1000, 2000, 3000]

def test_order_by_points_preserve_order_for_equal_sums():
    assert order_by_points([11, 101, 1001]) == [11, 101, 1001]