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

def concatenate(strings: List[str]):
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
    assert concatenate(['', '', 'hello', '', 'world', '']) == 'helloworld'

@pytest.mark.parametrize("input_strings,expected", [
    (['python', 'testing'], 'pythontesting'),
    (['', ''], ''),
    (['123', '456', '789'], '123456789'),
    (['special', 'chars!', '@#$'], 'specialchars!@#$')
])
def test_concatenate_parametrized(input_strings, expected):
    assert concatenate(input_strings) == expected

def test_concatenate_non_string_raises_type_error():
    with pytest.raises(TypeError):
        concatenate([1, 2, 3])

def test_concatenate_mixed_type_raises_type_error():
    with pytest.raises(TypeError):
        concatenate(['hello', 42, 'world'])
