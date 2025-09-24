# Test cases for HumanEval/29
# Generated using Claude API

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    return [x for x in strings if x.startswith(prefix)]


# Generated test cases:
import pytest
from typing import List

def filter_by_prefix(strings: List[str], prefix: str):
    return [x for x in strings if x.startswith(prefix)]

class TestFilterByPrefix:
    
    def test_empty_list(self):
        assert filter_by_prefix([], "test") == []
    
    def test_empty_prefix(self):
        strings = ["hello", "world", "test"]
        assert filter_by_prefix(strings, "") == ["hello", "world", "test"]
    
    def test_no_matches(self):
        strings = ["hello", "world", "test"]
        assert filter_by_prefix(strings, "xyz") == []
    
    def test_all_matches(self):
        strings = ["test1", "test2", "test3"]
        assert filter_by_prefix(strings, "test") == ["test1", "test2", "test3"]
    
    def test_partial_matches(self):
        strings = ["apple", "application", "banana", "app"]
        assert filter_by_prefix(strings, "app") == ["apple", "application", "app"]
    
    def test_exact_match(self):
        strings = ["test", "testing", "other"]
        assert filter_by_prefix(strings, "test") == ["test", "testing"]
    
    def test_case_sensitive(self):
        strings = ["Test", "test", "TEST"]
        assert filter_by_prefix(strings, "test") == ["test"]
    
    def test_single_character_prefix(self):
        strings = ["a", "ab", "abc", "b", "ba"]
        assert filter_by_prefix(strings, "a") == ["a", "ab", "abc"]
    
    def test_prefix_longer_than_string(self):
        strings = ["a", "ab", "abc"]
        assert filter_by_prefix(strings, "abcd") == []
    
    def test_special_characters(self):
        strings = ["@test", "@testing", "test@", "#test"]
        assert filter_by_prefix(strings, "@") == ["@test", "@testing"]
    
    def test_numbers_in_strings(self):
        strings = ["123abc", "123def", "456abc", "abc123"]
        assert filter_by_prefix(strings, "123") == ["123abc", "123def"]
    
    def test_whitespace_prefix(self):
        strings = [" test", " testing", "test ", "  test"]
        assert filter_by_prefix(strings, " ") == [" test", " testing", "  test"]
    
    def test_unicode_strings(self):
        strings = ["café", "cafeteria", "car", "çafe"]
        assert filter_by_prefix(strings, "caf") == ["café", "cafeteria"]
    
    @pytest.mark.parametrize("strings,prefix,expected", [
        (["hello", "help", "world"], "hel", ["hello", "help"]),
        (["python", "java", "javascript"], "java", ["java", "javascript"]),
        (["", "a", "ab"], "", ["", "a", "ab"]),
        (["test"], "test", ["test"]),
        (["short"], "verylongprefix", [])
    ])
    def test_parametrized_cases(self, strings, prefix, expected):
        assert filter_by_prefix(strings, prefix) == expected
    
    def test_duplicate_strings(self):
        strings = ["test", "test", "testing", "test"]
        assert filter_by_prefix(strings, "test") == ["test", "test", "testing", "test"]
    
    def test_newline_characters(self):
        strings = ["test\n", "test\nmore", "other"]
        assert filter_by_prefix(strings, "test") == ["test\n", "test\nmore"]
