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
from how_many_times import how_many_times
import pytest

@pytest.mark.parametrize("string, substring, expected", [
    ("", "a", 0),
    ("aaa", "a", 3),
    ("aaaa", "aa", 3),
    ("abcdefghijklmnopqrstuvwxyz", "abc", 1),
    ("abcabcabc", "abc", 3),
    ("aaaaaaaaa", "aa", 4),
    ("ababab", "ab", 3),
    ("mississippi", "iss", 2),
    ("hello world", "l", 3),
    ("python is awesome", "on", 1),
])
def test_how_many_times(string, substring, expected):
    assert how_many_times(string, substring) == expected

def test_empty_string():
    assert how_many_times("", "") == 0

def test_substring_not_found():
    assert how_many_times("hello", "world") == 0

def test_substring_longer_than_string():
    assert how_many_times("abc", "abcdef") == 0