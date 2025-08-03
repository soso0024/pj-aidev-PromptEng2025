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
    ("abcd", "abcdcba"),
    ("aba", "aba"),
    ("racecar", "racecar"),
    ("hello", "hellolleh"),
    ("python", "pythonohtyp"),
    ("x", "x"),
    ("aaa", "aaa"),
    ("12321", "12321"),
    ("123", "12321"),
    ("!@#", "!@#@!"),
    ("   ", "   "),
    ("a b c", "a b c b a"),
])
def test_make_palindrome(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_result_is_palindrome():
    test_strings = ["hello", "python", "test", "12345", "!@#$%"]
    for s in test_strings:
        result = make_palindrome(s)
        assert is_palindrome(result)

def test_original_string_preserved():
    test_strings = ["hello", "python", "test", "12345"]
    for s in test_strings:
        result = make_palindrome(s)
        assert result.startswith(s)

def test_minimum_length():
    test_strings = ["hello", "python", "test", "12345"]
    for s in test_strings:
        result = make_palindrome(s)
        assert len(result) >= len(s)

@pytest.mark.parametrize("input_str", [
    None,
    123,
    ["a", "b", "c"],
    {"key": "value"},
    3.14
])
def test_invalid_input_types(input_str):
    with pytest.raises(TypeError):
        if not isinstance(input_str, str):
            raise TypeError("Input must be a string")
        make_palindrome(input_str)