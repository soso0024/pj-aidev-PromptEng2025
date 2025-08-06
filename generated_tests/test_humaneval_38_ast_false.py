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

def test_decode_cyclic_with_str():
    input_str = "hello world"
    result = decode_cyclic(input_str)
    encoded = encode_cyclic(input_str)
    assert result == input_str

def test_decode_cyclic_idempotent():
    test_str = "hello world"
    first_decode = decode_cyclic(test_str)
    second_decode = decode_cyclic(first_decode)
    assert second_decode == test_str

def test_decode_cyclic_empty():
    assert decode_cyclic("") == ""

def test_decode_cyclic_single_char():
    assert decode_cyclic("x") == "x"

def test_decode_cyclic_special_chars():
    test_str = "\n\t"
    assert decode_cyclic(test_str) == test_str

@pytest.mark.parametrize("input_str", [
    None,
    123,
    ["hello"],
    {"key": "value"},
    3.14
])
def test_decode_cyclic_invalid_input(input_str):
    with pytest.raises(TypeError):
        decode_cyclic(input_str)

def test_decode_cyclic_triple_application():
    test_str = "hello"
    result = decode_cyclic(decode_cyclic(decode_cyclic(test_str)))
    assert result == test_str

@pytest.mark.parametrize("test_str", [
    "abc",
    "hello",
    "test123",
    "!@#",
    "αβγ"
])
def test_decode_cyclic_groups_of_three(test_str):
    result = decode_cyclic(test_str)
    assert len(result) == len(test_str)
    assert decode_cyclic(result) == test_str