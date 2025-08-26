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

def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""

def test_remove_vowels_no_vowels():
    assert remove_vowels("xyz") == "xyz"

def test_remove_vowels_all_vowels():
    assert remove_vowels("aeiou") == ""

def test_remove_vowels_mixed_case():
    assert remove_vowels("aBcEiOu") == "BcO"

@pytest.mark.parametrize("input_text,expected_output", [
    ("Hello, World!", "Hll, Wrld!"),
    ("Python is awesome", "Pythn s wsm"),
    ("I love coding", "lv cdng"),
    ("AEIOUaeiou", ""),
    ("123abc456", "123bc456")
])
def test_remove_vowels_various_inputs(input_text, expected_output):
    assert remove_vowels(input_text) == expected_output

def test_remove_vowels_non_string_input():
    with pytest.raises(TypeError):
        remove_vowels(123)