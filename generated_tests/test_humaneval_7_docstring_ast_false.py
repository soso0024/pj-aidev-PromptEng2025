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
    ([], "a", []),
    (["abc", "bacd", "cde", "array"], "a", ["abc", "bacd", "array"]),
    (["python", "java", "javascript"], "java", ["java", "javascript"]),
    (["", "test", "example"], "", ["", "test", "example"]),
    (["hello", "world"], "xyz", []),
    (["Test", "test"], "test", ["test"]),
    (["one", "two", "three"], " ", []),
    (["a", "aa", "aaa"], "aa", ["aa", "aaa"]),
    (["Special!@#", "Normal", "!@#"], "!@#", ["Special!@#", "!@#"]),
    ([" ", "  ", "   "], " ", [" ", "  ", "   "]),
])
def test_filter_by_substring_parametrized(strings, substring, expected):
    from filter_substring import filter_by_substring
    assert filter_by_substring(strings, substring) == expected


def test_filter_by_substring_empty_substring():
    strings = ["abc", "def", "ghi"]
    assert filter_by_substring(strings, "") == strings


def test_filter_by_substring_case_sensitivity():
    strings = ["Test", "testing", "TEST"]
    assert filter_by_substring(strings, "Test") == ["Test"]


def test_filter_by_substring_special_characters():
    strings = ["test\n", "test\t", "test\r", "normal"]
    assert filter_by_substring(strings, "\n") == ["test\n"]


@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    True,
    ["valid", None, "invalid"],
    ["valid", 123, "invalid"],
])
def test_filter_by_substring_invalid_input(invalid_input):
    with pytest.raises((TypeError, AttributeError)):
        filter_by_substring(invalid_input, "test")


@pytest.mark.parametrize("invalid_substring", [
    None,
    123,
    True,
    ["test"],
    {"key": "value"},
])
def test_filter_by_substring_invalid_substring(invalid_substring):
    with pytest.raises(TypeError):
        filter_by_substring(["test"], invalid_substring)