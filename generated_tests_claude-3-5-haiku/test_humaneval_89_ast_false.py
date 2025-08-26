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

def test_encrypt_with_spaces_and_punctuation():
    assert encrypt('hello world!') == 'hello world!'
    assert encrypt('test, 123') == 'test, 123'

def test_encrypt_empty_string():
    assert encrypt('') == ''

def test_encrypt_full_alphabet():
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'efghijklmnopqrstuvwxyzabcd'

@pytest.mark.parametrize("input_str,expected", [
    ('a', 'e'),
    ('z', 'c'),
    ('hello', 'lipps'),
    ('python', 'tcxlsr')
])
def test_encrypt_parametrized(input_str, expected):
    assert encrypt(input_str) == expected

def test_encrypt_non_string_input():
    with pytest.raises(TypeError):
        encrypt(123)
        encrypt(None)