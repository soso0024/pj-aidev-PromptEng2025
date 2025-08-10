# Test cases for HumanEval/12
# Generated using Claude API

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


# Generated test cases:
import pytest
from typing import List, Optional

@pytest.mark.parametrize("strings,expected", [
    ([], None),
    (['abc', 'def', 'ghi'], 'abc'),
    (['short', 'longer', 'longest'], 'longest'),
    (['one', 'two', 'three'], 'three'),
    (['apple', 'banana', 'cherry', 'date'], 'banana'),
    ([' ', '  ', '   '], ' '),
    ([''], None),
    ([None], None),
    (['1', '2', '3'], '3'),
])
def test_longest(strings, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            assert longest(strings) == expected
    else:
        assert longest(strings) == expected