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

def test_order_by_points_positive_numbers():
    assert order_by_points([1, 11, 111]) == [1, 11, 111]

def test_order_by_points_mixed_numbers():
    assert order_by_points([13, 21, 12]) == [21, 12, 13]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_zero():
    assert order_by_points([0, 10, 100]) == [0, 10, 100]

def test_order_by_points_large_numbers():
    assert order_by_points([1000, 100, 10]) == [10, 100, 1000]

def test_order_by_points_complex_case():
    assert order_by_points([52, 23, 14, 5]) == [5, 14, 23, 52]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 11, 111], [1, 11, 111]),
    ([-1, -10, -100], [-1, -10, -100]),
    ([52, 23, 14, 5], [5, 14, 23, 52]),
    ([0, 10, 100], [0, 10, 100])
])
def test_order_by_points_parametrized(input_list, expected):
    assert order_by_points(input_list) == expected

def test_order_by_points_empty_list():
    assert order_by_points([]) == []