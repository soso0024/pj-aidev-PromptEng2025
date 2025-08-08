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

def test_exchange_all_even_lists():
    assert exchange([2, 4, 6, 8], [1, 3, 5, 7]) == "YES"

def test_exchange_mixed_lists_possible():
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES"

def test_exchange_mixed_lists_impossible():
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO"

def test_exchange_single_odd_element():
    assert exchange([1], [2]) == "YES"

def test_exchange_single_odd_element_impossible():
    assert exchange([1], [1]) == "NO"

def test_exchange_multiple_odd_elements():
    assert exchange([1, 3, 5], [2, 4, 6, 8, 10]) == "YES"

def test_exchange_not_enough_even_elements():
    assert exchange([1, 3, 5, 7], [2, 4]) == "NO"

@pytest.mark.parametrize("lst1,lst2,expected", [
    ([1, 2, 3, 4], [1, 2, 3, 4], "YES"),
    ([1, 2, 3, 4], [1, 5, 3, 4], "NO"),
    ([2, 4, 6, 8], [1, 3, 5, 7], "YES"),
    ([1, 3, 5], [2, 4, 6, 8, 10], "YES"),
    ([1, 3, 5, 7], [2, 4], "NO")
])
def test_exchange_parametrized(lst1, lst2, expected):
    assert exchange(lst1, lst2) == expected
