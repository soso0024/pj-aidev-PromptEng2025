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
    ("abba", "abba"),
    ("12321", "12321"),
    ("123", "12321"),
    ("xyyx", "xyyx"),
    ("abcd", "abcdcba"),
])
def test_make_palindrome(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_result_is_palindrome():
    test_strings = ["python", "algorithm", "test", "programming"]
    for s in test_strings:
        result = make_palindrome(s)
        assert is_palindrome(result)

def test_original_string_preserved():
    test_string = "hello"
    result = make_palindrome(test_string)
    assert result.startswith(test_string)

def test_empty_string():
    assert make_palindrome("") == ""

def test_single_character():
    assert make_palindrome("x") == "x"

def test_already_palindrome():
    palindromes = ["racecar", "deed", "noon", "level"]
    for p in palindromes:
        assert make_palindrome(p) == p

def test_type_error():
    with pytest.raises(TypeError):
        make_palindrome(None)

def test_type_error_non_string():
    with pytest.raises(TypeError):
        make_palindrome(123)