# Test cases for HumanEval/50
# Generated using Claude API



def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


# Generated test cases:
import pytest

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "mjqqt"),
    ("abcde", "fghij"),
    ("zzzzz", "eeeee"),
    ("", ""),
    ("z", "e"),
    ("abcdefghijklmnopqrstuvwxyz", "fghijklmnopqrstuvwxyzabcde"),
])
def test_encode_shift(input_str, expected):
    assert encode_shift(input_str) == expected

@pytest.mark.parametrize("encoded_str,expected", [
    ("mjqqt", "hello"),
    ("fghij", "abcde"),
    ("eeeee", "zzzzz"),
    ("", ""),
    ("e", "z"),
    ("fghijklmnopqrstuvwxyzabcde", "abcdefghijklmnopqrstuvwxyz"),
])
def test_decode_shift(encoded_str, expected):
    assert decode_shift(encoded_str) == expected

def test_encode_decode_roundtrip():
    test_strings = [
        "hello",
        "python",
        "testing",
        "abcdefghijklmnopqrstuvwxyz",
        "",
        "z"
    ]
    for s in test_strings:
        assert decode_shift(encode_shift(s)) == s

def test_decode_encode_roundtrip():
    test_strings = [
        "mjqqt",
        "fghij",
        "eeeee",
        "fghijklmnopqrstuvwxyzabcde",
        "",
        "e"
    ]
    for s in test_strings:
        assert encode_shift(decode_shift(s)) == s

def test_encode_shift_raises_on_invalid_input():
    invalid_inputs = [
        "Hello",  # uppercase
        "hello!",  # punctuation
        "hello123",  # numbers
        "hello world",  # spaces
    ]
    for invalid_input in invalid_inputs:
        try:
            encode_shift(invalid_input)
            pytest.fail(f"Expected ValueError for input: {invalid_input}")
        except (ValueError, IndexError):
            pass

def test_decode_shift_raises_on_invalid_input():
    invalid_inputs = [
        "MJQQT",  # uppercase
        "fghij!",  # punctuation
        "mjqqt123",  # numbers
        "mjqqt world",  # spaces
    ]
    for invalid_input in invalid_inputs:
        try:
            decode_shift(invalid_input)
            pytest.fail(f"Expected ValueError for input: {invalid_input}")
        except (ValueError, IndexError):
            pass