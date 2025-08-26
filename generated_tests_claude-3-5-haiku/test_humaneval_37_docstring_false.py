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

def test_sort_even_basic():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

def test_sort_even_empty_list():
    assert sort_even([]) == []

def test_sort_even_single_element():
    assert sort_even([5]) == [5]

def test_sort_even_multiple_elements():
    assert sort_even([7, 8, 1, 2, 5, 6]) == [1, 8, 5, 2, 7, 6]

def test_sort_even_negative_numbers():
    assert sort_even([-3, -2, -1, 0]) == [-3, -2, -1, 0]

def test_sort_even_mixed_numbers():
    assert sort_even([10, 9, 8, 7, 6, 5]) == [6, 9, 8, 7, 10, 5]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([6, 5, 4, 3, 2, 1], [4, 5, 2, 3, 6, 1]),
    ([100, 1, 50, 2, 25, 3], [25, 1, 50, 2, 100, 3])
])
def test_sort_even_parametrized(input_list, expected):
    assert sort_even(input_list) == expected