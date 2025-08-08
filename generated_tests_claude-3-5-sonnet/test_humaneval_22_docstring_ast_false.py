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


@pytest.mark.parametrize("test_input,expected", [
    ([], []),
    ([1, 2, 3], [1, 2, 3]),
    ([1.0, 2.0, 3.0], []),
    (["a", "b", "c"], []),
    ([1, "a", 2, "b", 3], [1, 2, 3]),
    ([None, True, False, 1], [1]),
    ([1, 2.5, "3", [4], {5}, (6,)], [1]),
    ([0, -1, 1000000], [0, -1, 1000000]),
    ([float("inf"), -float("inf"), 42], [42]),
    ([1, 1.0, True, "1"], [1]),
    ([[], {}, (), set(), 1], [1]),
    ([object(), 1, Exception(), 2], [1, 2])
])
def test_filter_integers_parametrized(test_input, expected):
    assert filter_integers(test_input) == expected


def test_filter_integers_empty_list():
    assert filter_integers([]) == []


def test_filter_integers_only_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_filter_integers_no_integers():
    assert filter_integers(["a", 1.5, [], {}]) == []


def test_filter_integers_mixed_types():
    assert filter_integers([1, "string", 2.0, 3, True, 4]) == [1, 3, 4]


def test_filter_integers_with_none():
    assert filter_integers([None, 1, None, 2]) == [1, 2]


def test_filter_integers_with_nested_structures():
    assert filter_integers([[1], 1, [2, 3], 2]) == [1, 2]


def test_filter_integers_type_error():
    with pytest.raises(TypeError):
        filter_integers(42)
    with pytest.raises(TypeError):
        filter_integers(None)