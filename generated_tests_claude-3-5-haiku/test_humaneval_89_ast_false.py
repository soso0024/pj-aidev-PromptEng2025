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
    assert encrypt('AbC') == 'AbC'
    assert encrypt('Hello') == 'Hello'

def test_encrypt_special_characters():
    assert encrypt('hello, world!') == 'hello, world!'
    assert encrypt('123 abc') == '123 efg'

def test_encrypt_empty_string():
    assert encrypt('') == ''

def test_encrypt_full_alphabet():
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'efghijklmnopqrstuvwxyzabcd'

def test_encrypt_repeated_characters():
    assert encrypt('aaa') == 'eee'

def test_encrypt_unicode_characters():
    assert encrypt('áéíóú') == 'áéíóú'

def test_encrypt_whitespace():
    assert encrypt('  hello  ') == '  hello  '