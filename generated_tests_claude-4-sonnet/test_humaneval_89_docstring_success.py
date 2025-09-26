# Test cases for HumanEval/89
# Generated using Claude API


def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out


# Generated test cases:
import pytest

def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out

@pytest.mark.parametrize("input_str,expected", [
    ("hi", "lm"),
    ("asdfghjkl", "ewhjklnop"),
    ("gf", "kj"),
    ("et", "ix"),
    ("", ""),
    ("a", "e"),
    ("z", "d"),
    ("xyz", "bcd"),
    ("abcdefghijklmnopqrstuvwxyz", "efghijklmnopqrstuvwxyzabcd"),
    ("Hello World!", "Hipps Wsvph!"),
    ("123", "123"),
    ("!@#$%", "!@#$%"),
    ("a1b2c3", "e1f2g3"),
    ("   ", "   "),
    ("test", "xiwx"),
    ("python", "tcxlsr"),
    ("HELLO", "HELLO"),
    ("MiXeD", "MmXiD"),
    ("special!@#characters", "wtigmep!@#glevegxivw"),
    ("single", "wmrkpi")
])
def test_encrypt_parametrized(input_str, expected):
    assert encrypt(input_str) == expected

def test_encrypt_empty_string():
    assert encrypt("") == ""

def test_encrypt_only_lowercase():
    assert encrypt("abcd") == "efgh"

def test_encrypt_with_numbers():
    assert encrypt("abc123def") == "efg123hij"

def test_encrypt_with_spaces():
    assert encrypt("a b c") == "e f g"

def test_encrypt_with_punctuation():
    assert encrypt("hello, world!") == "lipps, asvph!"

def test_encrypt_uppercase_unchanged():
    assert encrypt("ABC") == "ABC"

def test_encrypt_mixed_case():
    assert encrypt("AbC") == "AfC"

def test_encrypt_wrap_around():
    assert encrypt("xyz") == "bcd"
    assert encrypt("wxyz") == "abcd"

def test_encrypt_single_character():
    assert encrypt("a") == "e"
    assert encrypt("z") == "d"
    assert encrypt("m") == "q"

def test_encrypt_long_string():
    long_input = "abcdefghijklmnopqrstuvwxyz" * 3
    expected = "efghijklmnopqrstuvwxyzabcd" * 3
    assert encrypt(long_input) == expected

def test_encrypt_special_characters_only():
    assert encrypt("!@#$%^&*()") == "!@#$%^&*()"

def test_encrypt_newlines_and_tabs():
    assert encrypt("a\nb\tc") == "e\nf\tg"