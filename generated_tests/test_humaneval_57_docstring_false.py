# Test cases for HumanEval/57
# Generated using Claude API



def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


# Generated test cases:
import pytest

def test_monotonic_increasing():
    assert monotonic([1, 2, 3, 4]) == True

def test_monotonic_decreasing():
    assert monotonic([4, 3, 2, 1]) == True

def test_not_monotonic():
    assert monotonic([1, 3, 2, 4]) == False

def test_single_element():
    assert monotonic([1]) == True

def test_empty_list():
    assert monotonic([]) == True

def test_duplicate_elements():
    assert monotonic([1, 1, 1]) == True

def test_negative_numbers():
    assert monotonic([-3, -2, -1, 0]) == True

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4], True),
    ([4, 3, 2, 1], True),
    ([1, 3, 2, 4], False),
    ([1], True),
    ([], True),
    ([1, 1, 1], True),
    ([-3, -2, -1], True),
    ([1.5, 2.5, 3.5], True),
    ([3.5, 2.5, 1.5], True),
    ([1, 2, 2, 3], True),
    ([3, 2, 2, 1], True),
    ([1, 2, 1, 2], False)
])
def test_monotonic_parametrized(input_list, expected):
    assert monotonic(input_list) == expected

def test_large_numbers():
    assert monotonic([1000000, 2000000, 3000000]) == True

def test_mixed_types():
    with pytest.raises(TypeError):
        monotonic([1, "2", 3])

def test_none_in_list():
    with pytest.raises(TypeError):
        monotonic([1, None, 3])

def test_non_list_input():
    with pytest.raises(TypeError):
        monotonic("not a list")