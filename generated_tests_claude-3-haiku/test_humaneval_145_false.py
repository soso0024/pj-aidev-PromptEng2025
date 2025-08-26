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
from solution import order_by_points

@pytest.mark.parametrize("nums,expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]),
    ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([1, -2, 3, -4, 5], [5, 1, 3, -2, -4]),
    ([11, 22, 33, 44, 55], [11, 22, 33, 44, 55]),
    ([100, 200, 300, 400, 500], [100, 200, 300, 400, 500]),
    ([-100, -200, -300, -400, -500], [-100, -200, -300, -400, -500]),
    ([1, 10, 100, 1000, 10000], [1, 10, 100, 1000, 10000]),
    ([-1, -10, -100, -1000, -10000], [-1, -10, -100, -1000, -10000]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([1, -1, 2, -2, 3, -3, 4, -4, 5, -5], [5, 1, 3, -1, -2, -3, -4, -5, 2, 4]),
    ([11, 22, 33, 44, 55, 66, 77, 88, 99], [11, 22, 33, 44, 55, 66, 77, 88, 99])
])
def test_order_by_points(nums, expected):
    assert order_by_points(nums) == expected