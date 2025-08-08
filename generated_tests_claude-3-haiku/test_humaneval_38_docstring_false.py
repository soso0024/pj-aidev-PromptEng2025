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
from your_module import encode_cyclic, decode_cyclic

@pytest.mark.parametrize("input_str, expected", [
    ("abc", "bca"),
    ("hello", "lohel"),
    ("world", "orlwd"),
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("abcdef", "bcdefa"),
    ("abcdefghi", "bcdefgahi"),
    ("abcdefghijkl", "bcdefghijlk"),
])
def test_encode_cyclic(input_str, expected):
    assert encode_cyclic(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("bca", "abc"),
    ("lohel", "hello"),
    ("orlwd", "world"),
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("bcdefa", "abcdef"),
    ("bcdefgahi", "abcdefghi"),
    ("bcdefghijlk", "abcdefghijkl"),
])
def test_decode_cyclic(input_str, expected):
    assert decode_cyclic(input_str) == expected

def test_decode_cyclic_canonical():
    assert decode_cyclic(encode_cyclic("hello")) == "hello"
    assert decode_cyclic(encode_cyclic("")) == ""
    assert decode_cyclic(encode_cyclic("abcdefghijkl")) == "abcdefghijkl"