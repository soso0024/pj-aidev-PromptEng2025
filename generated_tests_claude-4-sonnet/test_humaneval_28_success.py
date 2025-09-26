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

def test_concatenate_empty_list():
    assert concatenate([]) == ""

def test_concatenate_single_string():
    assert concatenate(["hello"]) == "hello"

def test_concatenate_multiple_strings():
    assert concatenate(["hello", "world"]) == "helloworld"

def test_concatenate_with_spaces():
    assert concatenate(["hello", " ", "world"]) == "hello world"

def test_concatenate_empty_strings():
    assert concatenate(["", "", ""]) == ""

def test_concatenate_mixed_empty_and_non_empty():
    assert concatenate(["hello", "", "world"]) == "helloworld"

def test_concatenate_special_characters():
    assert concatenate(["hello", "!", "@", "#"]) == "hello!@#"

def test_concatenate_numbers_as_strings():
    assert concatenate(["1", "2", "3"]) == "123"

def test_concatenate_whitespace_strings():
    assert concatenate([" ", "\t", "\n"]) == " \t\n"

def test_concatenate_unicode_strings():
    assert concatenate(["café", "naïve"]) == "cafénaïve"

@pytest.mark.parametrize("input_list,expected", [
    ([], ""),
    (["a"], "a"),
    (["a", "b"], "ab"),
    (["hello", " ", "world"], "hello world"),
    (["", "test", ""], "test"),
    (["1", "2", "3", "4", "5"], "12345")
])
def test_concatenate_parametrized(input_list, expected):
    assert concatenate(input_list) == expected

def test_concatenate_long_strings():
    long_string = "a" * 1000
    assert concatenate([long_string, long_string]) == long_string * 2

def test_concatenate_quotes_in_strings():
    assert concatenate(['hello "world"', " it's nice"]) == 'hello "world" it\'s nice'

def test_concatenate_newlines_and_tabs():
    assert concatenate(["line1\n", "line2\t", "line3"]) == "line1\nline2\tline3"
