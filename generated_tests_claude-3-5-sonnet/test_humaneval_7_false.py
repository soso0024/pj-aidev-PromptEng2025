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


@pytest.mark.parametrize("strings, substring, expected", [
    (["hello", "world", "hello world"], "hello", ["hello", "hello world"]),
    (["test", "testing", "tested"], "test", ["test", "testing", "tested"]),
    ([], "test", []),
    (["hello", "world"], "", ["hello", "world"]),
    (["hello", "world"], " ", []),
    (["", "test", ""], "test", ["test"]),
    (["HELLO", "WORLD"], "hello", []),
    (["one", "two", "three"], "four", []),
    (["test123", "123test", "test"], "123", ["test123", "123test"]),
    (["!@#", "$%^", "!@#$%^"], "!@#", ["!@#", "!@#$%^"]),
])
def test_filter_by_substring_parametrized(strings: List[str], substring: str, expected: List[str], filter_by_substring):
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_empty_substring(filter_by_substring):
    strings = ["hello", "world"]
    assert filter_by_substring(strings, "") == strings

def test_filter_by_substring_case_sensitive(filter_by_substring):
    strings = ["Hello", "HELLO", "hello"]
    assert filter_by_substring(strings, "hello") == ["hello"]

def test_filter_by_substring_special_chars(filter_by_substring):
    strings = ["test\n", "test\t", "test"]
    assert filter_by_substring(strings, "\n") == ["test\n"]

def test_filter_by_substring_unicode(filter_by_substring):
    strings = ["café", "cafe", "café latte"]
    assert filter_by_substring(strings, "é") == ["café", "café latte"]

@pytest.mark.parametrize("invalid_input", [
    None,
    42,
    True,
    (1, 2, 3)
])
def test_filter_by_substring_invalid_input(invalid_input, filter_by_substring):
    with pytest.raises(TypeError):
        filter_by_substring(invalid_input, "test")

def test_filter_by_substring_dict_input(filter_by_substring):
    with pytest.raises(TypeError):
        filter_by_substring({"key": "value"}, "test")

def test_filter_by_substring_invalid_substring(filter_by_substring):
    with pytest.raises(TypeError):
        filter_by_substring(["test"], None)

def test_filter_by_substring_non_string_list(filter_by_substring):
    with pytest.raises(TypeError):
        filter_by_substring([1, 2, 3], "test")

@pytest.fixture
def filter_by_substring():
    def _filter_by_substring(strings: List[str], substring: str) -> List[str]:
        return [x for x in strings if substring in x]
    return _filter_by_substring