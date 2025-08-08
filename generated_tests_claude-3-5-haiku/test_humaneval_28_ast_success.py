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
from typing import List

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

def test_concatenate_normal_case():
    assert concatenate(['hello', 'world']) == 'helloworld'

def test_concatenate_empty_list():
    assert concatenate([]) == ''

def test_concatenate_single_string():
    assert concatenate(['test']) == 'test'

def test_concatenate_multiple_strings():
    assert concatenate(['a', 'b', 'c', 'd']) == 'abcd'

def test_concatenate_with_empty_strings():
    assert concatenate(['', '', 'test', '']) == 'test'

@pytest.mark.parametrize("input_strings,expected", [
    (['hello', 'world'], 'helloworld'),
    ([], ''),
    ([''], ''),
    (['a', 'b', 'c'], 'abc'),
    (['', 'test', ''], 'test')
])
def test_concatenate_parametrized(input_strings, expected):
    assert concatenate(input_strings) == expected

def test_concatenate_with_special_characters():
    assert concatenate(['hello!', '@world', '123']) == 'hello!@world123'

def test_concatenate_with_unicode():
    assert concatenate(['こんにちは', '世界']) == 'こんにちは世界'

def test_concatenate_type_error():
    with pytest.raises(TypeError):
        concatenate([1, 2, 3])
