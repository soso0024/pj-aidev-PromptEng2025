# Test cases for HumanEval/112
# Generated using Claude API


def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """

    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)


# Generated test cases:
import pytest

def reverse_delete(s,c):
    s = ''.join([char for char in s if char not in [x.lower() for x in c]])
    return (s, s[::-1] == s)

def test_reverse_delete_basic_cases():
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)

def test_reverse_delete_empty_strings():
    assert reverse_delete("", "") == ('', True)
    assert reverse_delete("abc", "") == ('abc', False)
    assert reverse_delete("", "abc") == ('', True)

def test_reverse_delete_no_deletion():
    assert reverse_delete("hello", "x") == ('hello', False)

def test_reverse_delete_full_deletion():
    assert reverse_delete("abcde", "abcde") == ('', True)

def test_reverse_delete_palindrome_cases():
    assert reverse_delete("racecar", "x") == ('racecar', True)
    assert reverse_delete("radar", "d") == ('raar', True)

def test_reverse_delete_case_sensitivity():
    assert reverse_delete("AbCdE", "ac") == ('bDE', False)

@pytest.mark.parametrize("s,c,expected", [
    ("hello", "l", ('heo', False)),
    ("python", "p", ('ython', False)),
    ("level", "e", ('lvl', True)),
    ("programming", "og", ('prammin', False))
])
def test_reverse_delete_parametrized(s, c, expected):
    assert reverse_delete(s, c) == expected