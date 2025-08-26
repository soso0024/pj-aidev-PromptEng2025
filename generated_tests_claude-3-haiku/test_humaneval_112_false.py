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
from solution import reverse_delete
import pytest

def test_reverse_delete_normal_case():
    assert reverse_delete("Hello World", "l") == ("Heo Word", True)
    assert reverse_delete("Python is awesome", "on") == ("Pythi awesewe", True)

def test_reverse_delete_empty_string():
    assert reverse_delete("", "a") == ("", True)

def test_reverse_delete_no_matching_chars():
    assert reverse_delete("Hello", "x") == ("Hello", False)

@pytest.mark.parametrize("input_str,chars,expected_str,is_palindrome", [
    ("A man, a plan, a canal: Panama", "aon", "A mn  lnPnm", True),
    ("race a car", "r", "ae a ca", False),
    ("Was it a car or a cat I saw?", "aou", "Ws t a r r a ct I s?", True)
])
def test_reverse_delete_parametrized(input_str, chars, expected_str, is_palindrome):
    assert reverse_delete(input_str, chars) == (expected_str, is_palindrome)

def test_reverse_delete_invalid_input():
    with pytest.raises(TypeError):
        reverse_delete(123, "a")
    with pytest.raises(TypeError):
        reverse_delete("hello", 123)