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

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([5, 6, 3, 4], [3, 6, 5, 4]),
    ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 8, 3, 6, 5, 4, 7, 2, 9]),
    ([1], [1]),
    ([2, 1], [2, 1]),
    ([3, 1, 2], [2, 1, 3]),
    ([10, 9, 8, 7, 6, 5], [6, 9, 8, 7, 10, 5]),
    ([], []),
    ([0], [0]),
    ([0, 1], [0, 1]),
    ([-1, -2, -3, -4], [-3, -2, -1, -4]),
    ([-5, 10, -3, 8, -1], [-5, 10, -3, 8, -1]),
    ([100, 50, 25, 75], [25, 50, 100, 75]),
])
def test_sort_even_parametrized(input_list, expected):
    assert sort_even(input_list) == expected

def test_sort_even_empty_list():
    assert sort_even([]) == []

def test_sort_even_single_element():
    assert sort_even([42]) == [42]

def test_sort_even_two_elements():
    assert sort_even([5, 3]) == [5, 3]

def test_sort_even_all_same_values():
    assert sort_even([5, 5, 5, 5]) == [5, 5, 5, 5]

def test_sort_even_negative_numbers():
    assert sort_even([-10, -5, -20, -15]) == [-20, -5, -10, -15]

def test_sort_even_mixed_positive_negative():
    assert sort_even([-1, 2, -3, 4, -5]) == [-5, 2, -3, 4, -1]

def test_sort_even_already_sorted():
    assert sort_even([1, 10, 2, 20, 3, 30]) == [1, 10, 2, 20, 3, 30]

def test_sort_even_reverse_sorted():
    assert sort_even([9, 10, 7, 20, 5, 30]) == [5, 10, 7, 20, 9, 30]

def test_sort_even_odd_length_list():
    assert sort_even([8, 1, 6, 2, 4]) == [4, 1, 6, 2, 8]

def test_sort_even_large_numbers():
    assert sort_even([1000, 999, 500, 888, 250]) == [250, 999, 500, 888, 1000]

def test_sort_even_zeros_and_positives():
    assert sort_even([0, 1, 0, 2, 0]) == [0, 1, 0, 2, 0]

def test_sort_even_duplicates_in_even_positions():
    assert sort_even([5, 1, 5, 2, 3, 4]) == [3, 1, 5, 2, 5, 4]