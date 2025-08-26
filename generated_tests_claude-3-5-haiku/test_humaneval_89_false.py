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

def test_encrypt_lowercase_letters():
    assert encrypt('abc') == 'efg'
    assert encrypt('xyz') == 'bcd'

def test_encrypt_mixed_case():
    assert encrypt('ABC') == 'ABC'
    assert encrypt('aBc') == 'aBc'

def test_encrypt_with_spaces_and_punctuation():
    assert encrypt('hello world!') == 'lipps asvph!'
    assert encrypt('a b c!') == 'e f g!'

def test_encrypt_empty_string():
    assert encrypt('') == ''

def test_encrypt_numbers_and_symbols():
    assert encrypt('123!@#') == '123!@#'

def test_encrypt_full_alphabet():
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'efghijklmnopqrstuvwxyzabcd'

@pytest.mark.parametrize("input_str,expected", [
    ('test', 'xiwx'),
    ('python', 'tcxlsr'),
    ('encryption', 'gpetcxxmsr')
])
def test_encrypt_parametrized(input_str, expected):
    assert encrypt(input_str) == expected