# Test cases for HumanEval/42
# Generated using Claude API



def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """

    return [(e + 1) for e in l]


# Generated test cases:
import pytest

def test_incr_list_empty():
    assert incr_list([]) == []

def test_incr_list_single_element():
    assert incr_list([5]) == [6]

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], [2, 3, 4]),
    ([-10, 0, 10], [-9, 1, 11]),
    ([0.5, 1.2, 2.7], [1.5, 2.2, 3.7])
])
def test_incr_list_multiple_elements(input, expected):
    assert incr_list(input) == expected

def test_incr_list_none_input():
    with pytest.raises(TypeError):
        incr_list(None)

def test_incr_list_string_input():
    with pytest.raises(TypeError):
        incr_list("test")

def test_incr_list_mixed_types():
    with pytest.raises(TypeError):
        incr_list([1, 2.3, "four"])

def incr_list(l: list):
    return [(e + 1) for e in l]
