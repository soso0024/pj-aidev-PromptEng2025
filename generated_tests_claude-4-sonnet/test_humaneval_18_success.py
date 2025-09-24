# Test cases for HumanEval/18
# Generated using Claude API



def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times


# Generated test cases:
import pytest

def how_many_times(string: str, substring: str):
    times = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1
    return times

class TestHowManyTimes:
    
    def test_empty_string_empty_substring(self):
        assert how_many_times("", "") == 1
    
    def test_empty_string_non_empty_substring(self):
        assert how_many_times("", "a") == 0
    
    def test_non_empty_string_empty_substring(self):
        assert how_many_times("hello", "") == 6
    
    def test_substring_not_found(self):
        assert how_many_times("hello", "xyz") == 0
    
    def test_substring_found_once(self):
        assert how_many_times("hello", "ell") == 1
    
    def test_substring_found_multiple_times_non_overlapping(self):
        assert how_many_times("abcabc", "abc") == 2
    
    def test_substring_found_multiple_times_overlapping(self):
        assert how_many_times("aaaa", "aa") == 3
    
    def test_substring_same_as_string(self):
        assert how_many_times("hello", "hello") == 1
    
    def test_substring_longer_than_string(self):
        assert how_many_times("hi", "hello") == 0
    
    def test_single_character_string_and_substring_match(self):
        assert how_many_times("a", "a") == 1
    
    def test_single_character_string_and_substring_no_match(self):
        assert how_many_times("a", "b") == 0
    
    def test_repeated_single_character(self):
        assert how_many_times("aaaaa", "a") == 5
    
    def test_case_sensitive(self):
        assert how_many_times("Hello", "hello") == 0
        assert how_many_times("Hello", "Hello") == 1
    
    def test_special_characters(self):
        assert how_many_times("a!b@c#a!b@c#", "!b@") == 2
    
    def test_whitespace_characters(self):
        assert how_many_times("a b c a b c", " b ") == 2
    
    def test_numbers_as_strings(self):
        assert how_many_times("123123123", "123") == 3
    
    def test_overlapping_pattern_complex(self):
        assert how_many_times("abababab", "abab") == 3
    
    @pytest.mark.parametrize("string,substring,expected", [
        ("", "", 1),
        ("", "a", 0),
        ("hello", "", 6),
        ("abcdef", "cd", 1),
        ("abcabcabc", "abc", 3),
        ("aaaa", "aa", 3),
        ("test", "test", 1),
        ("short", "verylongsubstring", 0),
        ("mississippi", "issi", 2),
        ("banana", "ana", 2)
    ])
    def test_parametrized_cases(self, string, substring, expected):
        assert how_many_times(string, substring) == expected
