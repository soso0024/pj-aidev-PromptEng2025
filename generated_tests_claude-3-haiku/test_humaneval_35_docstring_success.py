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
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        return None
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

def test_max_element_empty_list():
    assert max_element([]) is None

def test_max_element_single_element():
    assert max_element([5]) == 5

def test_max_element_positive_numbers():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, 2, 9, 0, 123, 1]) == 123

def test_max_element_negative_numbers():
    assert max_element([-5, -3, -10]) == -3

def test_max_element_mixed_numbers():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

def test_max_element_duplicate_numbers():
    assert max_element([1, 2, 2, 3, 3, 3]) == 3

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], 3),
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 123),
    ([-5, -3, -10], -3),
    ([1, 1, 1, 1], 1),
    ([], None)
])
def test_max_element_parametrized(input, expected):
    assert max_element(input) == expected