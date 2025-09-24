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

def filter_by_substring(strings: List[str], substring: str):
    return [x for x in strings if substring in x]

class TestFilterBySubstring:
    
    def test_empty_list(self):
        assert filter_by_substring([], "test") == []
    
    def test_empty_substring(self):
        strings = ["hello", "world", "python"]
        assert filter_by_substring(strings, "") == ["hello", "world", "python"]
    
    def test_no_matches(self):
        strings = ["apple", "banana", "cherry"]
        assert filter_by_substring(strings, "xyz") == []
    
    def test_all_matches(self):
        strings = ["testing", "test", "contest"]
        assert filter_by_substring(strings, "test") == ["testing", "test", "contest"]
    
    def test_partial_matches(self):
        strings = ["hello", "world", "help", "welcome"]
        assert filter_by_substring(strings, "el") == ["hello", "help", "welcome"]
    
    def test_case_sensitive(self):
        strings = ["Hello", "hello", "HELLO"]
        assert filter_by_substring(strings, "hello") == ["hello"]
    
    def test_single_character_substring(self):
        strings = ["cat", "dog", "bird", "fish"]
        assert filter_by_substring(strings, "a") == ["cat"]
    
    def test_substring_longer_than_strings(self):
        strings = ["a", "bb", "ccc"]
        assert filter_by_substring(strings, "dddd") == []
    
    def test_exact_match(self):
        strings = ["exact", "not exact", "exactly"]
        assert filter_by_substring(strings, "exact") == ["exact", "not exact", "exactly"]
    
    def test_special_characters(self):
        strings = ["hello@world", "test#123", "normal"]
        assert filter_by_substring(strings, "@") == ["hello@world"]
    
    def test_numbers_in_strings(self):
        strings = ["test123", "abc456", "789xyz"]
        assert filter_by_substring(strings, "123") == ["test123"]
    
    def test_whitespace_substring(self):
        strings = ["hello world", "helloworld", "hello  world"]
        assert filter_by_substring(strings, " ") == ["hello world", "hello  world"]
    
    def test_unicode_characters(self):
        strings = ["café", "naïve", "résumé", "normal"]
        assert filter_by_substring(strings, "é") == ["café", "résumé"]
    
    @pytest.mark.parametrize("strings,substring,expected", [
        (["a", "ab", "abc"], "a", ["a", "ab", "abc"]),
        (["test1", "test2", "other"], "test", ["test1", "test2"]),
        (["", "a", ""], "a", ["a"]),
        (["", "", ""], "", ["", "", ""]),
    ])
    def test_parametrized_cases(self, strings, substring, expected):
        assert filter_by_substring(strings, substring) == expected
    
    def test_empty_strings_in_list(self):
        strings = ["", "hello", "", "world", ""]
        assert filter_by_substring(strings, "") == ["", "hello", "", "world", ""]
    
    def test_empty_strings_with_non_empty_substring(self):
        strings = ["", "hello", "", "world"]
        assert filter_by_substring(strings, "test") == []
    
    def test_duplicate_strings(self):
        strings = ["test", "test", "other", "test"]
        assert filter_by_substring(strings, "test") == ["test", "test", "test"]
