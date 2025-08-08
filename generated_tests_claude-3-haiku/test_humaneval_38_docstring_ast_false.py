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
from encode_cyclic import encode_cyclic, decode_cyclic
import pytest

def test_encode_cyclic_empty_string():
    assert encode_cyclic("") == ""

def test_encode_cyclic_single_char():
    assert encode_cyclic("a") == "a"

def test_encode_cyclic_two_chars():
    assert encode_cyclic("ab") == "ab"

@pytest.mark.parametrize("input_str,expected", [
    ("abc", "bca"),
    ("abcd", "bcda"),
    ("abcde", "bcdea"),
    ("abcdefghi", "bcdefghai")
])
def test_encode_cyclic_normal_cases(input_str, expected):
    assert encode_cyclic(input_str) == expected

def test_decode_cyclic_empty_string():
    assert decode_cyclic("") == ""

def test_decode_cyclic_single_char():
    assert decode_cyclic("a") == "a"

def test_decode_cyclic_two_chars():
    assert decode_cyclic("ab") == "ab"

@pytest.mark.parametrize("input_str,expected", [
    ("bca", "abc"),
    ("bcda", "abcd"),
    ("bcdea", "abcde"),
    ("bcdefghai", "abcdefghi")
])
def test_decode_cyclic_normal_cases(input_str, expected):
    assert decode_cyclic(input_str) == expected

def test_decode_cyclic_canonical_implementation():
    assert decode_cyclic(encode_cyclic("abcdefghi")) == "abcdefghi"