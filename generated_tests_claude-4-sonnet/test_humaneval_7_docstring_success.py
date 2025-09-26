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


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


class TestFilterBySubstring:
    
    def test_empty_list(self):
        assert filter_by_substring([], 'a') == []
    
    def test_empty_substring(self):
        strings = ['abc', 'def', 'ghi']
        assert filter_by_substring(strings, '') == strings
    
    def test_no_matches(self):
        assert filter_by_substring(['xyz', 'def', 'ghi'], 'a') == []
    
    def test_all_matches(self):
        strings = ['abc', 'bac', 'cab']
        assert filter_by_substring(strings, 'a') == strings
    
    def test_partial_matches(self):
        assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    
    def test_case_sensitive(self):
        assert filter_by_substring(['ABC', 'abc', 'Abc'], 'a') == ['abc']
    
    def test_substring_longer_than_strings(self):
        assert filter_by_substring(['a', 'ab', 'abc'], 'abcd') == []
    
    def test_exact_match(self):
        assert filter_by_substring(['hello', 'world'], 'hello') == ['hello']
    
    def test_substring_at_beginning(self):
        assert filter_by_substring(['hello', 'help', 'world'], 'hel') == ['hello', 'help']
    
    def test_substring_at_end(self):
        assert filter_by_substring(['testing', 'running', 'jumping'], 'ing') == ['testing', 'running', 'jumping']
    
    def test_substring_in_middle(self):
        assert filter_by_substring(['hello', 'yellow', 'mellow'], 'ell') == ['hello', 'yellow', 'mellow']
    
    def test_special_characters(self):
        assert filter_by_substring(['test@email.com', 'user@domain.org', 'noatsign'], '@') == ['test@email.com', 'user@domain.org']
    
    def test_numbers_in_strings(self):
        assert filter_by_substring(['abc123', 'def456', 'ghi'], '123') == ['abc123']
    
    def test_whitespace_substring(self):
        assert filter_by_substring(['hello world', 'helloworld', 'test case'], ' ') == ['hello world', 'test case']
    
    def test_single_character_strings(self):
        assert filter_by_substring(['a', 'b', 'c', 'a'], 'a') == ['a', 'a']
    
    def test_single_character_substring(self):
        assert filter_by_substring(['apple', 'banana', 'cherry'], 'a') == ['apple', 'banana']
    
    @pytest.mark.parametrize("strings,substring,expected", [
        ([], "test", []),
        (["abc"], "a", ["abc"]),
        (["abc"], "d", []),
        (["hello", "world"], "o", ["hello", "world"]),
        (["Python", "Java", "C++"], "++", ["C++"]),
    ])
    def test_parametrized_cases(self, strings, substring, expected):
        assert filter_by_substring(strings, substring) == expected
