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
    assert remove_vowels('') == ''

@pytest.mark.parametrize("input_text,expected_output", [
    ("abcdef\nghijklm", "bcdf\nghjklm"),
    ("abcdef", "bcdf"),
    ("aaaaa", ""),
    ("aaBAA", "B"),
    ("zbcd", "zbcd")
])
def test_remove_vowels(input_text, expected_output):
    assert remove_vowels(input_text) == expected_output

def test_remove_vowels_non_string_input():
    with pytest.raises(TypeError):
        remove_vowels(123)
