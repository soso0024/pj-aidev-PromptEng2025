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
import pytest

def test_sort_third_empty_list():
    assert sort_third([]) == []

def test_sort_third_single_element():
    assert sort_third([1]) == [1]

def test_sort_third_even_length():
    assert sort_third([1, 2, 3, 4, 5, 6]) == [1, 2, 4, 3, 5, 6]

def test_sort_third_odd_length():
    assert sort_third([1, 2, 3, 4, 5]) == [1, 2, 4, 3, 5]

@pytest.mark.parametrize("input,expected", [
    ([10, 20, 30, 40, 50, 60], [10, 20, 40, 30, 50, 60]),
    ([100, 200, 300, 400, 500, 600, 700], [100, 200, 400, 300, 500, 600, 700]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 4, 3, 5, 6, 7, 8, 9]),
    ([1.1, 2.2, 3.3, 4.4, 5.5, 6.6], [1.1, 2.2, 4.4, 3.3, 5.5, 6.6]),
    (['a', 'b', 'c', 'd', 'e', 'f'], ['a', 'b', 'd', 'c', 'e', 'f'])
])
def test_sort_third_parametrized(input, expected):
    assert sort_third(input) == expected