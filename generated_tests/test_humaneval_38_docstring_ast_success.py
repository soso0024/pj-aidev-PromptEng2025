# Test cases for HumanEval/38
# Generated using Claude API



def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """

    return encode_cyclic(encode_cyclic(s))


# Generated test cases:
import pytest

def test_encode_cyclic_basic():
    assert encode_cyclic("abc") == "bca"
    assert encode_cyclic("abcdef") == "bcaefd"

def test_encode_cyclic_empty():
    assert encode_cyclic("") == ""

def test_encode_cyclic_single_char():
    assert encode_cyclic("a") == "a"

def test_encode_cyclic_two_chars():
    assert encode_cyclic("ab") == "ab"

@pytest.mark.parametrize("input_str,expected", [
    ("abc", "abc"),
    ("abcdef", "abcdef"),
    ("a", "a"),
    ("ab", "ab"),
    ("", ""),
    ("hello world", "hello world"),
    ("123456789", "123456789"),
    ("abcdefghi", "abcdefghi")
])
def test_decode_cyclic(input_str, expected):
    encoded = encode_cyclic(input_str)
    decoded = decode_cyclic(encoded)
    assert decoded == expected

@pytest.mark.parametrize("input_str", [
    "test",
    "python",
    "programming",
    "!@#$%^",
    "12345",
    "   ",
    "a b c",
    "mixed123string",
    "UPPERCASE",
    "lowercase"
])
def test_encode_decode_roundtrip(input_str):
    encoded = encode_cyclic(input_str)
    decoded = decode_cyclic(encoded)
    assert decoded == input_str

def test_encode_decode_special_chars():
    special_chars = "!@#$%^&*()"
    encoded = encode_cyclic(special_chars)
    decoded = decode_cyclic(encoded)
    assert decoded == special_chars

def test_encode_decode_whitespace():
    whitespace = "   \t\n  "
    encoded = encode_cyclic(whitespace)
    decoded = decode_cyclic(encoded)
    assert decoded == whitespace

def test_encode_decode_unicode():
    unicode_str = "Hello 世界"
    encoded = encode_cyclic(unicode_str)
    decoded = decode_cyclic(encoded)
    assert decoded == unicode_str