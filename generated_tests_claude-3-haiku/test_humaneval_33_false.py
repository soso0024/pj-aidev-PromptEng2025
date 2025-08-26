# Test cases for HumanEval/33
# Generated using Claude API



def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l = list(l)
    l[::3] = sorted(l[::3])
    return l


# Generated test cases:
from sort_third import sort_third
import pytest

def test_sort_third_empty_list():
    assert sort_third([]) == []

def test_sort_third_single_element():
    assert sort_third([42]) == [42]

def test_sort_third_sorted_list():
    assert sort_third([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_sort_third_unsorted_list():
    assert sort_third([3, 1, 4, 2, 5, 6]) == [1, 2, 4, 3, 5, 6]

def test_sort_third_list_with_duplicates():
    assert sort_third([3, 1, 3, 2, 5, 6]) == [1, 2, 3, 3, 5, 6]

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 8, 3, 6, 5, 4, 7, 2, 9]),
    ([42], [42]),
    ([], []),
    ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
    ([7, 6, 5, 4, 3, 2, 1], [1, 6, 3, 4, 5, 2, 7]),
])
def test_sort_third_parametrized(input, expected):
    assert sort_third(input) == expected

def test_sort_third_non_list_input():
    with pytest.raises(TypeError):
        sort_third(42)