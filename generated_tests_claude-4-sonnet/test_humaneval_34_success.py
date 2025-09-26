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

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([1]) == [1]

def test_unique_no_duplicates():
    assert unique([1, 2, 3]) == [1, 2, 3]

def test_unique_with_duplicates():
    assert unique([3, 1, 2, 1, 3]) == [1, 2, 3]

def test_unique_all_same_elements():
    assert unique([5, 5, 5, 5]) == [5]

def test_unique_strings():
    assert unique(['apple', 'banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']

def test_unique_mixed_types():
    with pytest.raises(TypeError):
        unique([1, '1', 2, '2', 1])

def test_unique_negative_numbers():
    assert unique([-1, -2, -1, 0, 1]) == [-2, -1, 0, 1]

def test_unique_floats():
    assert unique([1.5, 2.5, 1.5, 3.0]) == [1.5, 2.5, 3.0]

def test_unique_boolean_values():
    assert unique([True, False, True, False]) == [False, True]

def test_unique_none_values():
    with pytest.raises(TypeError):
        unique([None, 1, None, 2])

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 2, 1], [1, 2, 3]),
    (['z', 'a', 'z', 'b'], ['a', 'b', 'z']),
    ([0, 0, 0], [0]),
    ([1.1, 2.2, 1.1], [1.1, 2.2])
])
def test_unique_parametrized(input_list, expected):
    assert unique(input_list) == expected

def test_unique_large_list():
    large_list = list(range(1000)) * 3
    expected = list(range(1000))
    assert unique(large_list) == expected

def test_unique_with_tuples():
    assert unique([(1, 2), (3, 4), (1, 2)]) == [(1, 2), (3, 4)]

def test_unique_preserves_order_after_sorting():
    result = unique([3, 1, 4, 1, 5, 9, 2, 6, 5])
    assert result == [1, 2, 3, 4, 5, 6, 9]

def test_unique_type_error_with_non_list():
    result = unique("not a list")
    assert result == [' ', 'a', 'i', 'l', 'n', 'o', 's', 't']

def test_unique_type_error_with_none():
    with pytest.raises(TypeError):
        unique(None)