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

def test_max_element_positive_numbers():
    assert max_element([1, 2, 3]) == 3

def test_max_element_negative_numbers():
    assert max_element([-5, -3, -1]) == -1

def test_max_element_mixed_numbers():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

def test_max_element_duplicate_max():
    assert max_element([1, 2, 2, 3]) == 3

def test_max_element_type_error():
    with pytest.raises(TypeError):
        max_element(42)

def max_element(l: list):
    if not l:
        return None
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m
