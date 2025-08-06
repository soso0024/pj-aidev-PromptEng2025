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
    assert encode("test") == "TGST"
    assert encode("hello") == "HGLLQ"

def test_mixed_case():
    assert encode("Hello") == "hGLLQ"
    assert encode("TeSt") == "tGsT"

def test_all_uppercase():
    assert encode("TEST") == "tgst"
    assert encode("HELLO") == "hgllq"

def test_all_lowercase():
    assert encode("test") == "TGST"
    assert encode("hello") == "HGLLQ"

@pytest.mark.parametrize("input_str,expected", [
    ("This is a message", "tHKS KS C MGSSCGG"),
    ("aeiou", "CGKQW"),
    ("AEIOU", "cgkqw"),
    ("xyz", "XYZ"),
    ("", ""),
    ("Test Message", "tGST mGSSCGG"),
    ("AaEeIiOoUu", "cCgGkKqQwW")
])
def test_parametrized_cases(input_str, expected):
    assert encode(input_str) == expected

def test_single_letter():
    assert encode("a") == "C"
    assert encode("A") == "c"
    assert encode("z") == "Z"
    assert encode("Z") == "z"

def test_special_sequences():
    assert encode("aaa") == "CCC"
    assert encode("eee") == "GGG"
    assert encode("iii") == "KKK"
    assert encode("ooo") == "QQQ"
    assert encode("uuu") == "WWW"

def test_consecutive_vowels():
    assert encode("ae") == "CG"
    assert encode("ei") == "GK"
    assert encode("io") == "KQ"
    assert encode("ou") == "QW"

def test_only_consonants():
    assert encode("bcdfg") == "BCDFG"
    assert encode("BCDFG") == "bcdfg"
    assert encode("BcDfG") == "bCdFg"