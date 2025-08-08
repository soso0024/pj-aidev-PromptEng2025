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
from typing import Any

@pytest.mark.parametrize("input_str,expected", [
    ("Hello world", 0),
    ("The sky is blue. The sun is shining. I love this weather", 1),
    ("I am bored. I am really bored!", 2),
    ("", 0),
    ("I am", 1),
    ("i am not counted. I am counted.", 1),
    ("Hello! I am here? I see you. I know.", 3),
    ("This is not. But I am. However this isn't. I see.", 1),
    ("I am.I am.I am.", 3),
    ("I am? I am! I am.", 3),
    ("Not a boredom. Still not. Never will be.", 0),
    ("This sentence ends oddly.? I am here!", 1),
    ("I'm not counted. I am counted.", 1),
    ("In this case. I in middle. Inside I.", 1),
    ("I  am spaced.I am not spaced.", 2),
])
def test_is_bored_parametrized(input_str: str, expected: int) -> None:
    assert is_bored(input_str) == expected

def test_is_bored_empty_string() -> None:
    assert is_bored("") == 0

def test_is_bored_single_char() -> None:
    assert is_bored("I am") == 1

def test_is_bored_multiple_delimiters() -> None:
    assert is_bored("I am here!!! I am here... I am here???") == 3

def test_is_bored_no_spaces() -> None:
    assert is_bored("I am.I am.I am") == 3

def test_is_bored_extra_spaces() -> None:
    assert is_bored("I   am   here.    I    am here.") == 2

def test_is_bored_mixed_case() -> None:
    assert is_bored("i am not counted. I am counted. i still not.") == 1

@pytest.mark.parametrize("input_str", [None, 123, [], {}])
def test_is_bored_invalid_input(input_str: Any) -> None:
    with pytest.raises((AttributeError, TypeError)):
        is_bored(input_str)