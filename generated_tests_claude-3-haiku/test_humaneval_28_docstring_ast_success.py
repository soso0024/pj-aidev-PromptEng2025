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

def test_concatenate_empty_list():
    assert concatenate([]) == ''

def test_concatenate_single_string():
    assert concatenate(['a']) == 'a'

def test_concatenate_multiple_strings():
    assert concatenate(['a', 'b', 'c']) == 'abc'

@pytest.mark.parametrize("input_strings,expected", [
    ([], ''),
    (['x'], 'x'),
    (['hello', 'world'], 'helloworld'),
    ([' ', ' ', ' '], '   '),
    (['1', '2', '3', '4', '5'], '12345')
])
def test_concatenate_parameterized(input_strings, expected):
    assert concatenate(input_strings) == expected

def test_concatenate_with_none():
    with pytest.raises(TypeError):
        concatenate([None])