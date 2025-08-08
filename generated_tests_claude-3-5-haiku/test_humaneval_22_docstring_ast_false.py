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

def test_filter_integers_normal_cases():
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers(['a', 3.14, 5]) == [5]

def test_filter_integers_empty_list():
    assert filter_integers([]) == []

def test_filter_integers_no_integers():
    assert filter_integers(['a', 3.14, {}, []]) == []

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([0, -1, -10, 100], [0, -1, -10, 100]),
    ([1.5, 2.7, 3, 4.2, 5], [3]),
    (['str', None, True, False, 42], [42]),
])
def test_filter_integers_parametrized(input_list, expected):
    assert filter_integers(input_list) == expected

def test_filter_integers_mixed_types():
    assert filter_integers([1, 'a', 2, 3.14, {}, [], 4, 5]) == [1, 2, 4, 5]