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
    assert how_many_times('', 'a') == 0
    assert how_many_times('', '') == 0

def test_how_many_times_single_char():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('hello', 'l') == 2

def test_how_many_times_multiple_chars():
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abababab', 'ab') == 4

def test_how_many_times_no_match():
    assert how_many_times('hello', 'x') == 0

@pytest.mark.parametrize("string,substring,expected", [
    ('', 'a', 0),
    ('aaa', 'a', 3),
    ('aaaa', 'aa', 3),
    ('abababab', 'ab', 4),
    ('hello', 'l', 2),
    ('hello', 'x', 0),
    ('mississippi', 'iss', 2)
])
def test_how_many_times_parametrized(string, substring, expected):
    assert how_many_times(string, substring) == expected

def test_how_many_times_case_sensitive():
    assert how_many_times('Hello', 'h') == 0
    assert how_many_times('Hello', 'H') == 1

def test_how_many_times_empty_substring():
    assert how_many_times('hello', '') == 0