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

def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    return ''.join([vowels_replace.get(i, i.swapcase()) for i in message])

def test_encode_empty_string():
    assert encode('') == ''

@pytest.mark.parametrize("input,expected", [
    ("test", "TGST"),
    ("This is a message", "tHIS IS A MSGSSAGM"),
    ("Hello, World!", "hGLLO, wORLD!"),
    ("aeiou AEIOU", "EGKOU CGKOU"),
    ("Python is awesome", "pYTHON IS CWGSOMG")
])
def test_encode_valid_inputs(input, expected):
    assert encode(input) == expected

def test_encode_non_letter_characters():
    assert encode('Test123!@#') == 'tGST123!@#'

def test_encode_mixed_case_input():
    assert encode('aBcDeFgH') == 'AbCdEfGh'