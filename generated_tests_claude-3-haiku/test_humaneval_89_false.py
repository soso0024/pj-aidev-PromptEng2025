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

def test_encrypt_normal_cases():
    assert encrypt("hello") == "jmmpc"
    assert encrypt("python") == "ravjqp"
    assert encrypt("abc") == "efg"

def test_encrypt_empty_string():
    assert encrypt("") == ""

def test_encrypt_non_alphabetic_characters():
    assert encrypt("hello123!@#") == "jmmpc123!@#"
    assert encrypt("abc DEF") == "efg IJK"

def test_encrypt_uppercase_characters():
    assert encrypt("HELLO") == "JMMPC"

@pytest.mark.parametrize("input,expected", [
    ("hello", "jmmpc"),
    ("python", "ravjqp"),
    ("abc", "efg"),
    ("", ""),
    ("hello123!@#", "jmmpc123!@#"),
    ("abc DEF", "efg IJK"),
    ("HELLO", "JMMPC")
])
def test_encrypt_all_cases(input, expected):
    assert encrypt(input) == expected