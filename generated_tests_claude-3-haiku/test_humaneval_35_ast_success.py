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

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], 4),
    ([4, 3, 2, 1], 4),
    ([1, 1, 1, 1], 1),
    ([-1, -2, -3, -4], -1),
    ([0, 0, 0, 0], 0),
    ([1], 1),
    ([1, 1], 1),
])
def test_max_element_valid_inputs(input_list, expected):
    assert max_element(input_list) == expected

def test_max_element_non_list_input():
    with pytest.raises(TypeError):
        max_element(123)

def test_max_element_list_with_non_numeric_elements():
    with pytest.raises(TypeError):
        max_element([1, 2, "3", 4])