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

def how_many_times(string: str, substring: str) -> int:
    times = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1
    return times

@pytest.mark.parametrize("string,substring,expected", [
    ("", "a", 0),
    ("aaa", "a", 3),
    ("aaaa", "aa", 3),
    ("", "", 1),
    ("hello", "", 6),
    ("abc", "xyz", 0),
    ("abcabc", "abc", 2),
    ("ababab", "aba", 2),
    ("aaaaaa", "aaa", 4),
    ("hello world", "l", 3),
    ("hello world", "ll", 1),
    ("hello world", "world", 1),
    ("hello world", "hello world", 1),
    ("hello world", "hello world!", 0),
    ("abcdefg", "cde", 1),
    ("abcdefg", "xyz", 0),
    ("aaabaaabaaab", "aaa", 3),
    ("overlapping", "pp", 1),
    ("banana", "ana", 2),
    ("banana", "an", 2),
    ("banana", "na", 2),
    ("abababab", "abab", 3),
    ("test", "test", 1),
    ("test", "testing", 0),
    ("a", "a", 1),
    ("a", "aa", 0),
    ("123123123", "123", 3),
    ("123123123", "231", 2),
    ("abcabcabc", "ca", 2),
    ("xyxyxyxy", "xyxy", 3)
])
def test_how_many_times_parametrized(string, substring, expected):
    assert how_many_times(string, substring) == expected

def test_empty_string_empty_substring():
    assert how_many_times("", "") == 1

def test_empty_string_non_empty_substring():
    assert how_many_times("", "abc") == 0

def test_non_empty_string_empty_substring():
    assert how_many_times("hello", "") == 6

def test_single_character_string_single_character_substring_match():
    assert how_many_times("a", "a") == 1

def test_single_character_string_single_character_substring_no_match():
    assert how_many_times("a", "b") == 0

def test_overlapping_patterns():
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("aaaaaa", "aa") == 5
    assert how_many_times("abababab", "aba") == 3

def test_no_overlapping_patterns():
    assert how_many_times("abcabc", "abc") == 2
    assert how_many_times("xyzxyz", "xyz") == 2

def test_substring_longer_than_string():
    assert how_many_times("abc", "abcdef") == 0
    assert how_many_times("a", "abc") == 0

def test_case_sensitive():
    assert how_many_times("AaAa", "a") == 2
    assert how_many_times("AaAa", "A") == 2
    assert how_many_times("Hello", "hello") == 0

def test_special_characters():
    assert how_many_times("!@#!@#", "!@#") == 2
    assert how_many_times("a.b.c.d", ".") == 3
    assert how_many_times("a..b..c", "..") == 2

def test_whitespace():
    assert how_many_times("a b c d", " ") == 3
    assert how_many_times("  hello  world  ", "  ") == 3
    assert how_many_times("\n\n\n", "\n") == 3

def test_numbers_as_strings():
    assert how_many_times("1234512345", "123") == 2
    assert how_many_times("1111", "11") == 3