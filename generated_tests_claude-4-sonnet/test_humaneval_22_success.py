# Test cases for HumanEval/22
# Generated using Claude API

from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """

    return [x for x in values if isinstance(x, int)]


# Generated test cases:
import pytest
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if isinstance(x, int)]

def test_empty_list():
    assert filter_integers([]) == []

def test_only_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_no_integers():
    assert filter_integers(['a', 'b', 'c']) == []

def test_mixed_types():
    assert filter_integers([1, 'a', 2, 'b', 3]) == [1, 2, 3]

def test_negative_integers():
    assert filter_integers([-1, -2, -3]) == [-1, -2, -3]

def test_zero():
    assert filter_integers([0, 1, 2]) == [0, 1, 2]

def test_floats_excluded():
    assert filter_integers([1.5, 2.7, 3]) == [3]

def test_boolean_excluded():
    assert filter_integers([True, False, 1, 2]) == [True, False, 1, 2]

def test_none_excluded():
    assert filter_integers([None, 1, 2, None]) == [1, 2]

def test_strings_excluded():
    assert filter_integers(['1', '2', 1, 2]) == [1, 2]

def test_complex_types_excluded():
    assert filter_integers([[1, 2], {'a': 1}, (1, 2), 3]) == [3]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
    ([1.5, 2.5], []),
    (['a', 'b'], []),
    ([1, 'a', 2.5, 3], [1, 3]),
    ([0], [0]),
    ([-5, -10, 15], [-5, -10, 15]),
    ([True, False, 1], [True, False, 1]),
    ([None, 1, None, 2], [1, 2])
])
def test_parametrized_cases(input_list, expected):
    assert filter_integers(input_list) == expected

def test_large_integers():
    large_int = 999999999999999999
    assert filter_integers([large_int, 'test']) == [large_int]

def test_mixed_numeric_types():
    assert filter_integers([1, 1.0, 1j, 2]) == [1, 2]

def test_nested_structures():
    assert filter_integers([1, [2, 3], {4: 5}, (6, 7), 8]) == [1, 8]