# Test cases for HumanEval/91
# Generated using Claude API


def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


# Generated test cases:
import pytest
import re

def is_bored(S):
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence.strip() and sentence[0:2] == 'I ' for sentence in sentences)

def test_is_bored_basic_cases():
    assert is_bored("I love coding. This is fun.") == 1
    assert is_bored("I am happy! I am excited.") == 2
    assert is_bored("Hello world. Nothing special here.") == 0

def test_is_bored_empty_string():
    assert is_bored("") == 0

def test_is_bored_multiple_punctuation():
    assert is_bored("I love coding! I am great? I am awesome.") == 3

def test_is_bored_case_sensitive():
    assert is_bored("i am not bored. I am bored.") == 1

def test_is_bored_mixed_punctuation():
    assert is_bored("Hello! I am here. What is up? I am fine.") == 2

@pytest.mark.parametrize("input_string,expected", [
    ("I am testing. This is a test.", 1),
    ("No bored sentences here.", 0),
    ("I like coding! I enjoy programming.", 2),
    ("", 0),
    ("I.", 1),
    ("Not starting with I.", 0)
])
def test_is_bored_parametrized(input_string, expected):
    assert is_bored(input_string) == expected