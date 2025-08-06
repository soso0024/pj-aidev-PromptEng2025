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

def test_unique_basic():
    assert unique([1, 2, 2, 3, 3, 3]) == [1, 2, 3]

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([1]) == [1]

def test_unique_negative_numbers():
    assert unique([-3, -2, -1, -2, -3]) == [-3, -2, -1]

def test_unique_mixed_numbers():
    assert unique([-1, 0, 1, -1, 0, 1]) == [-1, 0, 1]

@pytest.mark.parametrize("input_list,expected", [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [0, 2, 3, 5, 9, 123]),
    ([1.1, 2.2, 1.1, 3.3], [1.1, 2.2, 3.3]),
    ([0, 0, 0, 0], [0]),
    ([-1, -1, 1, 1], [-1, 1]),
    ([10**9, -(10**9), 0], [-(10**9), 0, 10**9])
])
def test_unique_parametrized(input_list, expected):
    assert unique(input_list) == expected

def test_unique_with_strings():
    result = unique(['a', 'b', 'a'])
    assert result == ['a', 'b']

def test_unique_with_mixed_types():
    with pytest.raises(TypeError):
        unique([1, 'a', 2, 'b'])

def test_unique_with_none():
    with pytest.raises(TypeError):
        unique([1, None, 2])

def test_unique_with_nested_lists():
    with pytest.raises(TypeError):
        unique([[1], [2], [1]])

def test_unique_with_large_numbers():
    assert unique([10**10, 10**10, 10**9]) == [10**9, 10**10]