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

def test_encrypt_empty_string():
    assert encrypt('') == ''

def test_encrypt_lowercase_letters():
    assert encrypt('abc') == 'efg'
    assert encrypt('xyz') == 'bcd'

def test_encrypt_uppercase_letters():
    assert encrypt('ABC') == 'EFG'
    assert encrypt('XYZ') == 'BCD'

def test_encrypt_mixed_case():
    assert encrypt('aBc') == 'eBg'
    assert encrypt('xYz') == 'bCd'

def test_encrypt_non_alphabetic_characters():
    assert encrypt('123!@#') == '123!@#'
    assert encrypt('hello world!') == 'lipps asvph!'

@pytest.mark.parametrize("input,expected", [
    ('python', 'tcxlsr'),
    ('javascript', 'jezewgvmtx'),
    ('encryption', 'irgvctxmsr'),
    ('decryption', 'higvctxmsr')
])
def test_encrypt_various_inputs(input, expected):
    assert encrypt(input) == expected

def test_encrypt_long_string():
    long_string = 'The quick brown fox jumps over the lazy dog.'
    expected = 'Tli uymgo fvsar jsb nyqtw sziv xli pedc hsk.'
    assert encrypt(long_string) == expected