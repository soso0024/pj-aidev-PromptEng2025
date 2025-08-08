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

def test_unique_single_element_list():
    assert unique([5]) == [5]

def test_unique_multiple_elements_list():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_unique_duplicate_elements_list():
    assert unique([1, 1, 1, 2, 2, 3]) == [1, 2, 3]

def test_unique_sorted_list():
    assert unique([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]

def test_unique_unsorted_list():
    assert unique([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

@pytest.mark.parametrize("input,expected", [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [0, 2, 3, 5, 9, 123]),
    ([1, 1, 1, 2, 2, 3], [1, 2, 3]),
    ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
    ([5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
    ([], [])
])
def test_unique_parametrized(input, expected):
    assert unique(input) == expected

def test_unique_with_non_list_input():
    with pytest.raises(TypeError):
        unique(5)
