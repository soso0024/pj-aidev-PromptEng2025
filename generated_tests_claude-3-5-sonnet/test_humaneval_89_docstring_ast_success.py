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

def test_basic_encryption():
    assert encrypt("hi") == "lm"
    assert encrypt("asdfghjkl") == "ewhjklnop"
    assert encrypt("gf") == "kj"
    assert encrypt("et") == "ix"

@pytest.mark.parametrize("input_str,expected", [
    ("abc", "efg"),
    ("xyz", "bcd"),
    ("", ""),
    ("hello", "lipps"),
    ("z", "d"),
    ("a", "e")
])
def test_encrypt_parametrized(input_str, expected):
    assert encrypt(input_str) == expected

@pytest.mark.parametrize("input_str,expected", [
    ("ABC", "ABC"),
    ("123", "123"),
    ("!@#", "!@#"),
    ("Hi There!", "Hm Tlivi!"),
    ("mix123up", "qmb123yt"),
    ("a b c", "e f g")
])
def test_encrypt_special_cases(input_str, expected):
    assert encrypt(input_str) == expected

def test_long_string():
    input_str = "abcdefghijklmnopqrstuvwxyz"
    expected = "efghijklmnopqrstuvwxyzabcd"
    assert encrypt(input_str) == expected

def test_repeated_characters():
    assert encrypt("aaa") == "eee"
    assert encrypt("zzz") == "ddd"

def test_mixed_case():
    assert encrypt("aBcD") == "eBgD"

def test_spaces_and_punctuation():
    assert encrypt("hello, world!") == "lipps, asvph!"
    assert encrypt("test.test") == "xiwx.xiwx"

def test_unicode_characters():
    assert encrypt("héllo") == "lépps"
    assert encrypt("über") == "üfiv"