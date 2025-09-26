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

def test_decode_cyclic_single_character():
    assert decode_cyclic("a") == "a"

def test_decode_cyclic_two_characters():
    assert decode_cyclic("ab") == "ab"

def test_decode_cyclic_three_characters():
    assert decode_cyclic("abc") == "cab"

def test_decode_cyclic_four_characters():
    assert decode_cyclic("abcd") == "cabd"

def test_decode_cyclic_five_characters():
    assert decode_cyclic("abcde") == "cabde"

def test_decode_cyclic_six_characters():
    assert decode_cyclic("abcdef") == "cabfde"

def test_decode_cyclic_seven_characters():
    assert decode_cyclic("abcdefg") == "cabfdeg"

def test_decode_cyclic_eight_characters():
    assert decode_cyclic("abcdefgh") == "cabfdegh"

def test_decode_cyclic_nine_characters():
    assert decode_cyclic("abcdefghi") == "cabfdeigh"

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "lhelo"),
    ("world", "rwold"),
    ("python", "tpynho"),
    ("testing", "stentig"),
    ("abcdefghijklmnopqrstuvwxyz", "cabfdeighljkomnrpqustxvwyz"),
    ("1234567890", "3126459780"),
    ("!@#$%^&*()", "#!@^$%(&*)"),
    ("Hello World!", "lHe lorWo!ld"),
    ("   ", "   "),
    ("a b c", "ba  c"),
    ("123abc456def", "312cab645fde"),
    ("special chars: !@#$%^&*()", "espacicl rha s:#!@^$%(&*)"),
    ("mixed123ABC!@#", "xmi1edA23!BC@#"),
])
def test_decode_cyclic_various_strings(input_str, expected):
    assert decode_cyclic(input_str) == expected

def test_decode_cyclic_whitespace_only():
    assert decode_cyclic("   ") == "   "
    assert decode_cyclic("\t\n\r") == "\r\t\n"

def test_decode_cyclic_unicode():
    assert decode_cyclic("αβγ") == "γαβ"
    assert decode_cyclic("🙂🙃😊") == "😊🙂🙃"

def test_decode_cyclic_long_string():
    long_str = "a" * 1000
    assert decode_cyclic(long_str) == long_str

def test_decode_cyclic_repeating_pattern():
    assert decode_cyclic("abcabcabc") == "cabcabcab"
    assert decode_cyclic("123123123") == "312312312"

def test_decode_cyclic_mixed_case():
    assert decode_cyclic("AbCdEfGhI") == "CAbfdEIGh"

def test_decode_cyclic_numbers_and_letters():
    assert decode_cyclic("a1b2c3d4e5") == "ba132ced45"