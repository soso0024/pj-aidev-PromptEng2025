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

def test_basic_substring_count():
    assert how_many_times("hello", "l") == 2
    assert how_many_times("hello", "ll") == 1
    assert how_many_times("hello", "h") == 1

@pytest.mark.parametrize("string,substring,expected", [
    ("", "", 1),
    ("", "a", 0),
    ("a", "", 2),
    ("aaa", "aa", 2),
    ("banana", "ana", 2),
    ("test test test", "test", 3),
    ("overlapping", "lap", 1),
    ("mississippi", "issi", 2),
    ("abc", "xyz", 0),
    ("  spaces  ", " ", 4),
    ("hello\nworld", "\n", 1),
    ("special!@#", "!", 1),
    ("case SENSITIVE", "case", 1),
    ("case SENSITIVE", "CASE", 0),
])
def test_parametrized_cases(string, substring, expected):
    assert how_many_times(string, substring) == expected

def test_long_strings():
    long_string = "a" * 1000
    assert how_many_times(long_string, "aa") == 999
    assert how_many_times(long_string, "aaa") == 998

def test_edge_cases():
    assert how_many_times("a", "aa") == 0
    assert how_many_times("", "") == 1
    assert how_many_times("x", "") == 2

@pytest.mark.parametrize("string,substring", [
    (None, "test"),
    ("test", None),
    (123, "test"),
    ("test", 123),
])
def test_invalid_inputs(string, substring):
    with pytest.raises((TypeError, AttributeError)):
        how_many_times(string, substring)

def test_unicode_strings():
    assert how_many_times("🌟✨🌟", "🌟") == 2
    assert how_many_times("café", "é") == 1
    assert how_many_times("über", "ü") == 1