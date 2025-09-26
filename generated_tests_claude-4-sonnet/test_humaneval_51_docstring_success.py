# Test cases for HumanEval/51
# Generated using Claude API



def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


# Generated test cases:
import pytest

def remove_vowels(text):
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

def test_remove_vowels_empty_string():
    assert remove_vowels('') == ''

def test_remove_vowels_with_newline():
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'

def test_remove_vowels_simple():
    assert remove_vowels('abcdef') == 'bcdf'

def test_remove_vowels_all_vowels():
    assert remove_vowels('aaaaa') == ''

def test_remove_vowels_mixed_case():
    assert remove_vowels('aaBAA') == 'B'

def test_remove_vowels_no_vowels():
    assert remove_vowels('zbcd') == 'zbcd'

@pytest.mark.parametrize("input_text,expected", [
    ('', ''),
    ('a', ''),
    ('e', ''),
    ('i', ''),
    ('o', ''),
    ('u', ''),
    ('A', ''),
    ('E', ''),
    ('I', ''),
    ('O', ''),
    ('U', ''),
    ('bcdfg', 'bcdfg'),
    ('BCDFG', 'BCDFG'),
    ('aeiou', ''),
    ('AEIOU', ''),
    ('AeIoU', ''),
    ('hello', 'hll'),
    ('HELLO', 'HLL'),
    ('Hello World', 'Hll Wrld'),
    ('123456', '123456'),
    ('a1e2i3o4u5', '12345'),
    ('!@#$%', '!@#$%'),
    ('aeiou!@#$%AEIOU', '!@#$%'),
    ('The quick brown fox', 'Th qck brwn fx'),
    ('Programming', 'Prgrmmng'),
    ('aAeEiIoOuU', ''),
    ('xyz', 'xyz'),
    ('XYZ', 'XYZ'),
    (' ', ' '),
    ('   ', '   '),
    ('a b c d e', ' b c d '),
    ('\n\t\r', '\n\t\r'),
    ('a\nb\nc\nd\ne', '\nb\nc\nd\n'),
    ('special chars: !@#$%^&*()', 'spcl chrs: !@#$%^&*()'),
    ('1234567890', '1234567890'),
    ('MiXeD cAsE tExT', 'MXD cs txT')
])
def test_remove_vowels_parametrized(input_text, expected):
    assert remove_vowels(input_text) == expected

def test_remove_vowels_unicode():
    assert remove_vowels('café') == 'cfé'

def test_remove_vowels_long_string():
    long_text = 'a' * 1000 + 'b' * 1000
    expected = 'b' * 1000
    assert remove_vowels(long_text) == expected

def test_remove_vowels_alternating():
    assert remove_vowels('abababab') == 'bbbb'

def test_remove_vowels_consonants_only():
    assert remove_vowels('bcdfghjklmnpqrstvwxyz') == 'bcdfghjklmnpqrstvwxyz'

def test_remove_vowels_vowels_only():
    assert remove_vowels('aeiouAEIOU') == ''