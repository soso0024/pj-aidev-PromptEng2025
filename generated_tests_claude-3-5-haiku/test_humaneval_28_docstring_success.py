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
import pytest

def test_concatenate_empty_list():
    assert concatenate([]) == ''

def test_concatenate_single_string():
    assert concatenate(['hello']) == 'hello'

def test_concatenate_multiple_strings():
    assert concatenate(['a', 'b', 'c']) == 'abc'

def test_concatenate_with_empty_strings():
    assert concatenate(['', '', '']) == ''

def test_concatenate_mixed_strings():
    assert concatenate(['hello', ' ', 'world']) == 'hello world'

@pytest.mark.parametrize("input_list,expected", [
    ([], ''),
    (['python'], 'python'),
    (['a', 'b', 'c'], 'abc'),
    (['hello', ' ', 'world'], 'hello world'),
    (['', 'test', ''], 'test')
])
def test_concatenate_parametrized(input_list, expected):
    assert concatenate(input_list) == expected

def test_concatenate_type_error():
    with pytest.raises(TypeError):
        concatenate([1, 2, 3])

def test_concatenate_none_input():
    with pytest.raises(TypeError):
        concatenate(None)
