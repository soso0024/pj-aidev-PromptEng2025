# Test cases for HumanEval/51
# Generated using Claude API



def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


# Generated test cases:
import pytest

def test_empty_string():
    assert remove_vowels("") == ""

def test_no_vowels():
    assert remove_vowels("bcd") == "bcd"

def test_all_vowels():
    assert remove_vowels("aeiou") == ""

def test_mixed_case():
    assert remove_vowels("aAeEiIoOuU") == ""

def test_with_spaces():
    assert remove_vowels("hello world") == "hll wrld"

def test_with_numbers():
    assert remove_vowels("h3ll0 w0rld") == "h3ll0 w0rld"

def test_with_special_chars():
    assert remove_vowels("hello!@#$%") == "hll!@#$%"

def test_with_newlines():
    assert remove_vowels("hello\nworld") == "hll\nwrld"

@pytest.mark.parametrize("input_str,expected", [
    ("", ""),
    ("hello", "hll"),
    ("HELLO", "HLL"),
    ("aeiou", ""),
    ("bcdfg", "bcdfg"),
    ("Hello World!", "Hll Wrld!"),
    ("a\nb\nc", "\nb\nc"),
    ("123", "123"),
    ("aAeEiIoOuU", ""),
    ("!@#$%", "!@#$%")
])
def test_remove_vowels_parametrized(input_str, expected):
    assert remove_vowels(input_str) == expected

def test_with_accented_chars():
    assert remove_vowels("héllo wörld") == "hll wrld"

def test_with_tabs():
    assert remove_vowels("hello\tworld") == "hll\twrld"

def test_single_char():
    assert remove_vowels("a") == ""
    assert remove_vowels("b") == "b"

def test_repeated_chars():
    assert remove_vowels("aaa") == ""
    assert remove_vowels("bbb") == "bbb"