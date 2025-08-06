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
    ([0, -1, 999999], [0, -1, 999999]),
    ([[], {}, (), 5], [5]),
    ([1, 2.5, "3", [4], 5], [1, 5]),
    ([object(), 42, None, 123], [42, 123])
])
def test_filter_integers_parametrized(test_input, expected):
    from filter_integers import filter_integers
    result = filter_integers(test_input)
    assert result == expected

def test_filter_integers_empty_list():
    assert filter_integers([]) == []

def test_filter_integers_only_integers():
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_filter_integers_no_integers():
    assert filter_integers(["a", 1.5, None]) == []

def test_filter_integers_mixed_types():
    assert filter_integers([1, "two", 3, 4.0, 5]) == [1, 3, 5]

def test_filter_integers_with_negative_numbers():
    assert filter_integers([-1, -2, 0, 1, 2]) == [-1, -2, 0, 1, 2]

def test_filter_integers_with_bool():
    assert filter_integers([True, False, 1, 2]) == [1, 2]

@pytest.mark.parametrize("invalid_input", [
    None,
    42,
    "string",
    {},
    set()
])
def test_filter_integers_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        filter_integers(invalid_input)