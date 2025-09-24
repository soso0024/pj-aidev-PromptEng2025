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

def reverse_delete(s, c):
    s = ''.join([char for char in s if char not in c])
    return (s, s == s[::-1])

def test_reverse_delete_empty_strings():
    assert reverse_delete('', '') == ('', True)
    assert reverse_delete('', 'abc') == ('', True)

def test_reverse_delete_no_match():
    assert reverse_delete('abcde', 'xyz') == ('abcde', False)
    assert reverse_delete('hello', 'world') == ('hello', False)

@pytest.mark.parametrize("s,c,expected", [
    ("abcde", "ae", ('bcd', False)),
    ("abcdef", "b", ('acdef', False)),
    ("abcdedcba", "ab", ('cdedc', True)),
    ("racecar", "r", ('aceac', True)),
    ("A man a plan a canal Panama", "aaa", (' mn a plan a canal Panama', False))
])
def test_reverse_delete_examples(s, c, expected):
    assert reverse_delete(s, c) == expected

def test_reverse_delete_all_characters_removed():
    assert reverse_delete('abc', 'abc') == ('', True)
    assert reverse_delete('hello world', 'hello world') == ('', True)

def test_reverse_delete_case_insensitive():
    assert reverse_delete('AbCdE', 'aE') == ('bCd', False)
    assert reverse_delete('rAcEcAr', 'Rr') == ('AcAc', True)