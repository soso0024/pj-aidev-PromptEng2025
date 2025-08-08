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
from reverse_delete import reverse_delete
import pytest

@pytest.mark.parametrize("s,c,expected_result,expected_is_palindrome", [
    ("abcde", "ae", "bcd", False),
    ("abcdef", "b", "acdef", False),
    ("abcdedcba", "ab", "cdedc", True),
    ("", "a", "", True),
    ("abab", "ab", "", True),
    ("abcabc", "abc", "", True),
    ("a", "a", "", True),
    ("abcdefghijklmnopqrstuvwxyz", "a", "bcdefghijklmnopqrstuvwxyz", False),
    ("Hello, World!", "Hd", "ello, Worl", False),
    ("Madam, I'm Adam", "Mda", "am, I'm a", True)
])
def test_reverse_delete(s, c, expected_result, expected_is_palindrome):
    result, is_palindrome = reverse_delete(s, c)
    assert result == expected_result
    assert is_palindrome == expected_is_palindrome