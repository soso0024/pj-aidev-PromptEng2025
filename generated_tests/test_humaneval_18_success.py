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
    ("hello world", "o", 2),
    ("banana", "ana", 2),
    ("aaaaa", "aa", 4),
    ("test string", "string", 1),
    ("", "", 1),
    ("abc", "", 4),
    ("hello", "xyz", 0),
    ("  ", " ", 2),
    ("aaa", "aaaa", 0),
    ("Mississippi", "issi", 2),
    ("Python Programming", "m", 2),
    ("🌟✨🌟", "🌟", 2)
])
def test_parametrized_cases(string, substring, expected):
    assert how_many_times(string, substring) == expected

def test_case_sensitivity():
    assert how_many_times("Hello HELLO", "hello") == 0
    assert how_many_times("HELLO", "HELLO") == 1
    assert how_many_times("hello", "HELLO") == 0

def test_special_characters():
    assert how_many_times("$$$$", "$$") == 3
    assert how_many_times("\n\n\n", "\n") == 3
    assert how_many_times("\t\t", "\t") == 2

def test_overlapping_substrings():
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("abababab", "abab") == 3

@pytest.mark.parametrize("invalid_input", [
    None,
    123
])
def test_invalid_input_types(invalid_input):
    with pytest.raises(TypeError):
        how_many_times(invalid_input, "test")
    with pytest.raises(TypeError):
        how_many_times("test", invalid_input)

def test_empty_inputs():
    assert how_many_times("", "test") == 0
    assert how_many_times("test", "") == 5
    assert how_many_times("", "") == 1

def test_unicode_strings():
    assert how_many_times("über über", "über") == 2
    assert how_many_times("你好你好", "你好") == 2
    assert how_many_times("🐍🐍🐍", "🐍") == 3