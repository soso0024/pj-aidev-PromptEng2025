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
    assert unique([5]) == [5]

def test_unique_multiple_elements():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_unique_duplicate_elements():
    assert unique([1, 1, 1, 2, 2, 3]) == [1, 2, 3]

def test_unique_mixed_types():
    assert sorted(unique([1, 'a', 2.0, 'b', 1])) == [1, 2.0, 'a', 'b']

@pytest.mark.parametrize("input,expected", [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [0, 2, 3, 5, 9, 123]),
    ([1, 1, 1, 2, 2, 3], [1, 2, 3]),
    ([1, 'a', 2.0, 'b', 1], [1, 2.0, 'a', 'b']),
    ([], [])
])
def test_unique_parametrized(input, expected):
    assert sorted(unique(input)) == sorted(expected)