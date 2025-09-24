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

def test_count_nums_empty_list():
    assert count_nums([]) == 0

def test_count_nums_all_positive():
    assert count_nums([123, 456, 789]) == 3

def test_count_nums_all_negative():
    assert count_nums([-123, -456, -789]) == 3

def test_count_nums_mixed():
    assert count_nums([123, -456, 789, -987]) == 4

def test_count_nums_single_element():
    assert count_nums([123]) == 1

def test_count_nums_zero():
    assert count_nums([0, 123, -456, 0]) == 2

def test_count_nums_single_negative():
    assert count_nums([-123]) == 1

def test_count_nums_single_zero():
    assert count_nums([0]) == 0

def test_count_nums_large_numbers():
    assert count_nums([12345678901, -98765432109, 87654321098]) == 3

def test_count_nums_non_integer_elements():
    with pytest.raises(TypeError):
        count_nums([123, 'abc', 456.0])

def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = abs(n), -1 
        n = [int(i) for i in str(abs(n))]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))