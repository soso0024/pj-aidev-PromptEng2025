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
    assert monotonic([1, 2, 4, 20]) == True
    assert monotonic([1, 2, 2, 20]) == True

def test_monotonic_decreasing():
    assert monotonic([4, 1, 0, -10]) == True
    assert monotonic([4, 2, 2, -10]) == True

def test_not_monotonic():
    assert monotonic([1, 20, 4, 10]) == False
    assert monotonic([1, 2, 20, 4]) == False
    assert monotonic([4, 2, 1, -10]) == True

def test_empty_list():
    assert monotonic([]) == True

def test_single_element_list():
    assert monotonic([42]) == True

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 4, 20], True),
    ([1, 20, 4, 10], False),
    ([4, 1, 0, -10], True),
    ([], True),
    ([42], True)
])
def test_monotonic_parametrized(input, expected):
    assert monotonic(input) == expected

def test_monotonic_type_error():
    with pytest.raises(TypeError):
        monotonic(42)