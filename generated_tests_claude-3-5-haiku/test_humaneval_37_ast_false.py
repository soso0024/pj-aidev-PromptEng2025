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
    if not l:
        return []
    
    evens = l[::2]
    odds = l[1::2]
    
    evens.sort()
    
    ans = []
    for i in range(max(len(evens), len(odds))):
        if i < len(evens):
            ans.append(evens[i])
        if i < len(odds):
            ans.append(odds[i])
    
    return ans

def test_sort_even_basic():
    assert sort_even([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert sort_even([5, 3, 2, 8]) == [5, 2, 3, 8]
    assert sort_even([1, 3, 2, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_sort_even_empty_list():
    assert sort_even([]) == []

def test_sort_even_single_element():
    assert sort_even([1]) == [1]
    assert sort_even([2]) == [2]

def test_sort_even_all_odd():
    assert sort_even([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_sort_even_all_even():
    assert sort_even([4, 2, 6, 8]) == [2, 4, 6, 8]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([6, 4, 2, 1, 3, 5], [1, 2, 3, 4, 5, 6]),
    ([10, 9, 8, 7, 6, 5], [5, 8, 7, 10, 9, 6]),
])
def test_sort_even_parametrized(input_list, expected):
    assert sort_even(input_list) == expected

def test_sort_even_uneven_length():
    assert sort_even([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort_even([4, 3, 2, 1]) == [2, 3, 4, 1]