# Test cases for HumanEval/35
# Generated using Claude API



def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m


# Generated test cases:
import pytest

def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

def test_max_element_single_element():
    assert max_element([5]) == 5

def test_max_element_positive_integers():
    assert max_element([1, 3, 2, 5, 4]) == 5

def test_max_element_negative_integers():
    assert max_element([-1, -3, -2, -5, -4]) == -1

def test_max_element_mixed_integers():
    assert max_element([-1, 3, -2, 5, -4]) == 5

def test_max_element_duplicates():
    assert max_element([5, 5, 5, 5]) == 5

def test_max_element_max_at_beginning():
    assert max_element([10, 1, 2, 3]) == 10

def test_max_element_max_at_end():
    assert max_element([1, 2, 3, 10]) == 10

def test_max_element_floats():
    assert max_element([1.5, 2.7, 1.2, 3.8]) == 3.8

def test_max_element_mixed_numbers():
    assert max_element([1, 2.5, 3, 1.5]) == 3

def test_max_element_strings():
    assert max_element(['apple', 'zebra', 'banana']) == 'zebra'

def test_max_element_zero_included():
    assert max_element([0, -1, -2]) == 0

def test_max_element_all_zeros():
    assert max_element([0, 0, 0]) == 0

def test_max_element_large_numbers():
    assert max_element([1000000, 999999, 1000001]) == 1000001

def test_max_element_empty_list_raises_error():
    with pytest.raises(IndexError):
        max_element([])

def test_max_element_two_elements():
    assert max_element([1, 2]) == 2
    assert max_element([2, 1]) == 2

@pytest.mark.parametrize("input_list,expected", [
    ([1], 1),
    ([1, 2], 2),
    ([2, 1], 2),
    ([1, 2, 3], 3),
    ([-1, -2, -3], -1),
    ([0], 0),
    ([5, 5, 5], 5)
])
def test_max_element_parametrized(input_list, expected):
    assert max_element(input_list) == expected
