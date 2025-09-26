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
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out

def test_encrypt_empty_string():
    assert encrypt('') == ''

def test_encrypt_single_lowercase_letter():
    assert encrypt('a') == 'e'
    assert encrypt('b') == 'f'
    assert encrypt('z') == 'd'

def test_encrypt_multiple_lowercase_letters():
    assert encrypt('abc') == 'efg'
    assert encrypt('xyz') == 'bcd'

def test_encrypt_wrap_around():
    assert encrypt('w') == 'a'
    assert encrypt('x') == 'b'
    assert encrypt('y') == 'c'
    assert encrypt('z') == 'd'

def test_encrypt_non_alphabetic_characters():
    assert encrypt('123') == '123'
    assert encrypt('!@#') == '!@#'
    assert encrypt(' ') == ' '
    assert encrypt('\n') == '\n'
    assert encrypt('\t') == '\t'

def test_encrypt_uppercase_letters():
    assert encrypt('A') == 'A'
    assert encrypt('ABC') == 'ABC'
    assert encrypt('XYZ') == 'XYZ'

def test_encrypt_mixed_case():
    assert encrypt('aA') == 'eA'
    assert encrypt('AbC') == 'AfC'

def test_encrypt_mixed_characters():
    assert encrypt('a1b2c3') == 'e1f2g3'
    assert encrypt('hello world!') == 'lipps asvph!'
    assert encrypt('test123') == 'xiwx123'

def test_encrypt_special_characters_and_spaces():
    assert encrypt('a b c') == 'e f g'
    assert encrypt('a-b-c') == 'e-f-g'
    assert encrypt('a.b.c') == 'e.f.g'

@pytest.mark.parametrize("input_str,expected", [
    ('a', 'e'),
    ('z', 'd'),
    ('hello', 'lipps'),
    ('world', 'asvph'),
    ('abcdefghijklmnopqrstuvwxyz', 'efghijklmnopqrstuvwxyzabcd'),
    ('', ''),
    ('123', '123'),
    ('ABC', 'ABC'),
    ('Hello World!', 'Lipps Wsvph!'),
    ('test@example.com', 'xiwx@ibeqtpi.gsq')
])
def test_encrypt_parametrized(input_str, expected):
    assert encrypt(input_str) == expected

def test_encrypt_long_string():
    long_input = 'a' * 1000
    expected = 'e' * 1000
    assert encrypt(long_input) == expected

def test_encrypt_all_lowercase_letters():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    expected = 'efghijklmnopqrstuvwxyzabcd'
    assert encrypt(alphabet) == expected