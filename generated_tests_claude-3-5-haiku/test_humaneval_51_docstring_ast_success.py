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

def test_remove_vowels_multiline_string():
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'

def test_remove_vowels_simple_string():
    assert remove_vowels('abcdef') == 'bcdf'

def test_remove_vowels_only_vowels():
    assert remove_vowels('aaaaa') == ''

def test_remove_vowels_mixed_case():
    assert remove_vowels('aaBAA') == 'B'

def test_remove_vowels_no_vowels():
    assert remove_vowels('zbcd') == 'zbcd'

@pytest.mark.parametrize("input_text,expected", [
    ('hello', 'hll'),
    ('HELLO', 'HLL'),
    ('aEiOu', ''),
    ('Python Programming', 'Pythn Prgrmmng'),
    ('123!@#', '123!@#')
])
def test_remove_vowels_parametrized(input_text, expected):
    assert remove_vowels(input_text) == expected
