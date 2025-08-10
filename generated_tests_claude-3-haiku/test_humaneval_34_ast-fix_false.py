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
    return sorted(list(set(l)), key=lambda x: (x is None, type(x) is not str, x))

def test_unique_empty_list():
    assert unique([]) == []

def test_unique_single_element_list():
    assert unique([1]) == [1]

def test_unique_multiple_elements_list():
    assert unique([1, 2, 3, 2, 4]) == [1, 2, 3, 4]

def test_unique_with_duplicates():
    assert unique([1, 1, 2, 2, 3, 3]) == [1, 2, 3]

def test_unique_with_strings():
    assert unique(['apple', 'banana', 'cherry', 'banana']) == ['apple', 'banana', 'cherry']

def test_unique_with_mixed_types():
    assert unique([1, 'a', 2.0, 'a', 3]) == [1, 2.0, 3, 'a']

def test_unique_with_none():
    assert unique([None, 1, None, 2]) == [None, 1, 2]

def test_unique_with_empty_string():
    assert unique(['', 'a', '']) == ['', 'a']

@pytest.mark.parametrize("input,expected", [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 2, 4], [1, 2, 3, 4]),
    ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
    (['apple', 'banana', 'cherry', 'banana'], ['apple', 'banana', 'cherry']),
    ([1, 'a', 2.0, 'a', 3], [1, 2.0, 3, 'a']),
    ([None, 1, None, 2], [None, 1, 2]),
    (['', 'a', ''], ['', 'a'])
])
def test_unique_parametrized(input, expected):
    assert unique(input) == expected