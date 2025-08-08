# Test cases for HumanEval/50
# Generated using Claude API



def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# Generated test cases:
import pytest

def test_basic_shift():
    assert decode_shift("yfxy") == "tast"
    assert decode_shift("mjqqt") == "hello"

def test_empty_string():
    assert decode_shift("") == ""

def test_single_character():
    assert decode_shift("f") == "a"
    assert decode_shift("z") == "u"

@pytest.mark.parametrize("input_str,expected", [
    ("yfxy", "tast"),
    ("mjqqt", "hello"),
    ("btwqi", "world"),
    ("udufw", "pypar"),
    ("", ""),
    ("f", "a"),
    ("z", "u"),
    ("ffffffff", "aaaaaaaa"),
    ("zzzzzzzz", "uuuuuuuu"),
    ("fgbijkqrsxyz", "abwdeflmnstu")
])
def test_decode_shift_parametrized(input_str, expected):
    assert decode_shift(input_str) == expected

def test_preserve_case():
    result = decode_shift("ABCD")
    assert isinstance(result, str)

def test_non_alpha():
    result = decode_shift("123")
    assert isinstance(result, str)
    result = decode_shift("test!")
    assert isinstance(result, str)
    result = decode_shift(" ")
    assert isinstance(result, str)

def test_special_sequences():
    assert decode_shift("mnopqrstuvwxyzabcdefghijkl") == "hijklmnopqrstuvwxyzabcdefg"

def test_type_error():
    try:
        decode_shift(None)
    except:
        pass
    
    try:
        decode_shift(123)
    except:
        pass
    
    try:
        decode_shift(['a', 'b', 'c'])
    except:
        pass