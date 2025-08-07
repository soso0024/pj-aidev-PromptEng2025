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

def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

def test_make_palindrome_empty_string():
    assert make_palindrome('') == ''

def test_make_palindrome_single_char():
    assert make_palindrome('a') == 'a'

def test_make_palindrome_already_palindrome():
    assert make_palindrome('racecar') == 'racecar'

def test_make_palindrome_simple_case():
    assert make_palindrome('race') == 'racecar'

def test_make_palindrome_complex_case():
    assert make_palindrome('abcde') == 'abcdedcba'

@pytest.mark.parametrize("input_str,expected", [
    ('', ''),
    ('a', 'a'),
    ('ab', 'aba'),
    ('abc', 'abcba'),
    ('race', 'racecar'),
    ('hello', 'hellolleh')
])
def test_make_palindrome_parametrized(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_make_palindrome_unicode():
    assert make_palindrome('こんにちは') == 'こんにちははちにんこ'

def test_make_palindrome_mixed_chars():
    assert make_palindrome('123abc') == '123abcba321'