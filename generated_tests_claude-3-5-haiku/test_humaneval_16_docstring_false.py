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

def test_count_distinct_characters_normal_cases():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('hello') == 4
    assert count_distinct_characters('aAaA') == 1

def test_count_distinct_characters_edge_cases():
    assert count_distinct_characters('') == 0
    assert count_distinct_characters(' ') == 1
    assert count_distinct_characters('!!!') == 1
    assert count_distinct_characters('123abc123ABC') == 6

def test_count_distinct_characters_special_characters():
    assert count_distinct_characters('a@b#c$') == 6
    assert count_distinct_characters('Hello, World!') == 7

@pytest.mark.parametrize("input_string,expected", [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    ('hello', 4),
    ('aAaA', 1),
    ('', 0),
    (' ', 1),
    ('!!!', 1),
    ('123abc123ABC', 6),
    ('a@b#c$', 6),
    ('Hello, World!', 7)
])
def test_count_distinct_characters_parametrized(input_string, expected):
    assert count_distinct_characters(input_string) == expected