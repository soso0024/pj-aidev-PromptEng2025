# Test cases for HumanEval/28
# Generated using Claude API

from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

    return ''.join(strings)


# Generated test cases:
from typing import List
import pytest

def test_concatenate(strings, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            from generated_tests_claude_3_haiku.test_humaneval_28_docstring import concatenate
            concatenate(strings)
    else:
        assert concatenate(strings) == expected

@pytest.mark.parametrize("strings,expected", [
    ([], ''),
    (['a', 'b', 'c'], 'abc'),
    ([' ', ' ', ' '], '   '),
    (['hello', 'world'], 'helloworld'),
    (['\n', '\t', '\r'], '\n\t\r'),
    (['"', "'", '\\'], '"\'\\'),
    ([1, 2, 3], TypeError),
    ([None, None, None], TypeError)
])
def test_concatenate(strings, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            from .test_humaneval_28_docstring import concatenate
            concatenate(strings)
    else:
        assert concatenate(strings) == expected