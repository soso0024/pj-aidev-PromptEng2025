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

def make_palindrome(string: str) -> str:
    if not string:
        return ""
    if string == string[::-1]:
        return string
    
    min_palindrome = string + string[::-1]
    for i in range(len(string)):
        test_str = string + string[i::-1]
        if test_str == test_str[::-1] and len(test_str) < len(min_palindrome):
            min_palindrome = test_str
    return min_palindrome

def test_make_palindrome_empty_string():
    assert make_palindrome("") == ""

def test_make_palindrome_single_char():
    assert make_palindrome("a") == "a"

@pytest.mark.parametrize("input_str,expected", [
    ("cat", "catac"),
    ("cata", "catac"),
    ("hello", "helloolleh"),
    ("racecar", "racecar"),
    ("abcd", "abcdcba"),
    ("xyz", "xyzyx"),
])
def test_make_palindrome_normal_cases(input_str, expected):
    assert make_palindrome(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "aba",
    "aa",
    "bb",
    "deed",
    "noon",
])
def test_make_palindrome_already_palindrome(input_str):
    assert make_palindrome(input_str) == input_str

def test_make_palindrome_special_chars():
    assert make_palindrome("!@#") == "!@##@!"

def test_make_palindrome_with_spaces():
    assert make_palindrome("hello world") == "hello worldlrow olleh"

@pytest.mark.parametrize("input_str,expected", [
    ("12345", "1234554321"),
    ("123321", "123321"),
    ("12321", "12321"),
])
def test_make_palindrome_numbers_as_strings(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_make_palindrome_mixed_case():
    assert make_palindrome("AbC") == "AbCbA"

def test_make_palindrome_unicode():
    assert make_palindrome("café") == "caféfac"

@pytest.mark.parametrize("input_str", [
    "   ",
    "\t\n",
    "\r\n",
])
def test_make_palindrome_whitespace(input_str):
    result = make_palindrome(input_str)
    assert result == result[::-1]
    assert result.startswith(input_str)