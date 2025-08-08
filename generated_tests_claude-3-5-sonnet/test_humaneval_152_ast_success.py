# Test cases for HumanEval/152
# Generated using Claude API


def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """

    return [abs(x-y) for x,y in zip(game,guess)]


# Generated test cases:
import pytest

def test_compare_basic():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

@pytest.mark.parametrize("game,guess,expected", [
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    ([5, 5, 5], [5, 5, 5], [0, 0, 0]),
    ([1, 2, 3], [3, 2, 1], [2, 0, 2]),
    ([10, 20, 30], [5, 15, 25], [5, 5, 5]),
    ([0, 0, 0], [1, 1, 1], [1, 1, 1]),
    ([-1, -2, -3], [1, 2, 3], [2, 4, 6]),
    ([100, 200], [99, 201], [1, 1]),
    ([], [], []),
    ([1], [2], [1]),
])
def test_compare_parametrized(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_single_element():
    assert compare([1], [1]) == [0]
    assert compare([0], [10]) == [10]
    assert compare([-5], [5]) == [10]

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]
    assert compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]

def test_compare_mixed_numbers():
    assert compare([-1, 0, 1], [1, 0, -1]) == [2, 0, 2]
    assert compare([-10, 5, -3], [10, -5, 3]) == [20, 10, 6]

@pytest.mark.xfail(raises=TypeError)
def test_compare_invalid_input_types():
    compare("123", [1, 2, 3])

@pytest.mark.xfail(raises=TypeError)
def test_compare_none_input():
    compare(None, [1, 2, 3])

@pytest.mark.xfail(raises=TypeError)
def test_compare_mixed_types():
    compare([1, "2", 3], [1, 2, 3])
