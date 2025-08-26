# Test cases for HumanEval/17
# Generated using Claude API

from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]


# Generated test cases:
import pytest

def test_parse_music_basic_notes():
    assert parse_music('o o| .|') == [4, 2, 1]

def test_parse_music_empty_string():
    assert parse_music('') == []

def test_parse_music_single_note():
    assert parse_music('o') == [4]

def test_parse_music_multiple_notes():
    assert parse_music('o o o| .| o|') == [4, 4, 2, 1, 2]

def test_parse_music_extra_whitespace():
    assert parse_music('  o   o|  .|  ') == [4, 2, 1]

@pytest.mark.parametrize("input_string,expected", [
    ('o o| .|', [4, 2, 1]),
    ('o o o', [4, 4, 4]),
    ('o| o| o|', [2, 2, 2]),
    ('.|', [1])
])
def test_parse_music_parametrized(input_string, expected):
    assert parse_music(input_string) == expected

def test_parse_music_invalid_note():
    with pytest.raises(KeyError):
        parse_music('x')
