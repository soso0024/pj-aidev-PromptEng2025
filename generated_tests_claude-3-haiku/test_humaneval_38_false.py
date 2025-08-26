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
    return ''.join(c * (i+1) for i, c in enumerate(s))

def decode_cyclic(s: str):
    result = ""
    for i in range(0, len(s), 1):
        result += s[i:i+i+1]
    return result

def test_decode_cyclic_normal_cases():
    assert decode_cyclic("abc") == "abcabcabc"
    assert decode_cyclic("hello") == "hellohellohello"
    assert decode_cyclic("python") == "pythonpythonpython"

def test_decode_cyclic_empty_string():
    assert decode_cyclic("") == ""

def test_decode_cyclic_single_character():
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("x") == "x"

@pytest.mark.parametrize("input,expected", [
    ("123", "112233"),
    ("xyz", "xyyzzz"),
    ("foo", "foofoofoofoo")
])
def test_decode_cyclic_parametrized(input, expected):
    assert decode_cyclic(input) == expected

def test_decode_cyclic_raises_type_error():
    with pytest.raises(TypeError):
        decode_cyclic(123)
    with pytest.raises(TypeError):
        decode_cyclic(None)