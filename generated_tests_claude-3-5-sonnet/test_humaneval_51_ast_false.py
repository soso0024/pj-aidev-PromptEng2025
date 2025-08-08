# Test cases for HumanEval/51
# Generated using Claude API



def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """

    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


# Generated test cases:
import pytest

def test_empty_string():
    assert remove_vowels("") == ""

def test_no_vowels():
    assert remove_vowels("rhythm") == "rhythm"

def test_all_vowels():
    assert remove_vowels("aeiou") == ""

def test_mixed_case():
    assert remove_vowels("AeIoU") == ""

@pytest.mark.parametrize("input_str,expected", [
    ("hello", "hll"),
    ("HELLO", "HLL"),
    ("Hello World!", "Hll Wrld!"),
    ("Python3", "Pythn3"),
    ("aAaAaA", ""),
    ("123!@#", "123!@#"),
    ("    ", "    "),
    ("aEiOu", ""),
    ("This is a test", "Ths s  tst"),
    ("UPPER CASE", "PPR CS"),
    ("lower case", "lwr cs"),
    ("12345", "12345"),
    ("!@#$%", "!@#$%"),
    ("Mixed123Case!", "Mxd123Cs!"),
    ("AaEeIiOoUu", "")
])
def test_various_inputs(input_str, expected):
    assert remove_vowels(input_str) == expected

def test_special_characters():
    assert remove_vowels("!@#$%^&*()") == "!@#$%^&*()"

def test_numbers():
    assert remove_vowels("12345") == "12345"

def test_whitespace():
    assert remove_vowels("   ") == "   "

def test_mixed_content():
    assert remove_vowels("Hello123!@#") == "Hll123!@#"

@pytest.mark.parametrize("input_str", [
    None,
    123,
    True,
    3.14
])
def test_invalid_types(input_str):
    with pytest.raises(TypeError):
        remove_vowels(input_str)

def test_list_input():
    with pytest.raises(AttributeError):
        remove_vowels(["hello"])

def test_dict_input():
    with pytest.raises(AttributeError):
        remove_vowels({"key": "value"})