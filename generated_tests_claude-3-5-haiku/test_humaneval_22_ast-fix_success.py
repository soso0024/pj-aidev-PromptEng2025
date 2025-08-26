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

def test_filter_integers_normal_case():
    assert filter_integers([1, 2, 'a', 3, 'b', 4]) == [1, 2, 3, 4]

def test_filter_integers_empty_list():
    assert filter_integers([]) == []

def test_filter_integers_no_integers():
    assert filter_integers(['a', 'b', 'c']) == []

def test_filter_integers_all_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_filter_integers_mixed_types():
    assert filter_integers([1, 'a', 2.5, 3, None, 4, [5], {6}]) == [1, 3, 4]

@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
    (['a', 'b'], []),
    ([1, 'a', 2.5, 3], [1, 3]),
    ([None, 1, 'test', 2], [1, 2])
])
def test_filter_integers_parametrized(input_list, expected):
    assert filter_integers(input_list) == expected
