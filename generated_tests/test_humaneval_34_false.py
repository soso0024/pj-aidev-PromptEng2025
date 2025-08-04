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
    assert unique([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element():
    assert unique([1]) == [1]

def test_unique_negative_numbers():
    assert unique([-1, -1, 2, -3, 2, -3]) == [-3, -1, 2]

def test_unique_mixed_types():
    with pytest.raises(TypeError):
        unique([1, "2", 3.0, True])

def test_unique_strings():
    assert unique(["apple", "banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 1, 1, 1], [1]),
    ([3, 2, 1], [1, 2, 3]),
    ([0, 0, 0, 1, 1, 2], [0, 1, 2]),
    (["a", "a", "b", "c", "b"], ["a", "b", "c"]),
    ([True, False, True, True], [False, True])
])
def test_unique_parametrized(input_list, expected):
    assert unique(input_list) == expected

def test_unique_none_element():
    with pytest.raises(TypeError):
        unique([1, None, 2])

def test_unique_large_numbers():
    assert unique([1000000, 999999, 1000000]) == [999999, 1000000]

def test_unique_floating_numbers():
    assert unique([1.1, 1.1, 2.2, 3.3, 2.2]) == [1.1, 2.2, 3.3]

def test_unique_not_list():
    with pytest.raises(TypeError):
        unique("not a list")

def test_unique_nested_lists():
    with pytest.raises(TypeError):
        unique([[1, 2], [3, 4], [1, 2]])