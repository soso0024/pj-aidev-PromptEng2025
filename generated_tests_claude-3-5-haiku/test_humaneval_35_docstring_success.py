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

def test_max_element_normal_cases():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

def test_max_element_single_element():
    assert max_element([42]) == 42

def test_max_element_negative_numbers():
    assert max_element([-1, -2, -3, -4]) == -1

def test_max_element_mixed_numbers():
    assert max_element([-10, 0, 5, -5, 3]) == 5

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], 3),
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 123),
    ([-1, -2, -3, -4], -1),
    ([42], 42)
])
def test_max_element_parametrized(input_list, expected):
    assert max_element(input_list) == expected

def test_max_element_empty_list():
    with pytest.raises(IndexError):
        max_element([])
