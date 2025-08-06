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

def test_basic_encoding():
    assert encode("hello") == "HGLLQ"
    assert encode("HELLO") == "hgllq"

def test_mixed_case():
    assert encode("HeLLo") == "hGllq"
    assert encode("wOrLd") == "WqRlD"

def test_empty_string():
    assert encode("") == ""

def test_no_vowels():
    assert encode("xyz") == "XYZ"
    assert encode("XYZ") == "xyz"

def test_all_vowels():
    assert encode("aeiou") == "CGKQW"
    assert encode("AEIOU") == "cgkqw"

@pytest.mark.parametrize("input_str,expected", [
    ("Hello World!", "hGllq wqRlD!"),
    ("Python3.8", "pYthqn3.8"),
    ("aAeEiIoOuU", "CcGgKkQqWw"),
    ("!@#$%^&*()", "!@#$%^&*()"),
    ("Mixed-Case_String", "mKxGd-cCsG_strKng"),
    ("     ", "     ")
])
def test_various_strings(input_str, expected):
    assert encode(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "12345",
    "!@#$%"
])
def test_reversible_encoding(input_str):
    encoded = encode(input_str)
    assert encode(encoded) == input_str

def test_special_characters():
    assert encode("Hello\n World") == "hGllq\n wqRlD"
    assert encode("\t\r\n") == "\t\r\n"

def test_unicode_characters():
    assert encode("Hello™") == "hGllq™"
    assert encode("Hello©World") == "hGllq©wqRlD"