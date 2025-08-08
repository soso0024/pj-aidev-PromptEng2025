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
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    return encode_cyclic(encode_cyclic(s))

def test_decode_cyclic_empty_string():
    assert decode_cyclic("") == ""

def test_decode_cyclic_single_char():
    assert decode_cyclic("a") == "a"

def test_decode_cyclic_multiple_chars():
    assert decode_cyclic("hello") == "hello"

@pytest.mark.parametrize("input_str", [
    "python",
    "test",
    "a",
    "xyz",
    "programming"
])
def test_decode_cyclic_various_inputs(input_str):
    assert decode_cyclic(input_str) == input_str

def test_decode_cyclic_unicode():
    assert decode_cyclic("こんにちは") == "こんにちは"

def test_decode_cyclic_special_chars():
    assert decode_cyclic("!@#$%^") == "!@#$%^"

def test_decode_cyclic_whitespace():
    assert decode_cyclic("  spaces  ") == "  spaces  "

def test_decode_cyclic_numbers():
    assert decode_cyclic("12345") == "12345"