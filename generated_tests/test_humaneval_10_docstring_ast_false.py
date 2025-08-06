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

def test_make_palindrome_empty_string():
    assert make_palindrome("") == ""

def test_make_palindrome_single_char():
    assert make_palindrome("a") == "a"

@pytest.mark.parametrize("input_str,expected", [
    ("cat", "catac"),
    ("cata", "catac"),
    ("xyz", "xyzyx"),
    ("racecar", "racecar"),
    ("python", "pythonohtyp"),
    ("a", "a"),
    ("aa", "aa"),
    ("aaa", "aaa"),
    ("ab", "aba"),
])
def test_make_palindrome_various_inputs(input_str, expected):
    assert make_palindrome(input_str) == expected

def test_make_palindrome_already_palindrome():
    palindromes = ["racecar", "madam", "noon", "level", "deed"]
    for palindrome in palindromes:
        assert make_palindrome(palindrome) == palindrome

def test_make_palindrome_special_chars():
    assert make_palindrome("!@#") == "!@#@!"

def test_make_palindrome_with_spaces():
    assert make_palindrome("hello ") == "hello olleh"

def test_make_palindrome_numbers_as_strings():
    assert make_palindrome("123") == "12321"

def test_make_palindrome_mixed_case():
    assert make_palindrome("AbC") == "AbCbA"

@pytest.mark.parametrize("input_str", [
    "   ",
    "\t\n",
    "\r\n",
    "  hello  ",
])
def test_make_palindrome_whitespace(input_str):
    result = make_palindrome(input_str)
    assert result == result[::-1]
    assert result.startswith(input_str)

def test_make_palindrome_unicode():
    assert make_palindrome("🌟") == "🌟"
    assert make_palindrome("🌟✨") == "🌟✨🌟"

@pytest.mark.parametrize("input_str", [
    None,
    123,
    ["a", "b", "c"],
    {"key": "value"},
    3.14
])
def test_make_palindrome_invalid_inputs(input_str):
    try:
        make_palindrome(input_str)
        pytest.fail(f"Expected TypeError for input: {input_str}")
    except (TypeError, AttributeError):
        pass