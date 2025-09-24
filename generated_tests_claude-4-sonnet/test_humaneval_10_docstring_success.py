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

class TestIsPalindrome:
    @pytest.mark.parametrize("input_str,expected", [
        ("", True),
        ("a", True),
        ("aa", True),
        ("aba", True),
        ("abba", True),
        ("racecar", True),
        ("madam", True),
        ("ab", False),
        ("abc", False),
        ("abcd", False),
        ("hello", False),
        ("A", True),
        ("Aa", False),
        ("121", True),
        ("123", False),
        ("12321", True),
        (" ", True),
        ("  ", True),
        ("a a", True),
        ("a b", False),
        ("!@#@!", True),
        ("!@#$", False)
    ])
    def test_is_palindrome(self, input_str, expected):
        assert is_palindrome(input_str) == expected

class TestMakePalindrome:
    @pytest.mark.parametrize("input_str,expected", [
        ("", ""),
        ("a", "a"),
        ("ab", "aba"),
        ("abc", "abcba"),
        ("cat", "catac"),
        ("cata", "catac"),
        ("abcd", "abcdcba"),
        ("race", "racecar"),
        ("x", "x"),
        ("xy", "xyx"),
        ("xyz", "xyzyx"),
        ("abcde", "abcdedcba"),
        ("racecar", "racecar"),
        ("madam", "madam"),
        ("aba", "aba"),
        ("abba", "abba"),
        ("12", "121"),
        ("123", "12321"),
        ("1234", "1234321"),
        ("aa", "aa"),
        ("aaa", "aaa"),
        ("aab", "aabaa"),
        ("aabc", "aabcbaa"),
        ("!", "!"),
        ("!@", "!@!"),
        ("!@#", "!@#@!"),
        (" ", " "),
        ("  ", "  "),
        (" a", " a "),
        ("a ", "a a")
    ])
    def test_make_palindrome(self, input_str, expected):
        result = make_palindrome(input_str)
        assert result == expected
        assert is_palindrome(result)
        assert result.startswith(input_str)

    def test_make_palindrome_properties(self):
        test_strings = ["", "a", "ab", "abc", "abcd", "hello", "world", "test", "python"]
        for s in test_strings:
            result = make_palindrome(s)
            assert is_palindrome(result)
            assert result.startswith(s)
            if s:
                assert len(result) >= len(s)

    def test_make_palindrome_already_palindrome(self):
        palindromes = ["", "a", "aa", "aba", "abba", "racecar", "madam", "12321"]
        for p in palindromes:
            assert make_palindrome(p) == p

    def test_make_palindrome_minimal_length(self):
        test_cases = [
            ("ab", "aba"),
            ("abc", "abcba"),
            ("abcd", "abcdcba")
        ]
        for input_str, expected in test_cases:
            result = make_palindrome(input_str)
            assert len(result) == len(expected)