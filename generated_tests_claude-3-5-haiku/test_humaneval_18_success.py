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
    if not substring:
        return 0

    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times

def test_how_many_times_basic_substring():
    assert how_many_times("hello hello world", "hello") == 2

def test_how_many_times_no_substring():
    assert how_many_times("world", "hello") == 0

def test_how_many_times_empty_string():
    assert how_many_times("", "test") == 0

def test_how_many_times_empty_substring():
    assert how_many_times("hello", "") == 0

def test_how_many_times_overlapping_substrings():
    assert how_many_times("aaaaa", "aa") == 4

def test_how_many_times_case_sensitive():
    assert how_many_times("Hello HELLO hello", "hello") == 1

def test_how_many_times_single_character():
    assert how_many_times("mississippi", "i") == 4

@pytest.mark.parametrize("string,substring,expected", [
    ("hello world", "o w", 1),
    ("banana", "ana", 2),
    ("programming", "mm", 1),
    ("test test test", "test", 3),
    ("", "", 0)
])
def test_how_many_times_parametrized(string, substring, expected):
    assert how_many_times(string, substring) == expected