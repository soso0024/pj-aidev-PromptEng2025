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
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

@pytest.mark.parametrize("message,expected", [
    ("hello", "HGLLQ"),
    ("HELLO", "hgllq"),
    ("Hello World", "hGLLQ wQRLD"),
    ("aeiou", "CGKQW"),
    ("AEIOU", "cgkqw"),
    ("bcdfg", "BCDFG"),
    ("BCDFG", "bcdfg"),
    ("", ""),
    ("123", "123"),
    ("!@#$%", "!@#$%"),
    ("a", "C"),
    ("A", "c"),
    ("e", "G"),
    ("E", "g"),
    ("i", "K"),
    ("I", "k"),
    ("o", "Q"),
    ("O", "q"),
    ("u", "W"),
    ("U", "w"),
    ("Hello123World", "hGLLQ123wQRLD"),
    ("aEiOu", "CgKqW"),
    ("Programming", "pRQGRCMMKNG"),
    ("Python", "pYTHQN"),
    ("Test Case", "tGST cCSG"),
    ("MixedCASE", "mKXGDccsg"),
    ("   ", "   "),
    ("a e i o u", "C G K Q W"),
    ("A E I O U", "c g k q w"),
    ("!@#aeiou$%^", "!@#CGKQW$%^"),
    ("123aeiou456", "123CGKQW456"),
    ("aBcDeFgHiJkLmNoPqRsTuVwXyZ", "CbCdGfGhKjKlMnQpQrStWvWxYz")
])
def test_encode_parametrized(message, expected):
    assert encode(message) == expected

def test_encode_empty_string():
    assert encode("") == ""

def test_encode_only_vowels():
    assert encode("aeiou") == "CGKQW"
    assert encode("AEIOU") == "cgkqw"

def test_encode_only_consonants():
    assert encode("bcdfg") == "BCDFG"
    assert encode("BCDFG") == "bcdfg"

def test_encode_numbers_only():
    assert encode("12345") == "12345"

def test_encode_special_characters():
    assert encode("!@#$%^&*()") == "!@#$%^&*()"

def test_encode_mixed_case():
    assert encode("HeLLo") == "hGllQ"

def test_encode_spaces():
    assert encode("hello world") == "HGLLQ WQRLD"

def test_encode_single_character():
    assert encode("a") == "C"
    assert encode("b") == "B"
    assert encode("A") == "c"
    assert encode("B") == "b"

def test_encode_whitespace():
    assert encode("   ") == "   "
    assert encode("\t") == "\t"
    assert encode("\n") == "\n"

def test_encode_alphanumeric():
    assert encode("abc123XYZ") == "CBC123xyz"