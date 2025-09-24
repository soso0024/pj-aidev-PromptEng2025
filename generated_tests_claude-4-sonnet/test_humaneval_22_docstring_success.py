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

def test_filter_integers_mixed_types():
    assert filter_integers(['a', 3.14, 5]) == [5]

def test_filter_integers_multiple_integers():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]

def test_filter_integers_empty_list():
    assert filter_integers([]) == []

def test_filter_integers_no_integers():
    assert filter_integers(['a', 'b', 3.14, [], {}]) == []

def test_filter_integers_only_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_filter_integers_negative_integers():
    assert filter_integers([-1, -2, 'test', 3.5]) == [-1, -2]

def test_filter_integers_zero():
    assert filter_integers([0, 'zero', 0.0]) == [0]

def test_filter_integers_boolean_values():
    assert filter_integers([True, False, 1, 2]) == [True, False, 1, 2]

def test_filter_integers_none_values():
    assert filter_integers([None, 1, None, 2]) == [1, 2]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2.5, "3", 4], [1, 4]),
    ([10, 20, 30], [10, 20, 30]),
    (["hello", "world"], []),
    ([1.1, 2.2, 3.3], []),
    ([0, -5, 100], [0, -5, 100])
])
def test_filter_integers_parametrized(input_list, expected):
    assert filter_integers(input_list) == expected

def test_filter_integers_complex_types():
    assert filter_integers([1, [1, 2], {'key': 'value'}, (1, 2), set([1, 2])]) == [1]

def test_filter_integers_large_numbers():
    large_int = 999999999999999999
    assert filter_integers([large_int, 'text', 3.14]) == [large_int]

def test_filter_integers_nested_structures():
    assert filter_integers([1, [2, 3], {'num': 4}, 5]) == [1, 5]