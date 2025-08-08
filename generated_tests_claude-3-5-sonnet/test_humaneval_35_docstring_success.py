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

def test_max_element_basic():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

@pytest.mark.parametrize("input_list,expected", [
    ([1], 1),
    ([1, 1, 1], 1),
    ([-1, -2, -3], -1),
    ([0, 0, 0], 0),
    ([999999, 1, 2], 999999),
    ([-999999, -1, -2], -1),
    ([1.5, 2.5, 3.5], 3.5),
    ([float('-inf'), 0, float('inf')], float('inf')),
])
def test_max_element_parametrized(input_list, expected):
    assert max_element(input_list) == expected

def test_max_element_identical_values():
    assert max_element([42, 42, 42]) == 42

def test_max_element_single_element():
    assert max_element([5]) == 5

@pytest.mark.parametrize("invalid_input", [
    [],
    None,
])
def test_max_element_invalid_input(invalid_input):
    with pytest.raises(Exception):
        max_element(invalid_input)

def test_max_element_large_numbers():
    assert max_element([10**9, 10**8, 10**7]) == 10**9

def test_max_element_mixed_types():
    with pytest.raises(TypeError):
        max_element([1, "2", 3])

def test_max_element_nested_lists():
    with pytest.raises(TypeError):
        max_element([1, [2, 3], 4])
