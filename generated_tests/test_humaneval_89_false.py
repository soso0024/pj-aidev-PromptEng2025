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
    assert encrypt("abc") == "efg"
    assert encrypt("xyz") == "bcd"

def test_mixed_case():
    assert encrypt("Hello") == "hipps"
    assert encrypt("hello") == "lipps"

def test_empty_string():
    assert encrypt("") == ""

def test_special_characters():
    assert encrypt("hello!") == "lipps!"
    assert encrypt("@#$%") == "@#$%"

def test_spaces():
    assert encrypt("hello world") == "lipps asvph"

@pytest.mark.parametrize("input_str,expected", [
    ("abc", "efg"),
    ("xyz", "bcd"),
    ("hello", "lipps"),
    ("", ""),
    ("hello!", "lipps!"),
    ("a b c", "e f g"),
    ("123", "123"),
    ("mix123ed", "qmb123ih"),
    ("abcdefghijklmnopqrstuvwxyz", "efghijklmnopqrstuvwxyzabcd"),
    ("!@#$%^&*()", "!@#$%^&*()")
])
def test_encryption_cases(input_str, expected):
    assert encrypt(input_str) == expected

def test_numbers():
    assert encrypt("123") == "123"
    assert encrypt("a1b2c3") == "e1f2g3"

def test_long_string():
    assert encrypt("abcdefghijklmnopqrstuvwxyz") == "efghijklmnopqrstuvwxyzabcd"

def test_repeated_characters():
    assert encrypt("aaa") == "eee"
    assert encrypt("zzz") == "ddd"