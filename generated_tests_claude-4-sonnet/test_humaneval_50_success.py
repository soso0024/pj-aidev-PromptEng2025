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

def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

def test_decode_shift_empty_string():
    assert decode_shift("") == ""

def test_decode_shift_single_character():
    assert decode_shift("f") == "a"
    assert decode_shift("a") == "v"
    assert decode_shift("z") == "u"

def test_decode_shift_multiple_characters():
    assert decode_shift("mjqqt") == "hello"
    assert decode_shift("btwqi") == "world"

def test_decode_shift_full_alphabet():
    shifted = "fghijklmnopqrstuvwxyzabcde"
    original = "abcdefghijklmnopqrstuvwxyz"
    assert decode_shift(shifted) == original

@pytest.mark.parametrize("input_str,expected", [
    ("f", "a"),
    ("g", "b"),
    ("h", "c"),
    ("i", "d"),
    ("j", "e"),
    ("a", "v"),
    ("b", "w"),
    ("c", "x"),
    ("d", "y"),
    ("e", "z")
])
def test_decode_shift_individual_letters(input_str, expected):
    assert decode_shift(input_str) == expected

def test_decode_shift_repeated_characters():
    assert decode_shift("fff") == "aaa"
    assert decode_shift("zzz") == "uuu"

def test_decode_shift_long_string():
    long_input = "f" * 1000
    expected = "a" * 1000
    assert decode_shift(long_input) == expected

def test_decode_shift_wraparound():
    assert decode_shift("abcde") == "vwxyz"

def test_decode_shift_common_words():
    assert decode_shift("ymj") == "the"
    assert decode_shift("fsi") == "and"
    assert decode_shift("tk") == "of"

def test_decode_shift_with_non_lowercase():
    result = decode_shift("A")
    assert isinstance(result, str)
    
    result = decode_shift("Hello")
    assert isinstance(result, str)
    
    result = decode_shift("123")
    assert isinstance(result, str)
    
    result = decode_shift("hello world")
    assert isinstance(result, str)
    
    result = decode_shift("hello!")
    assert isinstance(result, str)

def test_decode_shift_type_error():
    with pytest.raises(TypeError):
        decode_shift(None)
    
    with pytest.raises(TypeError):
        decode_shift(123)
    
    result = decode_shift(['a', 'b', 'c'])
    assert isinstance(result, str)