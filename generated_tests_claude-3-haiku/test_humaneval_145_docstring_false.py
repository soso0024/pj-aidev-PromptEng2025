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

def test_order_by_points_empty_list():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([42]) == [42]

def test_order_by_points_positive_numbers():
    assert order_by_points([1, 11, 111, 2, 22, 222]) == [1, 2, 11, 22, 111, 222]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -111, -2, -22, -222]) == [-111, -222, -11, -22, -1, -2]

def test_order_by_points_mixed_numbers():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_duplicate_digits_sum():
    assert order_by_points([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]

@pytest.mark.parametrize("input,expected", [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([], []),
    ([42], [42]),
    ([1, 11, 111, 2, 22, 222], [1, 2, 11, 22, 111, 222]),
    ([-1, -11, -111, -2, -22, -222], [-111, -222, -11, -22, -1, -2]),
    ([10, 20, 30, 40, 50], [10, 20, 30, 40, 50])
])
def test_order_by_points_parametrized(input, expected):
    assert order_by_points(input) == expected

def order_by_points(nums):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)