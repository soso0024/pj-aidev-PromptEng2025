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

def test_reverse_delete_normal_case():
    s = "Hello, World!"
    c = "l"
    expected_s = "Heo, Word!"
    expected_is_palindrome = False
    result = reverse_delete(s, c)
    assert result == (expected_s, expected_is_palindrome)

def test_reverse_delete_empty_string():
    s = ""
    c = "a"
    expected_s = ""
    expected_is_palindrome = True
    result = reverse_delete(s, c)
    assert result == (expected_s, expected_is_palindrome)

def test_reverse_delete_all_chars_removed():
    s = "aaa"
    c = "a"
    expected_s = ""
    expected_is_palindrome = True
    result = reverse_delete(s, c)
    assert result == (expected_s, expected_is_palindrome)

@pytest.mark.parametrize("s,c,expected_s,expected_is_palindrome", [
    ("A man, a plan, a canal: Panama", "aeiou", "mn, plan, canal: Panama", True),
    ("race a car", "r", "ae a ca", False),
    ("Was it a car or a cat I saw?", "t", "Was i a car or a ca I saw?", True)
])
def test_reverse_delete_parametrized(s, c, expected_s, expected_is_palindrome):
    result = reverse_delete(s, c)
    assert result == (expected_s, expected_is_palindrome)

def reverse_delete(s, c):
    s = ''.join([char for char in s if char not in c])
    return (s, s[::-1] == s)