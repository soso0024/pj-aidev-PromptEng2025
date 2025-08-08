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
    assert sort_even([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_sort_even_unsorted():
    assert sort_even([5, 2, 1, 4, 3, 6]) == [1, 2, 3, 4, 5, 6]

def test_sort_even_odd_length():
    assert sort_even([3, 2, 1, 4, 5]) == [1, 2, 3, 4, 5]

def test_sort_even_negative():
    assert sort_even([-3, 2, -1, 4]) == [-3, 2, -1, 4]

def test_sort_even_empty():
    assert sort_even([]) == []

def test_sort_even_single():
    assert sort_even([1]) == [1]

@pytest.mark.parametrize("input_list,expected", [
    ([4, 2, 3, 1], [3, 2, 4, 1]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([10, 1, 5, 2, 3, 4], [3, 1, 5, 2, 10, 4]),
    ([100, 2, 50, 4, 25, 6], [25, 2, 50, 4, 100, 6])
])
def test_sort_even_parametrized(input_list, expected):
    assert sort_even(input_list) == expected

def test_sort_even_duplicates():
    assert sort_even([2, 1, 2, 3, 2, 5]) == [2, 1, 2, 3, 2, 5]

def test_sort_even_zeros():
    assert sort_even([0, 1, 0, 2, 0, 3]) == [0, 1, 0, 2, 0, 3]

def test_sort_even_all_same():
    assert sort_even([7, 7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7, 7]

def test_sort_even_large_numbers():
    assert sort_even([1000, 1, 100, 2, 10, 3]) == [10, 1, 100, 2, 1000, 3]

@pytest.mark.parametrize("input_list", [
    None,
    "string",
    123,
    3.14
])
def test_sort_even_invalid_input(input_list):
    with pytest.raises((TypeError, AttributeError)):
        sort_even(input_list)
