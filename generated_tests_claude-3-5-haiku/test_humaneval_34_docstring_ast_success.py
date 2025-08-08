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

def test_unique_normal_case():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([42]) == [42]

def test_unique_all_duplicates():
    assert unique([1, 1, 1, 1]) == [1]

def test_unique_already_sorted():
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_unique_negative_numbers():
    assert unique([-3, -1, -3, 0, 2, -1]) == [-3, -1, 0, 2]

def test_unique_mixed_types():
    with pytest.raises(TypeError):
        unique([1, 'a', 2, 'b'])

@pytest.mark.parametrize("input_list,expected", [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [0, 2, 3, 5, 9, 123]),
    ([], []),
    ([42], [42]),
    ([1, 1, 1, 1], [1]),
    ([-3, -1, -3, 0, 2, -1], [-3, -1, 0, 2])
])
def test_unique_parametrized(input_list, expected):
    assert unique(input_list) == expected
