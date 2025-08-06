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

def test_reverse_delete_basic():
    assert reverse_delete("hello", "l") == ("heo", False)
    assert reverse_delete("abba", "b") == ("aa", True)

def test_reverse_delete_empty():
    assert reverse_delete("", "") == ("", True)
    assert reverse_delete("", "abc") == ("", True)

def test_reverse_delete_no_chars_to_remove():
    assert reverse_delete("hello", "") == ("hello", False)
    assert reverse_delete("radar", "x") == ("radar", True)

@pytest.mark.parametrize("input_str, chars_to_remove, expected", [
    ("hello world", " ", ("helloworld", False)),
    ("madam", "d", ("maam", True)),
    ("python", "python", ("", True)),
    ("aaa", "a", ("", True)),
    ("abcba", "ac", ("bb", True)),
    ("12321", "1", ("232", True)),
    ("test", "set", ("", True)),
    ("abcdef", "xyz", ("abcdef", False))
])
def test_reverse_delete_parametrized(input_str, chars_to_remove, expected):
    assert reverse_delete(input_str, chars_to_remove) == expected

def test_reverse_delete_special_chars():
    assert reverse_delete("!@#$%", "#%") == ("!@$", False)
    assert reverse_delete("a!a", "!") == ("aa", True)

def test_reverse_delete_numbers():
    assert reverse_delete("123321", "2") == ("1331", True)
    assert reverse_delete("12321", "2") == ("131", True)

def test_reverse_delete_case_sensitive():
    assert reverse_delete("AbBaA", "b") == ("ABaA", False)
    assert reverse_delete("AbBaA", "B") == ("AbaA", False)

def test_reverse_delete_multiple_chars():
    assert reverse_delete("hello world", "ol ") == ("hewrd", False)
    assert reverse_delete("abracadabra", "abc") == ("rdr", True)

def test_reverse_delete_all_same_chars():
    assert reverse_delete("aaaaa", "b") == ("aaaaa", True)
    assert reverse_delete("aaaaa", "a") == ("", True)

def test_reverse_delete_unicode():
    assert reverse_delete("héllò", "l") == ("héò", False)
    assert reverse_delete("αββα", "β") == ("αα", True)