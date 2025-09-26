# Test cases for HumanEval/16
# Generated using Claude API



def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))


# Generated test cases:
import pytest

def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

def test_count_distinct_characters_basic():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4

def test_count_distinct_characters_empty_string():
    assert count_distinct_characters('') == 0

def test_count_distinct_characters_single_character():
    assert count_distinct_characters('a') == 1
    assert count_distinct_characters('A') == 1

def test_count_distinct_characters_repeated_characters():
    assert count_distinct_characters('aaa') == 1
    assert count_distinct_characters('AAA') == 1
    assert count_distinct_characters('aAaA') == 1

def test_count_distinct_characters_mixed_case():
    assert count_distinct_characters('AaBbCc') == 3
    assert count_distinct_characters('Hello') == 4
    assert count_distinct_characters('HELLO') == 4
    assert count_distinct_characters('hello') == 4

def test_count_distinct_characters_special_characters():
    assert count_distinct_characters('!@#$%') == 5
    assert count_distinct_characters('a!b@c#') == 6
    assert count_distinct_characters('123') == 3

def test_count_distinct_characters_whitespace():
    assert count_distinct_characters(' ') == 1
    assert count_distinct_characters('a b c') == 4
    assert count_distinct_characters('   ') == 1

def test_count_distinct_characters_numbers():
    assert count_distinct_characters('123456') == 6
    assert count_distinct_characters('112233') == 3

def test_count_distinct_characters_alphanumeric():
    assert count_distinct_characters('abc123ABC') == 6
    assert count_distinct_characters('Test123test') == 6

@pytest.mark.parametrize("input_string,expected", [
    ("", 0),
    ("a", 1),
    ("ab", 2),
    ("aB", 2),
    ("abc", 3),
    ("abcABC", 3),
    ("Hello World", 8),
    ("Programming", 8),
    ("aabbcc", 3),
    ("123abc", 6),
    ("!@#abc", 6),
    ("   abc   ", 4)
])
def test_count_distinct_characters_parametrized(input_string, expected):
    assert count_distinct_characters(input_string) == expected