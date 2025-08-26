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
    assert concatenate(['hello', 'world', '123']) == 'helloworld123'

@pytest.mark.parametrize("input_strings,expected", [
    ([], ''),
    ([''], ''),
    (['hello'], 'hello'),
    (['hello', 'world'], 'helloworld'),
    (['a', 'b', 'c', 'd', 'e'], 'abcde')
])
def test_concatenate_parametrized(input_strings, expected):
    assert concatenate(input_strings) == expected

def test_concatenate_with_none():
    with pytest.raises(TypeError):
        concatenate([None])

def test_concatenate_with_non_string_element():
    with pytest.raises(TypeError):
        concatenate([1, 2, 3])
