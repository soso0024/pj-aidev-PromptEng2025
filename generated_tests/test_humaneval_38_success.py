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

def test_decode_cyclic_empty_string():
    assert decode_cyclic("") == ""

def test_decode_cyclic_single_char():
    assert decode_cyclic("a") == "a"

@pytest.mark.parametrize("input_str", [
    "hello",
    "12345",
    "!@#$%",
    "   ",
    "abc123",
    "Hello, World!",
    "\n\t\r",
    "αβγ",
    "🌟✨"
])
def test_decode_cyclic_various_strings(input_str):
    encoded = encode_cyclic(input_str)
    decoded = decode_cyclic(encoded)
    assert decoded == input_str

def test_decode_cyclic_long_string():
    long_str = "a" * 1000
    encoded = encode_cyclic(long_str)
    decoded = decode_cyclic(encoded)
    assert decoded == long_str

@pytest.mark.parametrize("input_str", [
    None,
    123,
    ["a", "b", "c"],
    {"key": "value"},
    3.14
])
def test_decode_cyclic_invalid_input(input_str):
    with pytest.raises((TypeError, AttributeError, KeyError)):
        decode_cyclic(input_str)

def test_decode_cyclic_encoding_consistency():
    test_str = "test string"
    encoded = encode_cyclic(test_str)
    decoded = decode_cyclic(encoded)
    assert decoded == test_str

def test_decode_cyclic_special_chars():
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    encoded = encode_cyclic(special_chars)
    decoded = decode_cyclic(encoded)
    assert decoded == special_chars

def test_decode_cyclic_mixed_content():
    mixed = "Hello123!@#αβγ🌟"
    encoded = encode_cyclic(mixed)
    decoded = decode_cyclic(encoded)
    assert decoded == mixed

def test_decode_cyclic_whitespace():
    whitespace = "\n\t\r\f\v "
    encoded = encode_cyclic(whitespace)
    decoded = decode_cyclic(encoded)
    assert decoded == whitespace