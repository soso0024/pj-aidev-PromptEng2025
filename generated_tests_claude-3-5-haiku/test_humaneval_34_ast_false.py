# Test cases for HumanEval/34
# Generated using Claude API



def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    return sorted(list(set(l)))


# Generated test cases:
import pytest

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))

def test_unique_basic_list():
    assert unique([3, 1, 2, 1, 3]) == [1, 2, 3]

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([5]) == [5]

def test_unique_all_same_elements():
    assert unique([2, 2, 2, 2]) == [2]

def test_unique_mixed_types():
    assert unique([1, 'a', 2, 'a', 1]) == [1, 2, 'a']

def test_unique_float_values():
    assert unique([1.1, 2.2, 1.1, 3.3]) == [1.1, 2.2, 3.3]

def test_unique_negative_numbers():
    assert unique([-1, -2, -1, 0, -2]) == [-2, -1, 0]

def test_unique_complex_list():
    assert unique([5, 'hello', 3.14, 5, 'hello', 3.14]) == [3.14, 5, 'hello']

def test_unique_none_values():
    assert unique([None, None, 1, None]) == [None, 1]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([], []),
    ([0, 0, 0], [0]),
    (['a', 'b', 'a', 'c'], ['a', 'b', 'c'])
])
def test_unique_parametrized(input_list, expected):
    assert unique(input_list) == expected

def test_unique_large_list():
    large_list = list(range(1000)) + list(range(1000))
    assert unique(large_list) == list(range(1000))

def test_unique_nested_lists():
    assert unique([[1, 2], [3, 4], [1, 2]]) == [[1, 2], [3, 4]]