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
    assert filter_integers([1, 2.3, 'hello', 4, 'world', 5]) == [1, 4, 5]

def test_filter_integers_none_in_list():
    assert filter_integers([1, None, 3, None, 5]) == [1, 3, 5]

@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3.0, 4, 5], [1, 2, 4, 5]),
    ([1, '2', 3, 4.0, '5'], [1, 3, 4]),
    ([True, False, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 4.0, 5.0], [1, 2, 3]),
])
def test_filter_integers_with_parametrize(input, expected):
    assert filter_integers(input) == expected

def test_filter_integers_with_string():
    with pytest.raises(TypeError):
        filter_integers('hello')

def test_filter_integers_with_set():
    with pytest.raises(TypeError):
        filter_integers({1, 2, 3})