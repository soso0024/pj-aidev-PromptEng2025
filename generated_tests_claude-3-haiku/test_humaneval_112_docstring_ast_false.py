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
from your_module import reverse_delete
import pytest

@pytest.mark.parametrize("s,c,expected_result,expected_is_palindrome", [
    ("abcde", "ae", "bcd", False),
    ("abcdef", "b", "acdef", False),
    ("abcdedcba", "ab", "cdedc", True),
    ("", "a", "", False),
    ("hello", "l", "heo", False),
    ("racecar", "r", "aceac", True),
    ("A man, a plan, a canal: Panama", "amanaplanacanalpanama", "", True),
    ("Was it a car or a cat I saw?", "wasitacaroracatisaw", "", True),
])
def test_reverse_delete(s, c, expected_result, expected_is_palindrome):
    result, is_palindrome = reverse_delete(s, c)
    assert result == expected_result
    assert is_palindrome == expected_is_palindrome

def test_reverse_delete_empty_input():
    assert reverse_delete("", "") == ("", True)

def test_reverse_delete_all_characters_removed():
    assert reverse_delete("hello", "hello") == ("", True)

def test_reverse_delete_invalid_input():
    with pytest.raises(TypeError):
        reverse_delete(123, "abc")
    with pytest.raises(TypeError):
        reverse_delete("abc", 123)