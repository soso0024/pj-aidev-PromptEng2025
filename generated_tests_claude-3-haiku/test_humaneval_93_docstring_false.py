# Test cases for HumanEval/93
# Generated using Claude API


def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


# Generated test cases:
import pytest
import string

def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace.get(i, i) for i in message])

def test_encode_empty_string():
    assert encode('') == ''

def test_encode_all_lowercase():
    assert encode('test') == 'TGST'

def test_encode_all_uppercase():
    assert encode('TEST') == 'tgst'

def test_encode_mixed_case():
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'

def test_encode_non_alphabetic_characters():
    assert encode('Test123!@#') == 'tGST123!@#'

@pytest.mark.parametrize("input,expected", [
    ("aeiou", "CGIKU"),
    ("AEIOU", "cGIKU"),
    ("Hello World", "hGLLO wORLD"),
    ("Python is awesome", "pYTHON KS CWGSOMG"),
    ("The quick brown fox", "tHG QUKCX BROWN FOX")
])
def test_encode_various_inputs(input, expected):
    assert encode(input) == expected

def test_encode_single_character():
    assert encode('a') == 'G'
    assert encode('A') == 'g'

def test_encode_whitespace():
    assert encode('  ') == '  '

def test_encode_punctuation():
    assert encode('Test, this is a message!') == 'tGST, THKS KS C MGSSCGG!'