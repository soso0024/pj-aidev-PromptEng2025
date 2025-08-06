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

def test_empty_string():
    assert encode("") == ""

def test_single_lowercase():
    assert encode("a") == "C"

def test_single_uppercase():
    assert encode("A") == "c"

def test_no_vowels():
    assert encode("xyz") == "XYZ"

def test_all_vowels_lowercase():
    assert encode("aeiou") == "CGKQW"

def test_all_vowels_uppercase():
    assert encode("AEIOU") == "cgkqw"

@pytest.mark.parametrize("input_str,expected", [
    ("test", "TGST"),
    ("hello", "HGLLQ"),
    ("This is a message", "tHKS KS C MGSSCGG"),
    ("UPPER", "wppgr"),
    ("MixedCase", "mKXGDcCSG"),
    ("zzz", "ZZZ"),
    ("aAaAa", "CcCcC"),
    ("Python", "pYTHQN"),
    ("OpenAI", "qPGNck"),
    ("Testing123", "tGSTKNG123")
])
def test_various_strings(input_str, expected):
    assert encode(input_str) == expected

@pytest.mark.parametrize("special_case", [
    "aeiouAEIOU",
    "AeIoUaEiOu",
    "aaaAAA",
    "EEEEEE"
])
def test_special_vowel_cases(special_case):
    result = encode(special_case)
    assert len(result) == len(special_case)
    assert result != special_case

def test_consecutive_vowels():
    assert encode("aei") == "CGK"
    assert encode("AEI") == "cgk"

def test_case_sensitivity():
    assert encode("aA") == "Cc"
    assert encode("zZ") == "Zz"