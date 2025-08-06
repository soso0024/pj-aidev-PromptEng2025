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
    (["", "test", ""], "", ["", "test", ""]),
    (["abc", "def", "ghi"], "xyz", []),
    (["Hello", "World", "Hello World"], " ", ["Hello World"]),
    (["Test", "test", "TEST"], "test", ["test"]),
    (["one", "two", "three"], "", ["one", "two", "three"]),
    ([" ", "  ", "   "], " ", [" ", "  ", "   "]),
    (["!@#", "$%^", "&*("], "#", ["!@#"]),
])
def test_filter_by_substring_parametrized(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected


def test_filter_by_substring_empty_substring():
    input_list = ["abc", "def", "ghi"]
    assert filter_by_substring(input_list, "") == input_list


def test_filter_by_substring_case_sensitive():
    input_list = ["Test", "testing", "TEST"]
    assert filter_by_substring(input_list, "Test") == ["Test"]


def test_filter_by_substring_special_characters():
    input_list = ["test.com", "test*com", "test@com"]
    assert filter_by_substring(input_list, ".") == ["test.com"]


def test_filter_by_substring_whitespace():
    input_list = ["no space", "nospace", "no  space"]
    assert filter_by_substring(input_list, "  ") == ["no  space"]


@pytest.mark.parametrize("invalid_input", [
    None,
    42,
    True,
    3.14,
])
def test_filter_by_substring_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        filter_by_substring(invalid_input, "test")


def test_filter_by_substring_invalid_substring():
    with pytest.raises(TypeError):
        filter_by_substring(["test"], None)
