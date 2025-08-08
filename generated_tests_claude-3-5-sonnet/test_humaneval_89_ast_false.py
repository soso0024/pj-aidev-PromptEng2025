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

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "lipps"),
    ("abcdef", "efghij"),
    ("xyz", "bcd"),
    ("", ""),
    ("a b c", "e f g"),
    ("HELLO", "HELLO"),
    ("Hello World!", "Lipps Asvph!"),
    ("123", "123"),
    ("z", "d"),
    ("aaa", "eee"),
    ("!@#$%", "!@#$%"),
    ("mix123up", "qmb123yt"),
    ("abcdefghijklmnopqrstuvwxyz", "efghijklmnopqrstuvwxyzabcd"),
    ("The Quick Brown Fox!", "Xli Uymgo Fvsar Jsb!"),
    ("  ", "  ")
])
def test_encrypt(input_str, expected):
    assert encrypt(input_str) == expected

def test_encrypt_empty_string():
    assert encrypt("") == ""

def test_encrypt_single_char():
    assert encrypt("a") == "e"
    assert encrypt("z") == "d"

def test_encrypt_special_chars():
    assert encrypt("!@#") == "!@#"
    assert encrypt(".,:") == ".,:"

def test_encrypt_mixed_case():
    assert encrypt("aBcD") == "eFgH"
    assert encrypt("Hello") == "Lipps"

def test_encrypt_spaces():
    assert encrypt("a b c") == "e f g"
    assert encrypt("   ") == "   "

def test_encrypt_numbers():
    assert encrypt("123abc") == "123efg"
    assert encrypt("a1b2c3") == "e1f2g3"

def test_encrypt_repeated_chars():
    assert encrypt("aaa") == "eee"
    assert encrypt("zzz") == "ddd"

def test_encrypt_full_alphabet():
    input_str = "abcdefghijklmnopqrstuvwxyz"
    expected = "efghijklmnopqrstuvwxyzabcd"
    assert encrypt(input_str) == expected

def test_encrypt_long_text():
    input_str = "The quick brown fox jumps over the lazy dog"
    expected = "Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk"
    assert encrypt(input_str) == expected