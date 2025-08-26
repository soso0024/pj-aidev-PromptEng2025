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

def test_encode_cyclic_basic():
    assert encode_cyclic("abcdef") == "bcdafe"

def test_encode_cyclic_short_string():
    assert encode_cyclic("ab") == "ab"

def test_encode_cyclic_empty_string():
    assert encode_cyclic("") == ""

def test_decode_cyclic_basic():
    assert decode_cyclic("bcdafe") == "abcdef"

def test_decode_cyclic_short_string():
    assert decode_cyclic("ab") == "ab"

def test_decode_cyclic_empty_string():
    assert decode_cyclic("") == ""

@pytest.mark.parametrize("input_str,expected", [
    ("abcdef", "bcdafe"),
    ("hello world", "el olhwrd"),
    ("python", "ythonp"),
    ("a", "a"),
    ("", "")
])
def test_encode_cyclic_parametrized(input_str, expected):
    assert encode_cyclic(input_str) == expected

@pytest.mark.parametrize("input_str,expected", [
    ("bcdafe", "abcdef"),
    ("el olhwrd", "hello world"),
    ("ythonp", "python"),
    ("a", "a"),
    ("", "")
])
def test_decode_cyclic_parametrized(input_str, expected):
    assert decode_cyclic(input_str) == expected

def test_encode_decode_roundtrip():
    original = "hello world"
    encoded = encode_cyclic(original)
    decoded = decode_cyclic(encoded)
    assert decoded == original