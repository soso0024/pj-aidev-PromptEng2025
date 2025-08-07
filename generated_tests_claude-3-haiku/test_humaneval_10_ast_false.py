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

def test_make_palindrome_single_character():
    assert make_palindrome('a') == 'a'

def test_make_palindrome_even_length_palindrome():
    assert make_palindrome('abba') == 'abba'

def test_make_palindrome_odd_length_palindrome():
    assert make_palindrome('racecar') == 'racecar'

def test_make_palindrome_non_palindrome():
    assert make_palindrome('hello') == 'hellolleh'

@pytest.mark.parametrize("input,expected", [
    ('', ''),
    ('a', 'a'),
    ('abba', 'abba'),
    ('racecar', 'racecar'),
    ('hello', 'hellolleh'),
    ('python', 'pythonnotyhp'),
    ('madam', 'madammadam'),
    ('level', 'levellevel'),
])
def test_make_palindrome_parametrized(input, expected):
    assert make_palindrome(input) == expected