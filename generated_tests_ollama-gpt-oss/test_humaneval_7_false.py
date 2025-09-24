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
import sys, os
sys.path.append(os.path.abspath('..'))
import pytest
from typing import List
from humaneval_7 import filter_by_substring

@pytest.mark.parametrize(
    "strings, substring, expected",
    [
        # Empty list
        ([], "a", []),
        # Empty substring matches all strings
        (["abc", "def"], "", ["abc", "def"]),
        # Substring not present
        (["abc", "def"], "x", []),
        # Substring present in one string
        (["abc", "def"], "d", ["def"]),
        # Substring present in multiple strings
        (["abc", "abd", "cde"], "a", ["abc", "abd"]),
        # Substring at start
        (["abc", "def"], "a", ["abc"]),
        # Substring at end
        (["abc", "def"], "c", ["abc"]),
        # Substring in middle
        (["abc", "def"], "b", ["abc"]),
        # Case sensitivity
        (["Abc", "abc"], "a", ["abc"]),
        # Unicode
        (["café", "cafe"], "é", ["café"]),
        # Emoji
        (["😊abc😊", "def"], "😊", ["😊abc😊"]),
        # Special characters
        (["$abc$", "def"], "$", ["$abc$"]),
        # Duplicate strings
        (["abc", "abc"], "a", ["abc", "abc"]),
        # Multiple occurrences in a single string
        (["aba"], "a", ["aba"]),
        # Substring appears in multiple strings
        (["abc", "def", "ghi"], "a", ["abc"]),
    ],
)
def test_filter_by_substring_basic(strings: List[str], substring: str, expected: List[str]):
    result = filter_by_substring(strings, substring)
    assert result == expected
    assert isinstance(result, list)

def test_original_list_not_mutated():
    original = ["abc", "def"]
    result = filter_by_substring(original, "a")
    assert original == ["abc", "def"]
    assert result != original

def test_empty_list_and_empty_substring():
    assert filter_by_substring([], "") == []

def test_none_substring_raises_type_error():
    with pytest.raises(TypeError):
        filter_by_substring(["abc"], None)

def test_non_string_element_raises_type_error():
    with pytest.raises(TypeError):
        filter_by_substring(["abc", 123], "a")

def test_strings_not_iterable_raises_type_error():
    with pytest.raises(TypeError):
        filter_by_substring(123, "a")

def test_tuple_input_returns_list():
    strings = ("abc", "def")
    result = filter_by_substring(strings, "a")
    assert result == ["abc"]

def test_generator_input_returns_list():
    strings = (s for s in ["abc", "def"])
    result = filter_by_substring(strings, "a")
    assert result == ["abc"]