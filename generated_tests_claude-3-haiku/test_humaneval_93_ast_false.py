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

def test_encode_empty_string():
    assert encode('') == ''

@pytest.mark.parametrize("message,expected", [
    ('Hello World', 'hGLLQ wQRLD'),
    ('Python is awesome', 'pYTHQN KS CWGSQMG'),
    ('ENCODE THIS MESSAGE', 'gncqdg thks mgsscgg'),
    ('123 abc DEF', '123 CBC dgf')
])
def test_encode_normal_cases(message, expected):
    assert encode(message) == expected

def test_encode_non_string_input():
    with pytest.raises(TypeError):
        encode(123)