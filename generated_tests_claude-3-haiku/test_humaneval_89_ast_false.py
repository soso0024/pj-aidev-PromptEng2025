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

def test_encrypt_all_lowercase():
    assert encrypt('hello') == 'lipps'

def test_encrypt_mixed_case():
    assert encrypt('Hello World') == 'Hipps Wsvph'

def test_encrypt_with_numbers():
    assert encrypt('Hello123World') == 'Hipps123Wsvph'

def test_encrypt_with_special_characters():
    assert encrypt('Hello@World!') == 'Hipps@Wsvph!'

def test_encrypt_with_uppercase():
    assert encrypt('HELLO') == 'HELLO'

def test_encrypt_with_non_alphabetic_characters():
    assert encrypt('Hello 123 World!') == 'Hipps 123 Wsvph!'

def test_encrypt_with_non_ascii_characters():
    assert encrypt('Hélló Wórld') == 'Héppó Wóvph'

def test_encrypt_with_empty_character():
    assert encrypt(' ') == ' '

def test_encrypt_with_negative_index():
    with pytest.raises(IndexError):
        encrypt('a')