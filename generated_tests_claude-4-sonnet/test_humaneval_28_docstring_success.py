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


def test_concatenate_empty_list():
    assert concatenate([]) == ''


def test_concatenate_single_string():
    assert concatenate(['hello']) == 'hello'


def test_concatenate_multiple_strings():
    assert concatenate(['a', 'b', 'c']) == 'abc'


def test_concatenate_strings_with_spaces():
    assert concatenate(['hello', ' ', 'world']) == 'hello world'


def test_concatenate_empty_strings():
    assert concatenate(['', '', '']) == ''


def test_concatenate_mixed_empty_and_non_empty():
    assert concatenate(['a', '', 'b', '', 'c']) == 'abc'


def test_concatenate_strings_with_special_characters():
    assert concatenate(['!', '@', '#', '$']) == '!@#$'


def test_concatenate_strings_with_numbers():
    assert concatenate(['1', '2', '3']) == '123'


def test_concatenate_long_strings():
    assert concatenate(['hello', 'world', 'python', 'programming']) == 'helloworldpythonprogramming'


def test_concatenate_strings_with_newlines():
    assert concatenate(['line1', '\n', 'line2']) == 'line1\nline2'


def test_concatenate_strings_with_tabs():
    assert concatenate(['col1', '\t', 'col2']) == 'col1\tcol2'


@pytest.mark.parametrize("input_list,expected", [
    ([], ''),
    (['a'], 'a'),
    (['a', 'b'], 'ab'),
    (['hello', 'world'], 'helloworld'),
    (['', 'test'], 'test'),
    (['test', ''], 'test'),
    (['1', '2', '3', '4', '5'], '12345')
])
def test_concatenate_parametrized(input_list, expected):
    assert concatenate(input_list) == expected


def test_concatenate_unicode_strings():
    assert concatenate(['café', 'naïve']) == 'cafénaïve'


def test_concatenate_strings_with_quotes():
    assert concatenate(['"hello"', "'world'"]) == '"hello"\'world\''
