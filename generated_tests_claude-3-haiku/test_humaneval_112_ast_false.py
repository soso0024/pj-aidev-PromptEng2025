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
    s = ''.join(char for char in s if char not in c)
    return (s, s == s[::-1])

def test_reverse_delete_empty_string():
    assert reverse_delete("", "a") == ("", True)

def test_reverse_delete_no_matching_chars():
    assert reverse_delete("hello", "x") == ("hello", False)

def test_reverse_delete_all_matching_chars():
    assert reverse_delete("aabbcc", "abc") == ("", True)

@pytest.mark.parametrize("input_str,chars,expected_str,expected_palindrome", [
    ("Hello World", "l", "Heo Word", True),
    ("Python is awesome", "on", "Pythi awe", True),
    ("A man a plan a canal Panama", "a", "mn  pln cnl Pnm", True),
    ("race car", "r", "ae a", True),
    ("Was it a car or a cat I saw?", "a", "Ws t  cr or  ct I sw?", True),
    ("Hello, World!", ",", "Hello World", False)
])
def test_reverse_delete_various_inputs(input_str, chars, expected_str, expected_palindrome):
    assert reverse_delete(input_str, chars) == (expected_str, expected_palindrome)

def test_reverse_delete_with_empty_chars():
    assert reverse_delete("Hello", "") == ("Hello", True)

def test_reverse_delete_with_none_input():
    with pytest.raises(TypeError):
        reverse_delete(None, "a")

def test_reverse_delete_with_none_chars():
    with pytest.raises(TypeError):
        reverse_delete("Hello", None)