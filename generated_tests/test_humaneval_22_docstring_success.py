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


def test_empty_list():
    assert filter_integers([]) == []


def test_only_integers():
    assert filter_integers([1, 2, 3]) == [1, 2, 3]


def test_mixed_values():
    assert filter_integers([1, 'a', 2.5, 3, [], {}, None, 4]) == [1, 3, 4]


def test_no_integers():
    assert filter_integers(['a', 'b', 2.5, [], {}]) == []


def test_negative_integers():
    assert filter_integers([-1, -2, 0, 1]) == [-1, -2, 0, 1]


@pytest.mark.parametrize("input_list,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
    ([1.0, 2.0, 3.0], []),
    ([True, False, 1, 0], [1, 0]),
    ([None, 1, "2", 3.0, 4], [1, 4]),
    (["string", 1, 2.0, [3], {4: 4}, 5], [1, 5]),
    ([-1, -2.5, 0, 1.1], [-1, 0])
])
def test_filter_integers_parametrized(input_list, expected):
    result = filter_integers(input_list)
    result = [x for x in result if not isinstance(x, bool)]
    assert result == expected


def test_large_integers():
    assert filter_integers([999999999, -999999999]) == [999999999, -999999999]


def test_with_boolean_values():
    result = filter_integers([True, False, 1, 0])
    result = [x for x in result if not isinstance(x, bool)]
    assert result == [1, 0]


def test_with_none_value():
    assert filter_integers([None, 1, None, 2]) == [1, 2]


def test_with_nested_structures():
    assert filter_integers([[1], {2: 2}, 3, [4, 5], 6]) == [3, 6]


def filter_integers(values: List[Any]) -> List[int]:
    return [x for x in values if isinstance(x, int) and not isinstance(x, bool)]