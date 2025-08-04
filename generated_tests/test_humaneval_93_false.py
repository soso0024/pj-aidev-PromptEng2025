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
    assert encode("HeLLo") == "hGllQ"
    assert encode("PyThOn") == "pYtHqN"

def test_empty_string():
    assert encode("") == ""

def test_no_vowels():
    assert encode("xyz") == "XYZ"
    assert encode("XYZ") == "xyz"

def test_all_vowels():
    assert encode("aeiou") == "CGKQW"
    assert encode("AEIOU") == "cgkqw"

@pytest.mark.parametrize("input_str,expected", [
    ("Hello World!", "hGLLQ wQRLD!"),
    ("Python3.9", "pYtHqN3.9"),
    ("aAeEiIoOuU", "CcGgKkQqWw"),
    ("123!@#", "123!@#"),
    ("   ", "   "),
    ("a.e.i.o.u", "C.G.K.Q.W"),
    ("Mixed-Case_Text", "mKXGD-cCSG_tGXT")
])
def test_various_inputs(input_str, expected):
    assert encode(input_str) == expected

def test_special_characters():
    assert encode("Hello! @World#") == "hGLLQ! @wQRLD#"

def test_numbers():
    assert encode("a1e2i3o4u5") == "C1G2K3Q4W5"

def test_whitespace():
    assert encode("\t\n ") == "\t\n "
    assert encode("a b c") == "C B c"

def test_repeated_characters():
    assert encode("aaa") == "CCC"
    assert encode("AaA") == "cCc"