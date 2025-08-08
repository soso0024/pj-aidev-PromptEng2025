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

def test_filter_integers_empty_list():
    assert filter_integers([]) == []

def test_filter_integers_all_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_filter_integers_mixed_types():
    assert filter_integers([1, 2.3, "four", 5, "six"]) == [1, 5]

def test_filter_integers_none_in_list():
    assert filter_integers([None, 1, None, 2, None]) == [1, 2]

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3.0, 4, 5], [1, 2, 4, 5]),
    ([1, "two", 3, 4.0, "five"], [1, 3, 4]),
    ([True, False, 1, 2, 3], [1, 2, 3]),
    (["one", "two", "three"], [])
])
def test_filter_integers_parametrized(input, expected):
    assert filter_integers(input) == expected

def test_filter_integers_raises_type_error():
    with pytest.raises(TypeError):
        filter_integers(None)