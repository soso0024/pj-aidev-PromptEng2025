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

def test_exchange_basic():
    assert exchange([1, 3, 5], [2, 4, 6]) == "YES"
    assert exchange([1, 3, 5], [1, 3, 5]) == "NO"

def test_exchange_empty_lists():
    assert exchange([], []) == "YES"
    assert exchange([], [2, 4]) == "YES"
    assert exchange([1, 3], []) == "NO"

def test_exchange_single_element():
    assert exchange([1], [2]) == "YES"
    assert exchange([1], [1]) == "NO"

@pytest.mark.parametrize("lst1, lst2, expected", [
    ([1, 2, 3], [2, 4, 6], "YES"),
    ([1, 3, 5, 7], [2, 4], "NO"),
    ([2, 4, 6], [1, 3, 5], "YES"),
    ([1, 1, 1], [2, 2, 2], "YES"),
    ([1, 3, 5], [1, 3, 5], "NO"),
    ([0, 2, 4], [0, 2, 4], "YES"),
])
def test_exchange_parametrized(lst1, lst2, expected):
    assert exchange(lst1, lst2) == expected

def test_exchange_large_numbers():
    assert exchange([999, 1001], [1000, 2000]) == "YES"
    assert exchange([999, 1001, 1003], [1000]) == "NO"

def test_exchange_negative_numbers():
    assert exchange([-1, -3], [-2, -4]) == "YES"
    assert exchange([-1, -3], [-1, -3]) == "NO"

def test_exchange_mixed_numbers():
    assert exchange([-1, 0, 1], [2, -2, 4]) == "YES"
    assert exchange([-1, 1, 3], [-2, 0]) == "NO"

def test_exchange_zeros():
    assert exchange([0, 0, 0], [0, 0, 0]) == "YES"
    assert exchange([1, 1], [0, 0]) == "YES"
