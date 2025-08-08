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

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([1]) == [1]

def test_unique_no_duplicates():
    assert unique([1, 2, 3]) == [1, 2, 3]

def test_unique_with_duplicates():
    assert unique([1, 2, 2, 3, 3, 3]) == [1, 2, 3]

def test_unique_all_duplicates():
    assert unique([1, 1, 1, 1]) == [1]

def test_unique_different_types():
    with pytest.raises(TypeError):
        unique([1, "1", True, 1.0])

def test_unique_negative_numbers():
    assert unique([-1, -2, -1, 0, 2, -2]) == [-2, -1, 0, 2]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 1, 1], [1]),
    ([], []),
    ([0], [0]),
    ([1.5, 1.0, 1.5, 2.5], [1.0, 1.5, 2.5])
])
def test_unique_parametrized(input_list, expected):
    assert unique(input_list) == expected

def test_unique_with_none():
    with pytest.raises(TypeError):
        unique([None, None, 1, 2, None])

def test_unique_mixed_types():
    with pytest.raises(TypeError):
        unique([1, "a", 1, "b", "a"])

@pytest.mark.xfail(raises=TypeError)
def test_unique_unhashable_types():
    unique([[1, 2], [3, 4]])