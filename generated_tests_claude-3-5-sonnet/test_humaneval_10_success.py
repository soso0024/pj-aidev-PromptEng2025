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
    ("hello", "hellolleh"),
    ("x", "x"),
    ("aabb", "aabbaa"),
    ("python", "pythonohtyp"),
    ("aaaaa", "aaaaa"),
    ("12321", "12321"),
    ("abcd", "abcdcba"),
    ("test", "testset"),
    ("   ", "   "),
    ("!@#", "!@#@!"),
])
def test_make_palindrome(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_result_is_palindrome():
    test_strings = ["hello", "python", "test", "12345", "abc", ""]
    for s in test_strings:
        result = make_palindrome(s)
        assert is_palindrome(result)

def test_original_string_preserved():
    test_strings = ["hello", "python", "test", "12345", "abc"]
    for s in test_strings:
        result = make_palindrome(s)
        assert result.startswith(s)

def test_minimal_addition():
    test_string = "abc"
    result = make_palindrome(test_string)
    assert len(result) <= 2 * len(test_string)

def test_already_palindrome():
    palindromes = ["racecar", "noon", "level", "a", ""]
    for p in palindromes:
        assert make_palindrome(p) == p

def test_special_characters():
    assert make_palindrome("!@#$%") == "!@#$%$#@!"
    assert make_palindrome("12!@") == "12!@!21"

def test_with_spaces():
    assert make_palindrome("a b c") == "a b c b a"
    assert make_palindrome("  ") == "  "

def test_single_character_strings():
    for c in "abcdefghijklmnopqrstuvwxyz0123456789":
        assert make_palindrome(c) == c