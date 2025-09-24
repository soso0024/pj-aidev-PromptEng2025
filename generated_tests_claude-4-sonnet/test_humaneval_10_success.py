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

def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

class TestMakePalindrome:
    
    def test_empty_string(self):
        assert make_palindrome("") == ""
    
    def test_single_character(self):
        assert make_palindrome("a") == "a"
    
    def test_already_palindrome_single_char(self):
        assert make_palindrome("x") == "x"
    
    def test_already_palindrome_multiple_chars(self):
        assert make_palindrome("aba") == "aba"
        assert make_palindrome("racecar") == "racecar"
        assert make_palindrome("madam") == "madam"
    
    def test_two_characters_different(self):
        assert make_palindrome("ab") == "aba"
    
    def test_two_characters_same(self):
        assert make_palindrome("aa") == "aa"
    
    def test_simple_cases(self):
        assert make_palindrome("abc") == "abcba"
        assert make_palindrome("cat") == "catac"
        assert make_palindrome("race") == "racecar"
    
    def test_longer_strings(self):
        assert make_palindrome("abcd") == "abcdcba"
        assert make_palindrome("hello") == "hellolleh"
    
    def test_partial_palindrome_suffix(self):
        assert make_palindrome("abcdc") == "abcdcba"
        assert make_palindrome("xyzyz") == "xyzyzyx"
    
    def test_numbers_as_string(self):
        assert make_palindrome("123") == "12321"
        assert make_palindrome("1234") == "1234321"
    
    def test_special_characters(self):
        assert make_palindrome("a!b") == "a!b!a"
        assert make_palindrome("@#$") == "@#$#@"
    
    def test_spaces(self):
        assert make_palindrome("a b") == "a b a"
        assert make_palindrome(" ") == " "
    
    def test_mixed_case(self):
        assert make_palindrome("Ab") == "AbA"
        assert make_palindrome("ABC") == "ABCBA"
    
    @pytest.mark.parametrize("input_str,expected", [
        ("a", "a"),
        ("ab", "aba"),
        ("abc", "abcba"),
        ("abcd", "abcdcba"),
        ("", ""),
        ("racecar", "racecar"),
        ("12321", "12321"),
        ("xyz", "xyzyx")
    ])
    def test_parametrized_cases(self, input_str, expected):
        assert make_palindrome(input_str) == expected