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

def test_encode_empty_message():
    assert encode("") == ""

def test_encode_all_vowels():
    assert encode("aeiouAEIOU") == "cgiouCGIOU"

def test_encode_mixed_message():
    assert encode("Hello World") == "HEllO WOrld"

@pytest.mark.parametrize("message,expected", [
    ("Python is awesome", "PYthOn Is awEsOmE"),
    ("The quick brown fox", "ThE qUIck brOwn fOx"),
    ("LEARN PYTEST", "lEArn pYtEst"),
    ("123 abc DEF", "123 Abc dEf")
])
def test_encode_various_messages(message, expected):
    assert encode(message) == expected

def test_encode_non_string_input():
    with pytest.raises(TypeError):
        encode(123)