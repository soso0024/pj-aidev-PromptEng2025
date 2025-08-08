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
    assert encrypt('hi') == 'lm'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'

@pytest.mark.parametrize("input_str,expected", [
    ("asdfghjkl", "ewhjklnop"),
    ("abcdefghijklmnopqrstuvwxyz", "efghijklmnopqrstuvwxyzabcd"),
    ("", ""),
    ("z", "d"),
    ("a", "e"),
])
def test_parametrized_encryption(input_str, expected):
    assert encrypt(input_str) == expected

@pytest.mark.parametrize("input_str,expected", [
    ("Hello World!", "Lipps Asvph!"),
    ("Test 123", "Xiwx 123"),
    ("a b c", "e f g"),
    ("Z Y X", "D C B"),
])
def test_mixed_case_and_special_chars(input_str, expected):
    assert encrypt(input_str.lower()) == expected.lower()

def test_repeated_characters():
    assert encrypt('aaa') == 'eee'
    assert encrypt('zzz') == 'ddd'

def test_special_sequences():
    assert encrypt('xyz') == 'bcd'
    assert encrypt('abc') == 'efg'

def test_non_alphabetic_chars():
    assert encrypt('123') == '123'
    assert encrypt('!@#') == '!@#'
    assert encrypt('a1b2c3') == 'e1f2g3'

def test_spaces():
    assert encrypt('a b c') == 'e f g'
    assert encrypt('   ') == '   '

def test_long_string():
    input_str = 'abcdefghijklmnopqrstuvwxyz' * 10
    expected = 'efghijklmnopqrstuvwxyzabcd' * 10
    assert encrypt(input_str) == expected
