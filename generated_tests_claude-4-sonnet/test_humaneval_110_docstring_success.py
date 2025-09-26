# Test cases for HumanEval/110
# Generated using Claude API


def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """

    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            odd += 1
    for i in lst2:
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"
            


# Generated test cases:
import pytest

def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            odd += 1
    for i in lst2:
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"

@pytest.mark.parametrize("lst1,lst2,expected", [
    ([1, 2, 3, 4], [1, 2, 3, 4], "YES"),
    ([1, 2, 3, 4], [1, 5, 3, 4], "NO"),
    ([2, 4, 6], [1, 3, 5], "YES"),
    ([1, 3, 5], [2, 4, 6], "YES"),
    ([1, 3, 5, 7], [2, 4], "NO"),
    ([1, 3, 5, 7], [2, 4, 6, 8], "YES"),
    ([2], [1], "YES"),
    ([1], [2], "YES"),
    ([1], [1], "NO"),
    ([2], [2], "YES"),
    ([1, 1, 1], [2, 2, 2], "YES"),
    ([1, 1, 1, 1], [2, 2, 2], "NO"),
    ([0, 2, 4], [1, 3, 5], "YES"),
    ([0], [0], "YES"),
    ([-1, -3], [-2, -4], "YES"),
    ([-1, -3, -5], [-2], "NO"),
    ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], "YES"),
    ([1, 3, 5, 7, 9], [2, 4, 6], "NO"),
    ([10, 20, 30], [11, 13, 15], "YES"),
    ([11, 13, 15, 17, 19], [10, 20], "NO")
])
def test_exchange(lst1, lst2, expected):
    assert exchange(lst1, lst2) == expected

def test_exchange_single_elements():
    assert exchange([2], [4]) == "YES"
    assert exchange([1], [3]) == "NO"

def test_exchange_all_even_lst1():
    assert exchange([2, 4, 6, 8], [1, 3, 5]) == "YES"

def test_exchange_all_odd_lst1():
    assert exchange([1, 3, 5], [2, 4, 6, 8, 10]) == "YES"

def test_exchange_all_odd_both_lists():
    assert exchange([1, 3, 5], [7, 9, 11]) == "NO"

def test_exchange_all_even_both_lists():
    assert exchange([2, 4, 6], [8, 10, 12]) == "YES"

def test_exchange_large_numbers():
    assert exchange([100, 101, 102], [103, 104, 105]) == "YES"
    assert exchange([101, 103, 105], [107, 109]) == "NO"

def test_exchange_negative_numbers():
    assert exchange([-2, -1, 0], [-3, -4, 2]) == "YES"
    assert exchange([-1, -3, -5], [-7, -9]) == "NO"

def test_exchange_mixed_positive_negative():
    assert exchange([-1, 2, -3, 4], [5, -6, 7, -8]) == "YES"
    assert exchange([-1, -3, 5, 7], [-9, 11]) == "NO"
