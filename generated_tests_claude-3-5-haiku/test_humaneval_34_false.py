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
    assert unique([3, 1, 2, 3, 4, 2]) == [1, 2, 3, 4]

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([5]) == [5]

def test_unique_all_duplicates():
    assert unique([1, 1, 1, 1]) == [1]

def test_unique_mixed_types():
    assert unique([1, 'a', 2, 'a', 3]) == [1, 2, 3, 'a']

def test_unique_negative_numbers():
    assert unique([-1, -2, -1, 0, -2, 3]) == [-2, -1, 0, 3]

def test_unique_floating_point():
    assert unique([1.1, 2.2, 1.1, 3.3]) == [1.1, 2.2, 3.3]

def test_unique_none_values():
    assert unique([None, None, 1, 2, None]) == [None, 1, 2]

@pytest.mark.parametrize("input_list,expected", [
    ([3, 1, 2, 3, 4, 2], [1, 2, 3, 4]),
    ([], []),
    ([5], [5]),
    ([1, 1, 1, 1], [1]),
    ([-1, -2, -1, 0, -2, 3], [-2, -1, 0, 3])
])
def test_unique_parametrized(input_list, expected):
    assert unique(input_list) == expected

def test_unique_input_type_error():
    with pytest.raises(TypeError):
        unique(123)

def test_unique_nested_list():
    assert unique([[1, 2], [1, 2], [3, 4]]) == [[1, 2], [3, 4]]