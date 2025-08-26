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
        if c.lower() in d:
            idx = d.index(c.lower())
            shifted_idx = (idx + 2*2) % 26
            out += d[shifted_idx] if c.islower() else d[shifted_idx].upper()
        else:
            out += c
    return out

def test_basic_encryption():
    assert encrypt('abc') == 'cde'
    assert encrypt('xyz') == 'zab'

def test_mixed_case_input():
    assert encrypt('AbC') == 'CdE'

def test_non_alphabetic_characters():
    assert encrypt('a1b2c3') == 'c1d2e3'
    assert encrypt('hello world!') == 'jgnnq yqtnf!'

def test_empty_string():
    assert encrypt('') == ''

def test_full_alphabet_shift():
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'cdefghijklmnopqrstuvwxyzab'

@pytest.mark.parametrize("input_str,expected", [
    ('hello', 'jgnnq'),
    ('python', 'ravxqp'),
    ('encryption', 'gpetarvqp'),
    ('OpenAI', 'QrgpAK')
])
def test_parametrized_encryption(input_str, expected):
    assert encrypt(input_str) == expected

def test_special_characters():
    assert encrypt('!@#$%^&*()') == '!@#$%^&*()'

def test_whitespace():
    assert encrypt('  spaces  ') == '  urcegu  '