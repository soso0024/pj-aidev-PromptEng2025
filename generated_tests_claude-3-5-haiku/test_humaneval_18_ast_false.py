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

def test_how_many_times_normal_cases():
    assert how_many_times("hello hello hello", "hello") == 3
    assert how_many_times("mississippi", "iss") == 2
    assert how_many_times("banana", "na") == 2

def test_how_many_times_edge_cases():
    assert how_many_times("", "") == 0
    assert how_many_times("hello", "") == 0
    assert how_many_times("", "test") == 0
    assert how_many_times("hello", "x") == 0

def test_how_many_times_overlapping():
    assert how_many_times("aaaaa", "aa") == 4

@pytest.mark.parametrize("string,substring,expected", [
    ("hello world", "o w", 1),
    ("python python python", "python", 3),
    ("abababab", "ab", 4),
    ("testtest", "test", 2),
    ("no match", "xyz", 0)
])
def test_how_many_times_parametrized(string, substring, expected):
    assert how_many_times(string, substring) == expected

def test_how_many_times_case_sensitive():
    assert how_many_times("Hello HELLO hello", "hello") == 1
    assert how_many_times("Hello HELLO hello", "Hello") == 1

def test_how_many_times_single_character():
    assert how_many_times("aaa", "a") == 3
    assert how_many_times("abcabcabc", "b") == 3

def test_how_many_times_long_substring():
    assert how_many_times("abcdefghijklmnop", "abcdefghijklmnop") == 1
    assert how_many_times("abcdefghijklmnopabcdefghijklmnop", "abcdefghijklmnop") == 2

def test_how_many_times_substring_longer_than_string():
    assert how_many_times("short", "longer substring") == 0