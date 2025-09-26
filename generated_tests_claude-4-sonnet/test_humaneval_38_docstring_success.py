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

class TestDecodeCyclic:
    
    def test_empty_string(self):
        assert decode_cyclic("") == ""
    
    def test_single_character(self):
        assert decode_cyclic("a") == "a"
    
    def test_two_characters(self):
        assert decode_cyclic("ab") == "ab"
    
    def test_three_characters(self):
        encoded = encode_cyclic("abc")
        assert decode_cyclic(encoded) == "abc"
    
    def test_four_characters(self):
        encoded = encode_cyclic("abcd")
        assert decode_cyclic(encoded) == "abcd"
    
    def test_five_characters(self):
        encoded = encode_cyclic("abcde")
        assert decode_cyclic(encoded) == "abcde"
    
    def test_six_characters(self):
        encoded = encode_cyclic("abcdef")
        assert decode_cyclic(encoded) == "abcdef"
    
    def test_seven_characters(self):
        encoded = encode_cyclic("abcdefg")
        assert decode_cyclic(encoded) == "abcdefg"
    
    def test_nine_characters(self):
        encoded = encode_cyclic("abcdefghi")
        assert decode_cyclic(encoded) == "abcdefghi"
    
    @pytest.mark.parametrize("input_str", [
        "hello",
        "world",
        "python",
        "testing",
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefg",
        "abcdefgh",
        "abcdefghi",
        "1234567890",
        "!@#$%^&*()",
        "Hello World!",
        "   ",
        "a b c",
        "123",
        "12345678901234567890"
    ])
    def test_encode_decode_roundtrip(self, input_str):
        encoded = encode_cyclic(input_str)
        decoded = decode_cyclic(encoded)
        assert decoded == input_str
    
    def test_special_characters(self):
        test_str = "!@#$%^"
        encoded = encode_cyclic(test_str)
        assert decode_cyclic(encoded) == test_str
    
    def test_numbers(self):
        test_str = "123456789"
        encoded = encode_cyclic(test_str)
        assert decode_cyclic(encoded) == test_str
    
    def test_mixed_content(self):
        test_str = "a1!b2@c3#"
        encoded = encode_cyclic(test_str)
        assert decode_cyclic(encoded) == test_str
    
    def test_spaces(self):
        test_str = "a b c d e f"
        encoded = encode_cyclic(test_str)
        assert decode_cyclic(encoded) == test_str
    
    def test_long_string(self):
        test_str = "abcdefghijklmnopqrstuvwxyz" * 10
        encoded = encode_cyclic(test_str)
        assert decode_cyclic(encoded) == test_str
    
    def test_unicode_characters(self):
        test_str = "αβγδεζ"
        encoded = encode_cyclic(test_str)
        assert decode_cyclic(encoded) == test_str
    
    def test_repeated_characters(self):
        test_str = "aaabbbccc"
        encoded = encode_cyclic(test_str)
        assert decode_cyclic(encoded) == test_str
    
    def test_decode_is_inverse_of_encode(self):
        test_cases = ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "hello world", "123456789"]
        for test_str in test_cases:
            encoded = encode_cyclic(test_str)
            decoded = decode_cyclic(encoded)
            assert decoded == test_str
