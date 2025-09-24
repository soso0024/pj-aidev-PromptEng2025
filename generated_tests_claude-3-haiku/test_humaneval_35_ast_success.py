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
    with pytest.raises(IndexError):
        max_element([])

def test_max_element_single_element():
    assert max_element([42]) == 42

def test_max_element_multiple_elements():
    assert max_element([1, 5, 3, 9, 2]) == 9

def test_max_element_negative_numbers():
    assert max_element([-5, -10, -3, -1]) == -1

def test_max_element_duplicate_elements():
    assert max_element([4, 7, 4, 9, 4]) == 9

def test_max_element_mixed_types():
    with pytest.raises(TypeError):
        max_element([1, 'a', 3.14])

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3, 4, 5], 5),
    ([-10, -5, 0, 5, 10], 10),
    ([0, 0, 0, 0, 0], 0),
    ([42], 42),
    ([], IndexError)
])
def test_max_element_parametrized(input, expected):
    if expected == IndexError:
        with pytest.raises(IndexError):
            max_element(input)
    else:
        assert max_element(input) == expected

def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m
