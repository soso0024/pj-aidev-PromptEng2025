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

@pytest.mark.parametrize("lst1, lst2, expected", [
    ([1, 2, 3, 4], [1, 2, 3, 4], "YES"),
    ([1, 2, 3, 4], [1, 5, 3, 4], "NO"),
    ([2, 4, 6, 8], [1, 3, 5, 7], "YES"),
    ([1, 3, 5, 7], [2, 4, 6, 8], "YES"),
    ([1, 1, 1, 1], [1, 1, 1, 1], "NO"),
    ([2, 2, 2, 2], [1, 1, 1, 1], "YES"),
    ([1], [2], "YES"),
    ([1], [1], "NO"),
    ([1, 3, 5], [2], "NO"),
    ([1, 3, 5], [2, 4, 6, 8], "YES"),
    ([99, 101], [2, 4, 6], "YES"),
    ([1, 3, 5, 7, 9], [2], "NO"),
    ([1, 2], [2, 1], "YES"),
    ([1, 3, 5, 7], [4], "NO"),
])
def test_exchange(lst1, lst2, expected):
    assert exchange(lst1, lst2) == expected

def test_exchange_same_list():
    assert exchange([2, 4, 6], [2, 4, 6]) == "YES"

def test_exchange_all_odd():
    assert exchange([1, 3, 5], [1, 3, 5]) == "NO"

def test_exchange_minimal():
    assert exchange([1], [2]) == "YES"

def test_exchange_single_odd():
    assert exchange([1], [1]) == "NO"

def test_exchange_large_numbers():
    assert exchange([999999], [1000000]) == "YES"

def test_exchange_zero():
    assert exchange([0], [1]) == "YES"
    
def test_exchange_negative_numbers():
    assert exchange([-1, -3], [-2, -4]) == "YES"
    assert exchange([-1, -3], [-1, -3]) == "NO"
