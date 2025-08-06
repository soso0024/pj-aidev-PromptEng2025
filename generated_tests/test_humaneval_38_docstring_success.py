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

@pytest.mark.parametrize("input_str,expected", [
    ("abc", "bca"),
    ("abcdef", "bcaefd"),
    ("abcdefghi", "bcaefdhig"),
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("abcd", "bcad"),
    ("123456789", "231564897"),
    ("!@#$%^", "@#!%^$"),
    ("   ", "   "),
    ("a b c", " ba c"),
    ("abcdefghijklmnop", "bcaefdhigkljnomp"),
    ("12", "12"),
    ("123", "231"),
    ("1234", "2314"),
])
def test_encode_cyclic(input_str, expected):
    assert encode_cyclic(input_str) == expected

@pytest.mark.parametrize("input_str", [
    "abc",
    "abcdef",
    "abcdefghi",
    "",
    "a",
    "ab",
    "abcd",
    "123456789",
    "!@#$%^",
    "   ",
    "a b c",
    "abcdefghijklmnop",
])
def test_encode_decode_cyclic_roundtrip(input_str):
    encoded = encode_cyclic(input_str)
    decoded = decode_cyclic(encoded)
    assert decoded == input_str

@pytest.mark.parametrize("input_str,expected", [
    ("bca", "abc"),
    ("bcaefd", "abcdef"),
    ("bcaefdhig", "abcdefghi"),
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("bcad", "abcd"),
    ("231564897", "123456789"),
    ("@#!%^$", "!@#$%^"),
    ("   ", "   "),
    (" ba c", "a b c"),
])
def test_decode_cyclic(input_str, expected):
    assert decode_cyclic(input_str) == expected

def test_encode_cyclic_none():
    with pytest.raises(TypeError):
        encode_cyclic(None)

def test_decode_cyclic_none():
    with pytest.raises(TypeError):
        decode_cyclic(None)

def test_encode_cyclic_non_string():
    with pytest.raises(TypeError):
        encode_cyclic(123)

def test_decode_cyclic_non_string():
    with pytest.raises(TypeError):
        decode_cyclic(123)