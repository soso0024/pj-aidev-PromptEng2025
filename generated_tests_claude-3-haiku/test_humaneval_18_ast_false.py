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

def test_how_many_times_empty_string():
    assert how_many_times("", "") == 0
    assert how_many_times("", "test") == 0

def test_how_many_times_single_character():
    assert how_many_times("a", "a") == 1
    assert how_many_times("abc", "a") == 1
    assert how_many_times("abc", "b") == 1
    assert how_many_times("abc", "c") == 1

def test_how_many_times_multiple_occurrences():
    assert how_many_times("aaa", "a") == 3
    assert how_many_times("abcabcabc", "abc") == 3
    assert how_many_times("ababab", "ab") == 3

def test_how_many_times_no_occurrences():
    assert how_many_times("abc", "x") == 0
    assert how_many_times("hello", "world") == 0

@pytest.mark.parametrize("string,substring,expected", [
    ("", "test", 0),
    ("a", "a", 1),
    ("abc", "a", 1),
    ("aaa", "a", 3),
    ("abcabcabc", "abc", 3),
    ("ababab", "ab", 3),
    ("abc", "x", 0),
    ("hello", "world", 0)
])
def test_how_many_times_parametrized(string, substring, expected):
    assert how_many_times(string, substring) == expected

def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times