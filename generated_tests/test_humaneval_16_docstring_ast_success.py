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

def test_basic_string():
    assert count_distinct_characters("hello") == 4

def test_empty_string():
    assert count_distinct_characters("") == 0

def test_all_same_character():
    assert count_distinct_characters("aaaa") == 1

def test_case_insensitive():
    assert count_distinct_characters("aAaA") == 1
    assert count_distinct_characters("aBcAbC") == 3

def test_special_characters():
    assert count_distinct_characters("!@#$%") == 5
    assert count_distinct_characters("a!a@a#") == 4

def test_numbers():
    assert count_distinct_characters("123123") == 3

def test_spaces():
    assert count_distinct_characters("a b c") == 4

@pytest.mark.parametrize("input_str,expected", [
    ("hello world", 8),
    ("Python3.8!", 10),
    ("aAaAbBbB", 2),
    ("    ", 1),
    ("12!@aA", 5),
    ("ZzYyXx", 3),
    (".,;:!?", 6),
    ("a1A1b2B2", 4)
])
def test_various_inputs(input_str, expected):
    assert count_distinct_characters(input_str) == expected

def test_unicode_characters():
    assert count_distinct_characters("üüÜÜ") == 1
    assert count_distinct_characters("αβγΑΒΓ") == 3

def test_mixed_string():
    assert count_distinct_characters("Hello123!@#") == 10

def test_single_character():
    assert count_distinct_characters("x") == 1

def test_alternating_case():
    assert count_distinct_characters("aAbBcC") == 3