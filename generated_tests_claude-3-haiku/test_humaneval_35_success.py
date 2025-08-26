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

def test_max_element_empty_list():
    assert max_element([]) is None

def test_max_element_single_element():
    assert max_element([42]) == 42

def test_max_element_multiple_elements():
    assert max_element([1, 5, 3, 9, 2]) == 9

def test_max_element_negative_numbers():
    assert max_element([-5, -10, -3, -1]) == -1

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 5),
    ([0, 0, 0, 0], 0),
    ([-1, -2, -3, -4, -5], -1),
    ([42], 42),
    ([], None)
])
def test_max_element_parametrized(input_list, expected):
    assert max_element(input_list) == expected

def max_element(l: list):
    if not l:
        return None
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m
