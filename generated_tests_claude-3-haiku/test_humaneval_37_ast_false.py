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
    assert sort_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6, 1, 3, 5]
    assert sort_even([1, 2, 3, 4, 5]) == [2, 4, 1, 3, 5]
    assert sort_even([2, 4, 6, 8]) == [2, 4, 6, 8]

def test_sort_even_empty_list():
    assert sort_even([]) == []

def test_sort_even_single_element():
    assert sort_even([1]) == [1]

def test_sort_even_all_odd():
    assert sort_even([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_sort_even_all_even():
    assert sort_even([2, 4, 6, 8]) == [2, 4, 6, 8]

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5, 6, 7], [2, 4, 6, 1, 3, 5, 7]),
    ([2, 4, 6, 8, 10], [2, 4, 6, 8, 10]),
    ([1, 3, 5, 7, 9, 11], [1, 3, 5, 7, 9, 11]),
    ([1, 2, 3, 4, 5, 6], [2, 4, 6, 1, 3, 5]),
    ([1, 2, 3, 4, 5], [2, 4, 1, 3, 5]),
    ([], []),
    ([1], [1])
])
def test_sort_even_parametrized(input, expected):
    assert sort_even(input) == expected

def test_sort_even_type_error():
    with pytest.raises(TypeError):
        sort_even(1)