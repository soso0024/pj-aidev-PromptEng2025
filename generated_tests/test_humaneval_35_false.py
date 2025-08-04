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
    assert max_element([1, 2, 3, 4, 5]) == 5
    assert max_element([5, 4, 3, 2, 1]) == 5
    assert max_element([1, 5, 2, 4, 3]) == 5

def test_max_element_negative():
    assert max_element([-1, -2, -3, -4, -5]) == -1
    assert max_element([-5, -4, -3, -2, -1]) == -1

def test_max_element_mixed():
    assert max_element([-1, 0, 1]) == 1
    assert max_element([-10, 5, 0, 100, -50]) == 100

def test_max_element_duplicates():
    assert max_element([1, 1, 1, 1]) == 1
    assert max_element([1, 2, 2, 1, 2]) == 2

def test_max_element_single():
    assert max_element([42]) == 42
    assert max_element([-42]) == -42

def test_max_element_floats():
    assert max_element([1.5, 2.5, 0.5]) == 2.5
    assert max_element([-1.5, -2.5, -0.5]) == -0.5

@pytest.mark.parametrize("test_input", [
    [],
    None,
    42
])
def test_max_element_invalid_input(test_input):
    with pytest.raises(Exception):
        max_element(test_input)

def test_max_element_string_input():
    with pytest.raises(TypeError):
        max_element(["string"])

def test_max_element_large_numbers():
    assert max_element([1000000, 999999, 1000001]) == 1000001
    assert max_element([-1000000, -999999, -1000001]) == -999999

def test_max_element_zero():
    assert max_element([0, 0, 0]) == 0
    assert max_element([-1, 0, 1]) == 1

@pytest.mark.parametrize("test_input,expected", [
    ([1, 2, 3], 3),
    ([3, 2, 1], 3),
    ([1.5, 2.7, 2.1], 2.7),
    ([-1, -2, -3], -1),
    ([0, 0, 0], 0)
])
def test_max_element_parametrized(test_input, expected):
    assert max_element(test_input) == expected