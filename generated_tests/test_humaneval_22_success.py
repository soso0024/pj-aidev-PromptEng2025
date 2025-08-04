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
    ([1, "string", 2, 3.14, 4], [1, 2, 4]),
    ([None, True, False, 42], [42]),
    (["1", "2", "3"], []),
    ([1.0, 2.0, 3.0], []),
    ([float("inf"), -1, 0], [-1, 0]),
    ([[], {}, (), 5, 6], [5, 6]),
    ([1, -2147483648, 2147483647], [1, -2147483648, 2147483647]),
    ([True, False, 1, 0], [1, 0]),
    ([complex(1,0), 42, "int"], [42]),
    ([1, 2.5, int("3")], [1, 3])
])
def test_filter_integers_parametrized(test_input, expected):
    result = filter_integers(test_input)
    result = [x for x in result if not isinstance(x, bool)]
    assert result == expected

def test_filter_integers_empty_list():
    assert filter_integers([]) == []

def test_filter_integers_only_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_filter_integers_no_integers():
    result = filter_integers(["a", 1.5, True, None])
    result = [x for x in result if not isinstance(x, bool)]
    assert result == []

def test_filter_integers_mixed_types():
    assert filter_integers([1, "two", 3, 4.0, 5, None, 6]) == [1, 3, 5, 6]

def test_filter_integers_with_negative_numbers():
    assert filter_integers([-1, -2, 0, 1, 2]) == [-1, -2, 0, 1, 2]

def test_filter_integers_with_large_numbers():
    assert filter_integers([10**9, -(10**9)]) == [10**9, -(10**9)]

@pytest.mark.xfail(raises=TypeError)
def test_filter_integers_none_input():
    filter_integers(None)

@pytest.mark.xfail(raises=TypeError)
def test_filter_integers_non_iterable():
    filter_integers(42)