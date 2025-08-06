# Test cases for HumanEval/7
# Generated using Claude API

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    return [x for x in strings if substring in x]


# Generated test cases:
import pytest
from typing import List

@pytest.mark.parametrize("strings,substring,expected", [
    (["hello", "world", "hello world"], "hello", ["hello", "hello world"]),
    (["test", "testing", "tested"], "test", ["test", "testing", "tested"]),
    (["abc", "def", "ghi"], "x", []),
    ([], "test", []),
    (["", "test", ""], "", ["", "test", ""]),
    (["Hello", "HELLO", "hello"], "hello", ["hello"]),
    (["one two", "three four", "five six"], " ", ["one two", "three four", "five six"]),
    (["special!@#", "normal", "!@#chars"], "!@#", ["special!@#", "!@#chars"]),
    (["a", "aa", "aaa"], "aa", ["aa", "aaa"]),
    ([" ", "  ", "   "], " ", [" ", "  ", "   "])
])
def test_filter_by_substring_parametrized(strings: List[str], substring: str, expected: List[str]):
    from filter_substring import filter_by_substring
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_empty_substring():
    strings = ["test", "hello", "world"]
    assert filter_by_substring(strings, "") == strings

def test_filter_by_substring_case_sensitive():
    strings = ["Test", "test", "TEST"]
    assert filter_by_substring(strings, "test") == ["test"]

def test_filter_by_substring_special_characters():
    strings = ["test\n", "test\t", "test\r"]
    assert filter_by_substring(strings, "\n") == ["test\n"]

def test_filter_by_substring_unicode():
    strings = ["café", "cafe", "café au lait"]
    assert filter_by_substring(strings, "é") == ["café", "café au lait"]

@pytest.mark.parametrize("invalid_strings", [
    None,
    42,
    True,
    {"set", "of", "strings"}
])
def test_filter_by_substring_invalid_input_type(invalid_strings):
    with pytest.raises(TypeError):
        filter_by_substring(invalid_strings, "test")

@pytest.mark.parametrize("invalid_substring", [
    None,
    42,
    True,
    ["list"],
    {"dict": "value"}
])
def test_filter_by_substring_invalid_substring_type(invalid_substring):
    with pytest.raises(TypeError):
        filter_by_substring(["test"], invalid_substring)