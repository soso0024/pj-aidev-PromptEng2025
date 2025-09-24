# Test cases for HumanEval/37
# Generated using Claude API



def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans


# Generated test cases:
import pytest

def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.append(e)
        ans.append(o)
    if len(l) > len(ans):
        ans.append(l[-1])
    return ans

def test_sort_even_empty_list():
    assert sort_even([]) == []

def test_sort_even_single_element():
    assert sort_even([1]) == [1]

def test_sort_even_even_length():
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

def test_sort_even_odd_length():
    assert sort_even([1, 2, 3]) == [1, 2, 3]

def test_sort_even_already_sorted():
    assert sort_even([1, 4, 3, 6]) == [1, 4, 3, 6]

def test_sort_even_reverse_sorted():
    assert sort_even([6, 4, 3, 1]) == [3, 6, 4, 1]

def test_sort_even_duplicate_values():
    assert sort_even([5, 2, 3, 2]) == [2, 5, 3, 2]