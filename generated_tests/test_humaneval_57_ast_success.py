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

def test_empty_list():
    assert monotonic([]) == True

def test_single_element():
    assert monotonic([1]) == True

def test_two_elements_increasing():
    assert monotonic([1, 2]) == True

def test_two_elements_decreasing():
    assert monotonic([2, 1]) == True

def test_two_elements_equal():
    assert monotonic([1, 1]) == True

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], True),
    ([1, 1, 2, 2, 3], True),
    ([3, 2, 1, 1, 1], True),
    ([1, 3, 2, 4], False),
    ([4, 2, 3, 1], False),
    ([1, 2, 2, 1], False),
])
def test_various_sequences(input_list, expected):
    assert monotonic(input_list) == expected

@pytest.mark.parametrize("input_list,expected", [
    ([0, 0, 0, 0], True),
    ([-1, -1, -1], True),
    ([-3, -2, -1, 0], True),
    ([0, -1, -2, -3], True),
    ([-1, -3, -2, -4], False),
])
def test_with_negative_and_zero(input_list, expected):
    assert monotonic(input_list) == expected

@pytest.mark.parametrize("input_list,expected", [
    ([1.1, 2.2, 3.3], True),
    ([3.3, 2.2, 1.1], True),
    ([1.1, 3.3, 2.2], False),
])
def test_with_floats(input_list, expected):
    assert monotonic(input_list) == expected

def test_with_strings():
    assert monotonic(['a', 'b', 'c']) == True
    assert monotonic(['c', 'b', 'a']) == True
    assert monotonic(['a', 'c', 'b']) == False

def test_mixed_types():
    with pytest.raises(TypeError):
        monotonic([1, 'a', 2.5])

def test_large_list():
    assert monotonic(list(range(1000))) == True
    assert monotonic(list(range(999, -1, -1))) == True
