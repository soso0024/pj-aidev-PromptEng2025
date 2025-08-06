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
import pytest

@pytest.mark.parametrize("word,expected", [
    ("yogurt", "u"),
    ("FULL", "U"),
    ("quick", ""),
    ("ab", ""),
    ("", ""),
    ("aei", ""),
    ("hello", "e"),
    ("HELLO", "E"),
    ("world", "o"),
    ("WORLD", "O"),
    ("rhythm", ""),
    ("AeIoU", ""),
    ("cAt", "A"),
    ("dOg", "O"),
    ("spaces between", "e"),
    ("UPPERCASE", "A"),
    ("lowercase", "a"),
    ("aeiou", ""),
    ("AEIOU", ""),
    ("consonant", "a"),
    ("xyz", ""),
    ("a", ""),
    ("E", ""),
    ("complex", "e"),
    ("COMPLEX", "E"),
    ("middle", "i"),
    ("MIDDLE", "I"),
    ("testing", "i"),
    ("TESTING", "I"),
    ("simple", "i"),
    ("SIMPLE", "I")
])
def test_get_closest_vowel(word, expected):
    assert get_closest_vowel(word) == expected

def test_get_closest_vowel_empty_string():
    assert get_closest_vowel("") == ""

def test_get_closest_vowel_single_char():
    assert get_closest_vowel("a") == ""

def test_get_closest_vowel_two_chars():
    assert get_closest_vowel("ab") == ""

def test_get_closest_vowel_all_consonants():
    assert get_closest_vowel("rhythm") == ""

def test_get_closest_vowel_all_vowels():
    assert get_closest_vowel("aeiou") == ""

def test_get_closest_vowel_case_sensitivity():
    assert get_closest_vowel("mIddle") == "I"
    assert get_closest_vowel("middle") == "i"

def test_get_closest_vowel_multiple_valid_vowels():
    assert get_closest_vowel("testament") == "e"

def test_get_closest_vowel_vowels_at_edges():
    assert get_closest_vowel("audio") == ""