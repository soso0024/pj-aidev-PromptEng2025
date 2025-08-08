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
    assert filter_integers(['a', 3.14, 5, 'b', 7, 'c']) == [5, 7]

def test_filter_integers_none_in_list():
    assert filter_integers([None, 1, None, 2, None]) == [1, 2]

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 'a', 3.14, 4], [1, 2, 4]),
    ([True, False, 1, 0, 'hello'], [1, 0]),
    ([[], {}, (), 1, 2, 3], [1, 2, 3])
])
def test_filter_integers_various_inputs(input, expected):
    assert filter_integers(input) == expected

def test_filter_integers_string_representation_of_int():
    assert filter_integers(['1', '2', '3']) == []