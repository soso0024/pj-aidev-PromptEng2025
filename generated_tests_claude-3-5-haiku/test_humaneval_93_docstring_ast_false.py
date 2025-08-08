# Test cases for HumanEval/93
# Generated using Claude API


def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])


# Generated test cases:
import pytest

def test_encode_basic_cases():
    assert encode('test') == 'TGST'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'

@pytest.mark.parametrize("input_str,expected", [
    ('hello', 'HGLLM'),
    ('WORLD', 'world'),
    ('Python', 'pYTHMN'),
    ('aeiou', 'CGKMU'),
    ('AEIOU', 'cgkmu')
])
def test_encode_parametrized(input_str, expected):
    assert encode(input_str) == expected

def test_encode_mixed_case():
    assert encode('MiXeD CaSe') == 'mKxGD cCSG'

def test_encode_empty_string():
    assert encode('') == ''

def test_encode_special_characters():
    assert encode('123!@#') == '123!@#'

def test_encode_spaces():
    assert encode('hello world') == 'HGLLM WMRLD'