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

def test_empty_list():
    assert concatenate([]) == ''

def test_single_string():
    assert concatenate(['hello']) == 'hello'

def test_multiple_strings():
    assert concatenate(['a', 'b', 'c']) == 'abc'

def test_strings_with_spaces():
    assert concatenate(['hello ', 'world']) == 'hello world'

def test_unicode_strings():
    assert concatenate(['こんにちは', 'world']) == 'こんにちはworld'

def test_numeric_strings():
    assert concatenate(['1', '2', '3']) == '123'

@pytest.mark.parametrize("input_list,expected", [
    ([], ''),
    (['a'], 'a'),
    (['hello', 'world'], 'helloworld'),
    (['123', '456'], '123456'),
    (['', 'test', ''], 'test')
])
def test_concatenate_parametrized(input_list, expected):
    assert concatenate(input_list) == expected

def test_type_error():
    with pytest.raises(TypeError):
        concatenate([1, 2, 3])
