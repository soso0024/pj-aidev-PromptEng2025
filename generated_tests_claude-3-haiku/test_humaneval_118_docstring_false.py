# Test cases for HumanEval/118
# Generated using Claude API


def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", 'O', 'U', 'I'}
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if (word[i+1] not in vowels) and (word[i-1] not in vowels):
                return word[i]
    return ""


# Generated test cases:
from your_module import get_closest_vowel

import pytest

@pytest.mark.parametrize("word,expected", [
    ("yogurt", "u"),
    ("FULL", "U"),
    ("quick", ""),
    ("ab", ""),
    ("hello", "e"),
    ("WORLD", "O"),
    ("Python", ""),
    ("aeiou", ""),
    ("a", ""),
    ("", ""),
    ("hello world", "o"),
    ("QUICK BROWN FOX", "O"),
    ("aBcDeFgHiJkLmNoPqRsTuVwXyZ", "U")
])
def test_get_closest_vowel(word, expected):
    assert get_closest_vowel(word) == expected