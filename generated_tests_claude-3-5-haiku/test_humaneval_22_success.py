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

def filter_integers(values: List[Any]):
    return [x for x in values if isinstance(x, int)]

def test_filter_integers_with_mixed_types():
    input_list = [1, 'a', 2, 3.14, 4, 'b', 5]
    result = filter_integers(input_list)
    assert result == [1, 2, 4, 5]

def test_filter_integers_with_only_integers():
    input_list = [1, 2, 3, 4, 5]
    result = filter_integers(input_list)
    assert result == [1, 2, 3, 4, 5]

def test_filter_integers_with_no_integers():
    input_list = ['a', 'b', 'c', 3.14]
    result = filter_integers(input_list)
    assert result == []

def test_filter_integers_with_empty_list():
    input_list = []
    result = filter_integers(input_list)
    assert result == []

def test_filter_integers_with_complex_types():
    input_list = [1, [2], {3}, (4,), 5]
    result = filter_integers(input_list)
    assert result == [1, 5]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 'a', 2, 3.14, 4, 'b', 5], [1, 2, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    (['a', 'b', 'c', 3.14], []),
    ([], []),
    ([1, [2], {3}, (4,), 5], [1, 5])
])
def test_filter_integers_parametrized(input_list, expected):
    result = filter_integers(input_list)
    assert result == expected
