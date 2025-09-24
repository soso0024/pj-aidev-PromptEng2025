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
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

def test_sort_even_empty_list():
    assert sort_even([]) == []

def test_sort_even_single_element():
    assert sort_even([5]) == [5]

def test_sort_even_two_elements():
    assert sort_even([3, 7]) == [3, 7]

def test_sort_even_three_elements():
    assert sort_even([1, 2, 3]) == [1, 2, 3]

def test_sort_even_four_elements():
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

def test_sort_even_odd_length():
    assert sort_even([9, 1, 5, 2, 3]) == [3, 1, 5, 2, 9]

def test_sort_even_even_length():
    assert sort_even([8, 1, 6, 2, 4, 3]) == [4, 1, 6, 2, 8, 3]

def test_sort_even_already_sorted():
    assert sort_even([1, 5, 3, 7, 9, 2]) == [1, 5, 3, 7, 9, 2]

def test_sort_even_reverse_sorted():
    assert sort_even([9, 1, 7, 2, 5, 3, 3, 4]) == [3, 1, 5, 2, 7, 3, 9, 4]

def test_sort_even_duplicates():
    assert sort_even([2, 1, 2, 3, 2, 5]) == [2, 1, 2, 3, 2, 5]

def test_sort_even_negative_numbers():
    assert sort_even([-3, 1, -1, 2, 0, 4]) == [-3, 1, -1, 2, 0, 4]

def test_sort_even_mixed_positive_negative():
    assert sort_even([5, -1, -3, 2, 1, 4]) == [-3, -1, 1, 2, 5, 4]

@pytest.mark.parametrize("input_list,expected", [
    ([1], [1]),
    ([2, 3], [2, 3]),
    ([4, 1, 2], [2, 1, 4]),
    ([6, 5, 4, 3, 2, 1], [2, 5, 4, 3, 6, 1]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([-1, -2, -3, -4], [-3, -2, -1, -4])
])
def test_sort_even_parametrized(input_list, expected):
    assert sort_even(input_list) == expected
