# Test cases for HumanEval/10
# Generated using Claude API



def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """

    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]


# Generated test cases:
import pytest
from typing import Optional

def test_make_palindrome_empty_string():
    assert make_palindrome("") == ""

def test_make_palindrome_single_char():
    assert make_palindrome("a") == "a"

@pytest.mark.parametrize("input_str,expected", [
    ("cat", "catac"),
    ("cata", "catac"),
    ("hello", "hellolleh"),
    ("racecar", "racecar"),
    ("abcd", "abcdcba"),
    ("xyz", "xyzyx"),
    ("level", "level"),
    ("12345", "123454321"),
])
def test_make_palindrome_various_inputs(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_make_palindrome_already_palindrome():
    assert make_palindrome("radar") == "radar"
    assert make_palindrome("noon") == "noon"

@pytest.mark.parametrize("input_str,expected", [
    ("A", "A"),
    ("AA", "AA"),
    ("AAA", "AAA"),
    ("aaa", "aaa"),
])
def test_make_palindrome_repeated_chars(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_make_palindrome_special_chars():
    assert make_palindrome("!@#") == "!@#@!"
    assert make_palindrome(".,;") == ".,;,."

def test_make_palindrome_with_spaces():
    assert make_palindrome("hello world") == "hello worldlrow olleh"
    assert make_palindrome("   ") == "   "

def test_make_palindrome_unicode():
    assert make_palindrome("😊") == "😊"
    assert make_palindrome("😊👋") == "😊👋😊"

def test_make_palindrome_mixed_case():
    assert make_palindrome("AbC") == "AbCbA"
    assert make_palindrome("TeSt") == "TeStSeT"

def test_make_palindrome_numbers():
    assert make_palindrome("123") == "12321"
    assert make_palindrome("999") == "999"

def test_make_palindrome_alphanumeric():
    assert make_palindrome("abc123") == "abc12321cba"
    assert make_palindrome("1a2b3c") == "1a2b3c3b2a1"