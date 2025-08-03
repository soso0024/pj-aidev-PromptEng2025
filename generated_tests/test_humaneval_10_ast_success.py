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

@pytest.mark.parametrize("input_str,expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "aba"),
    ("abc", "abcba"),
    ("racecar", "racecar"),
    ("python", "pythonohtyp"),
    ("hello", "hellolleh"),
    ("x", "x"),
    ("aaa", "aaa"),
    ("abcd", "abcdcba"),
    ("xyxy", "xyxyx"),
    ("12321", "12321"),
    ("12345", "123454321"),
])
def test_make_palindrome(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_result_is_palindrome():
    test_strings = ["hello", "python", "test", "algorithm", "code"]
    for s in test_strings:
        result = make_palindrome(s)
        assert is_palindrome(result)

def test_original_string_preserved():
    test_strings = ["hello", "python", "test"]
    for s in test_strings:
        result = make_palindrome(s)
        assert result.startswith(s)

def test_empty_string():
    assert make_palindrome("") == ""

def test_single_character():
    assert make_palindrome("x") == "x"

def test_already_palindrome():
    palindromes = ["racecar", "madam", "noon", "level"]
    for p in palindromes:
        assert make_palindrome(p) == p

@pytest.mark.parametrize("input_str", [
    "!@#",
    "123",
    "   ",
    "\n\t",
    "a b c",
    ".,;",
])
def test_special_characters(input_str):
    result = make_palindrome(input_str)
    assert is_palindrome(result)
    assert result.startswith(input_str)