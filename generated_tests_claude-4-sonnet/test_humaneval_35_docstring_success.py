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

def test_max_element_positive_numbers():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, 2, 9, 1]) == 9

def test_max_element_negative_numbers():
    assert max_element([-1, -2, -3]) == -1
    assert max_element([-10, -5, -20, -1]) == -1

def test_max_element_mixed_numbers():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    assert max_element([-5, 10, -3, 7]) == 10

def test_max_element_duplicates():
    assert max_element([5, 5, 5]) == 5
    assert max_element([1, 3, 3, 2]) == 3

def test_max_element_zero():
    assert max_element([0]) == 0
    assert max_element([0, 0, 0]) == 0
    assert max_element([-1, 0, -2]) == 0

def test_max_element_floats():
    assert max_element([1.5, 2.7, 1.2]) == 2.7
    assert max_element([-1.5, -2.7, -1.2]) == -1.2

def test_max_element_large_numbers():
    assert max_element([1000000, 999999, 1000001]) == 1000001

def test_max_element_two_elements():
    assert max_element([1, 2]) == 2
    assert max_element([2, 1]) == 2

def test_max_element_empty_list():
    with pytest.raises(IndexError):
        max_element([])

def test_max_element_strings():
    assert max_element(['a', 'b', 'c']) == 'c'
    assert max_element(['z', 'a', 'm']) == 'z'

@pytest.mark.parametrize("input_list,expected", [
    ([1], 1),
    ([1, 2], 2),
    ([2, 1], 2),
    ([1, 2, 3], 3),
    ([-1, -2, -3], -1),
    ([0, -1, 1], 1),
    ([100, 50, 75], 100)
])
def test_max_element_parametrized(input_list, expected):
    assert max_element(input_list) == expected
