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
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)

def test_reverse_delete_example_1():
    assert reverse_delete("abcde", "ae") == ("bcd", False)

def test_reverse_delete_example_2():
    assert reverse_delete("abcdef", "b") == ("acdef", False)

def test_reverse_delete_example_3():
    assert reverse_delete("abcdedcba", "ab") == ("cdedc", True)

def test_reverse_delete_empty_string():
    assert reverse_delete("", "abc") == ("", True)

def test_reverse_delete_empty_chars_to_delete():
    assert reverse_delete("abcde", "") == ("abcde", False)

def test_reverse_delete_both_empty():
    assert reverse_delete("", "") == ("", True)

def test_reverse_delete_all_chars_deleted():
    assert reverse_delete("abc", "abc") == ("", True)

def test_reverse_delete_no_chars_deleted():
    assert reverse_delete("xyz", "abc") == ("xyz", False)

def test_reverse_delete_single_char_palindrome():
    assert reverse_delete("abcba", "bc") == ("aa", True)

def test_reverse_delete_single_char_result():
    assert reverse_delete("abcde", "abde") == ("c", True)

def test_reverse_delete_palindrome_result():
    assert reverse_delete("racecar", "x") == ("racecar", True)

def test_reverse_delete_duplicate_chars_in_c():
    assert reverse_delete("hello", "ll") == ("heo", False)

def test_reverse_delete_repeated_chars():
    assert reverse_delete("aabbcc", "ac") == ("bb", True)

def test_reverse_delete_long_palindrome():
    assert reverse_delete("abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba", "xyz") == ("abcdefghijklmnopqrstuvwwvutsrqponmlkjihgfedcba", True)

@pytest.mark.parametrize("s,c,expected", [
    ("a", "a", ("", True)),
    ("a", "b", ("a", True)),
    ("aa", "a", ("", True)),
    ("ab", "a", ("b", True)),
    ("aba", "b", ("aa", True)),
    ("abba", "a", ("bb", True)),
    ("abcba", "c", ("abba", True)),
    ("hello world", "l", ("heo word", False)),
    ("madam", "m", ("ada", True)),
    ("12321", "2", ("131", True))
])
def test_reverse_delete_parametrized(s, c, expected):
    assert reverse_delete(s, c) == expected