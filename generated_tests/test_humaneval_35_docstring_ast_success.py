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

def test_basic_list():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

@pytest.mark.parametrize("input_list,expected", [
    ([1], 1),
    ([1, 1, 1], 1),
    ([0, 0, 0], 0),
    ([-1, -2, -3], -1),
    ([999999, 1000000, 999998], 1000000),
    ([1.5, 2.5, 1.1], 2.5),
    ([-0.5, -0.1, -0.9], -0.1),
])
def test_max_element_parametrized(input_list, expected):
    assert max_element(input_list) == expected

def test_single_element():
    assert max_element([42]) == 42

def test_negative_numbers():
    assert max_element([-5, -4, -3, -2, -1]) == -1

def test_mixed_numbers():
    assert max_element([-10, 0, 10]) == 10

def test_float_numbers():
    assert max_element([1.1, 2.2, 3.3]) == 3.3

def test_duplicate_max():
    assert max_element([1, 3, 3, 2]) == 3

@pytest.mark.xfail(raises=IndexError)
def test_empty_list():
    max_element([])

@pytest.mark.xfail(raises=TypeError)
def test_invalid_types():
    max_element(['a', 'b', 'c'])

@pytest.mark.xfail(raises=TypeError)
def test_none_in_list():
    max_element([1, None, 2])

def test_large_numbers():
    assert max_element([10**9, 10**8, 10**7]) == 10**9

def test_very_large_list():
    large_list = list(range(10000))
    assert max_element(large_list) == 9999
