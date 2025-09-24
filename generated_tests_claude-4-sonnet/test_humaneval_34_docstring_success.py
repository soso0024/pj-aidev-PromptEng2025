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
    return sorted(list(set(l)))

def test_unique_basic():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([42]) == [42]

def test_unique_no_duplicates():
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_unique_all_duplicates():
    assert unique([7, 7, 7, 7]) == [7]

def test_unique_negative_numbers():
    assert unique([-3, -1, -3, -2, -1]) == [-3, -2, -1]

def test_unique_mixed_positive_negative():
    assert unique([-1, 0, 1, -1, 0, 1]) == [-1, 0, 1]

def test_unique_floats():
    assert unique([3.14, 2.71, 3.14, 1.41]) == [1.41, 2.71, 3.14]

def test_unique_strings():
    assert unique(['apple', 'banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']

def test_unique_mixed_types():
    with pytest.raises(TypeError):
        unique([1, '1', 1, 2, '2'])

def test_unique_large_list():
    input_list = list(range(100)) * 3
    expected = list(range(100))
    assert unique(input_list) == expected

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 2, 1], [1, 2, 3]),
    ([10, 20, 10], [10, 20]),
    ([0], [0]),
    ([5, 5, 5], [5])
])
def test_unique_parametrized(input_list, expected):
    assert unique(input_list) == expected

def test_unique_preserves_original_list():
    original = [3, 1, 3, 2]
    original_copy = original.copy()
    unique(original)
    assert original == original_copy

def test_unique_boolean_values():
    assert unique([True, False, True, False]) == [False, True]

def test_unique_none_values():
    with pytest.raises(TypeError):
        unique([None, 1, None, 2])