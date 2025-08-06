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

def test_empty_string():
    assert how_many_times("", "a") == 0

def test_empty_substring():
    assert how_many_times("abc", "") == 4

def test_single_char():
    assert how_many_times("aaa", "a") == 3

def test_overlapping_substring():
    assert how_many_times("aaaa", "aa") == 3

def test_no_match():
    assert how_many_times("abc", "d") == 0

@pytest.mark.parametrize("string,substring,expected", [
    ("hello", "l", 2),
    ("banana", "ana", 2),
    ("aaaaa", "aa", 4),
    ("test", "test", 1),
    ("abcabc", "abc", 2),
    ("   ", " ", 3),
    ("aaa", "aaaa", 0),
    ("mississippi", "issi", 2),
    ("", "", 1),
    ("abc", "abc", 1),
    ("aaa", "aa", 2)
])
def test_various_cases(string, substring, expected):
    assert how_many_times(string, substring) == expected

@pytest.mark.parametrize("string,substring", [
    (None, "test"),
    ("test", None),
    (123, "test"),
    ("test", 123)
])
def test_invalid_inputs(string, substring):
    with pytest.raises(TypeError):
        how_many_times(string, substring)

def test_special_characters():
    assert how_many_times("$#$#$", "$#") == 2
    assert how_many_times("\n\n\n", "\n") == 3
    assert how_many_times("\t\t", "\t") == 2

def test_unicode_characters():
    assert how_many_times("🌟🌟🌟", "🌟") == 3
    assert how_many_times("é€£", "€") == 1