# Test cases for HumanEval/108
# Generated using Claude API


def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


# Generated test cases:
import pytest

def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0: 
            n, neg = abs(n), -1 
        n = [int(i) for i in str(abs(n))]
        n[0] = n[0] * neg
        return sum(n)
    return len([x for x in [digits_sum(i) for i in arr] if x > 0])

def test_count_nums_positive_numbers():
    assert count_nums([123, 456, 789]) == 3
    assert count_nums([1, 2, 3]) == 3
    assert count_nums([100, 200, 300]) == 3

def test_count_nums_negative_numbers():
    assert count_nums([-123, -456, -789]) == 3
    assert count_nums([-1, -2, -3]) == 0
    assert count_nums([-100, -200, -300]) == 0

def test_count_nums_mixed_numbers():
    assert count_nums([123, -456, 789]) == 3
    assert count_nums([1, -2, 3]) == 2
    assert count_nums([100, -200, 300]) == 2

def test_count_nums_empty_list():
    assert count_nums([]) == 0

def test_count_nums_single_element():
    assert count_nums([123]) == 1
    assert count_nums([-123]) == 1

def test_count_nums_zero():
    assert count_nums([0, 0, 0]) == 0

def test_count_nums_non_numeric_elements():
    with pytest.raises(ValueError):
        count_nums([123, 'abc', 456])