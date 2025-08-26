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
from sort_even import sort_even
import pytest

def test_sort_even_empty_list():
    assert sort_even([]) == []

def test_sort_even_single_element():
    assert sort_even([1]) == [1]

def test_sort_even_even_length():
    assert sort_even([1, 2, 3, 4]) == [2, 1, 4, 3]

def test_sort_even_odd_length():
    assert sort_even([1, 2, 3, 4, 5]) == [2, 1, 4, 3, 5]

@pytest.mark.parametrize("input,expected", [
    ([6, 1, 2, 3, 4, 5], [2, 1, 4, 3, 6, 5]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [8, 9, 6, 7, 4, 5, 2, 3, 10, 1]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 0])
])
def test_sort_even_various_inputs(input, expected):
    assert sort_even(input) == expected

def test_sort_even_non_list_input():
    with pytest.raises(TypeError):
        sort_even(123)