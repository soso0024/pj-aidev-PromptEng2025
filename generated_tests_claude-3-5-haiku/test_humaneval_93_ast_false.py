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
    vowels_replace = {
        'a': 'C', 'e': 'G', 'i': 'K', 'o': 'Q', 'u': 'W',
        'A': 'c', 'E': 'g', 'I': 'k', 'O': 'q', 'U': 'w'
    }
    message = message.swapcase()
    return ''.join([vowels_replace.get(i, i) for i in message])

def test_encode_basic_lowercase():
    assert encode("hello") == "HeLLo"

def test_encode_basic_uppercase():
    assert encode("WORLD") == "wORLd"

def test_encode_mixed_case():
    assert encode("HeLLo WoRLd") == "hEllO wOrld"

def test_encode_with_vowels():
    assert encode("aeiou") == "CEGIK"

def test_encode_with_uppercase_vowels():
    assert encode("AEIOU") == "cegik"

def test_encode_with_numbers():
    assert encode("hello123") == "HeLLo123"

def test_encode_with_special_characters():
    assert encode("hello!@#") == "HeLLo!@#"

def test_encode_empty_string():
    assert encode("") == ""

def test_encode_with_spaces():
    assert encode("hello world") == "HeLLo WoRLd"

@pytest.mark.parametrize("input_str,expected", [
    ("python", "PYThOn"),
    ("pytest", "PYTeSt"),
    ("OpenAI", "oPENai"),
    ("a1b2c3", "A1B2C3"),
    ("!@#$%^", "!@#$%^")
])
def test_encode_parametrized(input_str, expected):
    assert encode(input_str) == expected