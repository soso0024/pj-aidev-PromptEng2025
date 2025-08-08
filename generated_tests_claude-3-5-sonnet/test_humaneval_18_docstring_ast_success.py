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
    assert how_many_times("abc", "") == len("abc") + 1

def test_single_char():
    assert how_many_times("aaa", "a") == 3

def test_overlapping_substring():
    assert how_many_times("aaaa", "aa") == 3

@pytest.mark.parametrize("string,substring,expected", [
    ("hello", "l", 2),
    ("banana", "ana", 2),
    ("aaaaa", "aa", 4),
    ("test", "xyz", 0),
    ("mississippi", "issi", 2),
    ("   ", " ", 3),
    ("aaa", "aaaa", 0),
    ("абвгд", "аб", 1),
    ("abc", "abc", 1),
    ("🌟🌟🌟", "🌟", 3),
    ("hello world", "o w", 1),
])
def test_various_cases(string, substring, expected):
    assert how_many_times(string, substring) == expected

def test_empty_strings():
    assert how_many_times("", "") == 1

def test_type_error():
    with pytest.raises(TypeError):
        how_many_times(None, "a")
    with pytest.raises(TypeError):
        how_many_times("abc", None)
    with pytest.raises(TypeError):
        how_many_times(123, "a")
    with pytest.raises(TypeError):
        how_many_times("abc", 123)