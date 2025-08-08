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
    if not c:
        raise ValueError("Character to delete cannot be empty")
    s = ''.join([char for char in s if char not in c])
    return (s, s[::-1] == s)

def test_reverse_delete_empty_string():
    assert reverse_delete("", "a") == ("", True)

def test_reverse_delete_no_matching_chars():
    assert reverse_delete("hello", "x") == ("hello", False)

def test_reverse_delete_all_matching_chars():
    assert reverse_delete("aabbcc", "abc") == ("", True)

@pytest.mark.parametrize("input_str,char,expected_str,expected_result", [
    ("Hello World", "l", "Heo Word", False),
    ("Python is awesome", "n", "Pyto is awesome", False),
    ("Reverse this string", "e", "Rvrs ths string", False),
    ("Remove all A's", "A", "Remov ll 's", False),
    ("Keep everything", "", "Keep everything", True)
])
def test_reverse_delete_various_inputs(input_str, char, expected_str, expected_result):
    assert reverse_delete(input_str, char) == (expected_str, expected_result)