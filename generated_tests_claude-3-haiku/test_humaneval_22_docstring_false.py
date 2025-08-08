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
from typing import List, Any
import pytest

def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if isinstance(x, int)]

def test_filter_integers_empty_list():
    assert filter_integers([]) == []

def test_filter_integers_all_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_filter_integers_mixed_types():
    assert filter_integers([1, 2.3, 'abc', 4, [5]]) == [1, 4]

def test_filter_integers_only_non_integers():
    assert filter_integers(['a', 'b', 'c']) == []

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3.14, 'four', 5], [1, 2, 5]),
    ([True, False, 42, None, 3.14], [42]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([], [])
])
def test_filter_integers_parametrized(input, expected):
    assert filter_integers(input) == expected