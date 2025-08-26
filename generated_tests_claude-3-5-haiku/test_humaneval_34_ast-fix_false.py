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
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([42]) == [42]

def test_unique_all_duplicates():
    assert unique([1, 1, 1, 1]) == [1]

def test_unique_mixed_types():
    assert unique([1, '1', 2, '2']) == [1, '1', 2, '2']

def test_unique_unhashable_types():
    assert unique([[1], [1], [2], [3]]) == [[1], [2], [3]]

def test_unique_raises_type_error():
    with pytest.raises(TypeError):
        unique("not a list")

def test_unique_nested_lists():
    assert unique([[1, 2], [1, 2], [3, 4]]) == [[1, 2], [3, 4]]