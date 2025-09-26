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
    return sorted(nums, key=digits_sum)

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]
    assert order_by_points([-5]) == [-5]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_all_positive():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert order_by_points([15, 23, 14, 32]) == [23, 14, 32, 15]

def test_all_negative():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]
    assert order_by_points([-15, -23, -14, -32]) == [-32, -23, -14, -15]

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 2, -2]) == [-2, -1, 1, 2]
    assert order_by_points([12, -12, 21, -21]) == [-21, -12, 12, 21]

def test_same_digit_sum():
    assert order_by_points([12, 21, 30]) == [12, 21, 30]
    assert order_by_points([123, 321, 132]) == [123, 321, 132]

def test_zero():
    assert order_by_points([0]) == [0]
    assert order_by_points([0, 1, -1]) == [-1, 0, 1]
    assert order_by_points([10, 0, -10]) == [-10, 0, 10]

def test_large_numbers():
    assert order_by_points([999, 111, 222]) == [111, 222, 999]
    assert order_by_points([1000, 100, 10, 1]) == [1000, 100, 10, 1]

def test_negative_with_different_digit_sums():
    assert order_by_points([-123, -45, -6]) == [-6, -45, -123]
    assert order_by_points([-99, -11, -22]) == [-99, -11, -22]

def test_preserve_original_order_same_sum():
    assert order_by_points([13, 22, 31, 40]) == [13, 22, 31, 40]
    assert order_by_points([101, 110, 200]) == [101, 110, 200]

@pytest.mark.parametrize("nums,expected", [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([], []),
    ([0], [0]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([-5, -4, -3, -2, -1], [-5, -4, -3, -2, -1]),
    ([100, 10, 1], [100, 10, 1]),
    ([-100, -10, -1], [-100, -10, -1])
])
def test_parametrized_cases(nums, expected):
    assert order_by_points(nums) == expected