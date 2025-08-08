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

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

def test_concatenate_empty_list():
    assert concatenate([]) == ''

def test_concatenate_single_string():
    assert concatenate(['hello']) == 'hello'

@pytest.mark.parametrize("input_strings,expected", [
    (['one', 'two', 'three'], 'onetwothree'),
    (['a', 'b', 'c', 'd', 'e'], 'abcde'),
    ([' ', ' ', ' '], '   '),
])
def test_concatenate_multiple_strings(input_strings, expected):
    assert concatenate(input_strings) == expected

def test_concatenate_with_non_string_element():
    with pytest.raises(TypeError):
        concatenate([1, 'two', 3.0])