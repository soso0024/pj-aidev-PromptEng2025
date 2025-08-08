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

def order_by_points(nums):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=lambda x: (digits_sum(x), nums.index(x)))

def test_order_by_points_positive_numbers():
    assert order_by_points([1, 11, 111]) == [1, 11, 111]
    assert order_by_points([10, 2, 30]) == [2, 10, 30]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -111]) == [-1, -11, -111]
    assert order_by_points([-10, -2, -30]) == [-2, -10, -30]

def test_order_by_points_mixed_numbers():
    assert order_by_points([-1, 1, 0]) == [0, -1, 1]
    assert order_by_points([10, -10, 0]) == [0, -10, 10]

def test_order_by_points_complex_cases():
    assert order_by_points([13, 31, 22]) == [22, 13, 31]
    assert order_by_points([-13, 31, -22]) == [-22, -13, 31]

def test_order_by_points_empty_list():
    assert order_by_points([]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([1, 11, 111], [1, 11, 111]),
    ([-1, -11, -111], [-1, -11, -111]),
    ([10, 2, 30], [2, 10, 30]),
    ([13, 31, 22], [22, 13, 31]),
    ([], [])
])
def test_order_by_points_parametrized(input_list, expected):
    assert order_by_points(input_list) == expected