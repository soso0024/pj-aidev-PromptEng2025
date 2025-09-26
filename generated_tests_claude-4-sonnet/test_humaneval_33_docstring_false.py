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

def sort_third(l: list):
    l = list(l)
    l[::3] = sorted(l[::3])
    return l

def test_sort_third_example_1():
    assert sort_third([1, 2, 3]) == [1, 2, 3]

def test_sort_third_example_2():
    assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

def test_sort_third_empty_list():
    assert sort_third([]) == []

def test_sort_third_single_element():
    assert sort_third([42]) == [42]

def test_sort_third_two_elements():
    assert sort_third([5, 10]) == [5, 10]

def test_sort_third_three_elements():
    assert sort_third([9, 2, 1]) == [1, 2, 9]

def test_sort_third_all_same_values():
    assert sort_third([5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5]

def test_sort_third_negative_numbers():
    assert sort_third([-3, 1, -1, 2, -5, 4, 0]) == [-5, 1, -1, 2, -3, 4, 0]

def test_sort_third_mixed_positive_negative():
    assert sort_third([10, -2, 5, 3, -1, 8, 0]) == [0, -2, 5, 3, -1, 8, 10]

def test_sort_third_duplicates_at_divisible_indices():
    assert sort_third([3, 1, 3, 2, 3, 4, 3]) == [3, 1, 3, 2, 3, 4, 3]

def test_sort_third_large_numbers():
    assert sort_third([1000, 500, 2000, 100, 3000, 200]) == [100, 500, 2000, 1000, 3000, 200]

def test_sort_third_reverse_sorted():
    assert sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 7, 6, 5, 4, 9, 2, 1]

def test_sort_third_already_sorted():
    assert sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_sort_third_floats():
    assert sort_third([3.5, 1.2, 2.8, 4.1, 1.5, 3.9]) == [1.5, 1.2, 2.8, 4.1, 3.5, 3.9]

def test_sort_third_strings():
    assert sort_third(['z', 'b', 'y', 'c', 'x', 'd']) == ['x', 'b', 'y', 'c', 'z', 'd']

def test_sort_third_original_list_unchanged():
    original = [5, 6, 3, 4, 8, 9, 2]
    result = sort_third(original)
    assert original == [5, 6, 3, 4, 8, 9, 2]
    assert result == [2, 6, 3, 4, 8, 9, 5]

@pytest.mark.parametrize("input_list,expected", [
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([6, 5, 4, 3, 2, 1], [3, 5, 4, 6, 2, 1]),
    ([0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1]),
    ([-1, -2, -3], [-3, -2, -1])
])
def test_sort_third_parametrized(input_list, expected):
    assert sort_third(input_list) == expected