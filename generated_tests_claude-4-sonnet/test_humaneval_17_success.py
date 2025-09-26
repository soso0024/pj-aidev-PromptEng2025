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

def parse_music(music_string: str):
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]

def test_empty_string():
    assert parse_music("") == []

def test_single_whole_note():
    assert parse_music("o") == [4]

def test_single_half_note():
    assert parse_music("o|") == [2]

def test_single_quarter_note():
    assert parse_music(".|") == [1]

def test_multiple_same_notes():
    assert parse_music("o o o") == [4, 4, 4]

def test_mixed_notes():
    assert parse_music("o o| .|") == [4, 2, 1]

def test_all_note_types():
    assert parse_music("o o| .| o .| o|") == [4, 2, 1, 4, 1, 2]

def test_extra_spaces():
    assert parse_music("o  o|   .|") == [4, 2, 1]

def test_leading_trailing_spaces():
    assert parse_music(" o o| .| ") == [4, 2, 1]

def test_only_spaces():
    assert parse_music("   ") == []

def test_single_space():
    assert parse_music(" ") == []

@pytest.mark.parametrize("music_string,expected", [
    ("o", [4]),
    ("o|", [2]),
    (".|", [1]),
    ("o o|", [4, 2]),
    ("o| .|", [2, 1]),
    ("o .|", [4, 1]),
    ("o o| .| o", [4, 2, 1, 4])
])
def test_parametrized_valid_inputs(music_string, expected):
    assert parse_music(music_string) == expected

def test_invalid_note_raises_keyerror():
    with pytest.raises(KeyError):
        parse_music("x")

def test_invalid_note_mixed_with_valid():
    with pytest.raises(KeyError):
        parse_music("o x o|")

def test_partial_invalid_note():
    with pytest.raises(KeyError):
        parse_music("o|x")

def test_case_sensitive():
    with pytest.raises(KeyError):
        parse_music("O")

def test_multiple_invalid_notes():
    with pytest.raises(KeyError):
        parse_music("x y z")
