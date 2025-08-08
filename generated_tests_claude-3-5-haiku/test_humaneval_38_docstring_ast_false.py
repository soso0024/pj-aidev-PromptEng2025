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
    assert encode_cyclic("abcdefghi") == "bcdafghiek"

def test_encode_cyclic_short_string():
    assert encode_cyclic("ab") == "ab"
    assert encode_cyclic("abc") == "bca"

def test_encode_cyclic_empty_string():
    assert encode_cyclic("") == ""

def test_decode_cyclic_basic():
    assert decode_cyclic("bcdafghiek") == "abcdefghi"

def test_decode_cyclic_short_string():
    assert decode_cyclic("ab") == "ab"
    assert decode_cyclic("bca") == "abc"

def test_decode_cyclic_empty_string():
    assert decode_cyclic("") == ""

@pytest.mark.parametrize("input_str", [
    "hello",
    "python",
    "testing",
    "a" * 9,
    "cyclic"
])
def test_decode_encode_roundtrip(input_str):
    assert decode_cyclic(encode_cyclic(input_str)) == input_str

def test_decode_encode_unicode():
    unicode_str = "こんにちは世界"
    assert decode_cyclic(encode_cyclic(unicode_str)) == unicode_str

def test_decode_encode_mixed_characters():
    mixed_str = "Hello, 世界! 123"
    assert decode_cyclic(encode_cyclic(mixed_str)) == mixed_str