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

def test_empty_list():
    assert order_by_points([]) == []

def test_single_number():
    assert order_by_points([1]) == [1]

def test_positive_numbers():
    assert order_by_points([10, 2, 3, 4, 5]) == [10, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-10, -2, -3, -4, -5]) == [-5, -4, -3, -2, -10]

def test_mixed_numbers():
    assert order_by_points([-23, 345, -5, 19, -321, 2, -1000]) == [-5, -1000, -321, -23, 2, 19, 345]

@pytest.mark.parametrize("input_nums, expected", [
    ([1, 11, 2, 22], [1, 11, 2, 22]),
    ([99, 100, 101, 98], [100, 101, 98, 99]),
    ([-1, -2, -3, 1, 2, 3], [-3, -2, -1, 1, 2, 3]),
    ([0, 100, -100, 50, -50], [-50, -100, 0, 100, 50])
])
def test_various_number_combinations(input_nums, expected):
    assert order_by_points(input_nums) == expected

def test_large_numbers():
    assert order_by_points([1000000, 2000000, -3000000]) == [-3000000, 1000000, 2000000]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 2, 2, 3, 3]) == [1, 1, 2, 2, 3, 3]

def test_single_digit_numbers():
    assert order_by_points([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_numbers_with_same_digit_sum():
    assert order_by_points([19, 91, 82, 28]) == [19, 91, 82, 28]

def test_zero():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_all_negative():
    assert order_by_points([-5, -15, -25, -35]) == [-5, -35, -25, -15]