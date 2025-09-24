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

@pytest.mark.parametrize("input_message,expected", [
    ("test", "TGST"),
    ("This is a message", "tHKS KS C MGSSCGG"),
    ("", ""),
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
    ("aeiou", "CGKQW"),
    ("AEIOU", "cgkqw"),
    ("bcdfg", "BCDFG"),
    ("BCDFG", "bcdfg"),
    ("Hello World", "hGLLQ wQRLD"),
    ("Programming", "pRQGRCMMKNG"),
    ("xyz", "XYZ"),
    ("XYZ", "xyz"),
    ("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ", "CcBbCcDdGgFfGgHhKkJjKkLlMmNnQqPpQqRrSsTtWwVvWwXxYyZz"),
    ("The quick brown fox jumps over the lazy dog", "tHG QWKCK BRQWN FQX JWMPS QVGR THG LCZY DQG"),
    ("1234567890", "1234567890"),
    ("!@#$%^&*()", "!@#$%^&*()"),
    ("Mix3d Ch4r5", "mKX3D cH4R5"),
    ("a1e2i3o4u5", "C1G2K3Q4W5"),
    ("A1E2I3O4U5", "c1g2k3q4w5")
])
def test_encode_parametrized(input_message, expected):
    assert encode(input_message) == expected

def test_encode_empty_string():
    assert encode("") == ""

def test_encode_single_vowel_lowercase():
    assert encode("a") == "C"
    assert encode("e") == "G"
    assert encode("i") == "K"
    assert encode("o") == "Q"
    assert encode("u") == "W"

def test_encode_single_vowel_uppercase():
    assert encode("A") == "c"
    assert encode("E") == "g"
    assert encode("I") == "k"
    assert encode("O") == "q"
    assert encode("U") == "w"

def test_encode_single_consonant_lowercase():
    assert encode("b") == "B"
    assert encode("z") == "Z"

def test_encode_single_consonant_uppercase():
    assert encode("B") == "b"
    assert encode("Z") == "z"

def test_encode_all_vowels():
    assert encode("aeiouAEIOU") == "CGKQWcgkqw"

def test_encode_all_consonants():
    assert encode("bcdfghjklmnpqrstvwxyz") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_encode_mixed_case():
    assert encode("AbCdEfGhIjKlMnOpQrStUvWxYz") == "cBcDgFgHkJkLmNqPqRsTwVwXyZ"

def test_encode_with_spaces():
    assert encode("a e i o u") == "C G K Q W"

def test_encode_with_numbers():
    assert encode("a1b2c3") == "C1B2C3"

def test_encode_with_special_characters():
    assert encode("a!e@i#o$u%") == "C!G@K#Q$W%"

def test_encode_long_string():
    long_input = "a" * 1000
    expected = "C" * 1000
    assert encode(long_input) == expected

def test_encode_example_cases():
    assert encode("test") == "TGST"
    assert encode("This is a message") == "tHKS KS C MGSSCGG"