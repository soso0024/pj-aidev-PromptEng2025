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
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

def test_is_palindrome():
    assert is_palindrome('') == True
    assert is_palindrome('a') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man a plan a canal Panama') == False

def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('a') == 'a'
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    assert make_palindrome('race') == 'racecar'

@pytest.mark.parametrize("input_str,expected", [
    ('', ''),
    ('a', 'a'),
    ('cat', 'catac'),
    ('cata', 'catac'),
    ('race', 'racecar'),
    ('hello', 'helloolleh')
])
def test_make_palindrome_parametrized(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_make_palindrome_long_string():
    assert make_palindrome('abcdefg') == 'abcdefgfedcba'

def test_make_palindrome_already_palindrome():
    assert make_palindrome('racecar') == 'racecar'