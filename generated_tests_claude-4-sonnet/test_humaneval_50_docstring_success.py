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

def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

class TestEncodeShift:
    
    @pytest.mark.parametrize("input_str,expected", [
        ("a", "f"),
        ("z", "e"),
        ("hello", "mjqqt"),
        ("world", "btwqi"),
        ("abcdefghijklmnopqrstuvwxyz", "fghijklmnopqrstuvwxyzabcde"),
        ("", ""),
        ("x", "c"),
        ("y", "d"),
        ("programming", "uwtlwfrrnsl")
    ])
    def test_encode_shift_basic(self, input_str, expected):
        assert encode_shift(input_str) == expected
    
    def test_encode_shift_empty_string(self):
        assert encode_shift("") == ""
    
    def test_encode_shift_single_char(self):
        assert encode_shift("a") == "f"
        assert encode_shift("z") == "e"
    
    def test_encode_shift_wrap_around(self):
        assert encode_shift("vwxyz") == "abcde"

class TestDecodeShift:
    
    @pytest.mark.parametrize("input_str,expected", [
        ("f", "a"),
        ("e", "z"),
        ("mjqqt", "hello"),
        ("btwqi", "world"),
        ("fghijklmnopqrstuvwxyzabcde", "abcdefghijklmnopqrstuvwxyz"),
        ("", ""),
        ("c", "x"),
        ("d", "y"),
        ("uwtlwfrrnsl", "programming")
    ])
    def test_decode_shift_basic(self, input_str, expected):
        assert decode_shift(input_str) == expected
    
    def test_decode_shift_empty_string(self):
        assert decode_shift("") == ""
    
    def test_decode_shift_single_char(self):
        assert decode_shift("f") == "a"
        assert decode_shift("e") == "z"
    
    def test_decode_shift_wrap_around(self):
        assert decode_shift("abcde") == "vwxyz"

class TestEncodeDecodeRoundTrip:
    
    @pytest.mark.parametrize("original", [
        "hello",
        "world",
        "python",
        "test",
        "abcdefghijklmnopqrstuvwxyz",
        "programming",
        "a",
        "z",
        "",
        "quickbrownfox",
        "vwxyz"
    ])
    def test_encode_decode_roundtrip(self, original):
        encoded = encode_shift(original)
        decoded = decode_shift(encoded)
        assert decoded == original
    
    def test_decode_encode_roundtrip(self):
        test_strings = ["hello", "world", "python", "abcdefghijklmnopqrstuvwxyz", ""]
        for original in test_strings:
            decoded = decode_shift(original)
            encoded = encode_shift(decoded)
            assert encoded == original

class TestEdgeCases:
    
    def test_all_same_character(self):
        assert encode_shift("aaaa") == "ffff"
        assert decode_shift("ffff") == "aaaa"
    
    def test_alphabet_boundaries(self):
        assert encode_shift("abcde") == "fghij"
        assert encode_shift("vwxyz") == "abcde"
        assert decode_shift("fghij") == "abcde"
        assert decode_shift("abcde") == "vwxyz"
    
    def test_long_string(self):
        long_str = "a" * 1000
        encoded = encode_shift(long_str)
        assert len(encoded) == 1000
        assert all(c == "f" for c in encoded)
        assert decode_shift(encoded) == long_str
