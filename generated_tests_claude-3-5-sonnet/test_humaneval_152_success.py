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
import math

def test_compare_basic():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

@pytest.mark.parametrize("game,guess,expected", [
    ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
    ([5, 5, 5], [1, 1, 1], [4, 4, 4]),
    ([1, 2, 3], [3, 2, 1], [2, 0, 2]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([10, 20, 30], [5, 15, 25], [5, 5, 5]),
    ([-1, -2, -3], [1, 2, 3], [2, 4, 6]),
    ([0, -5, 10], [0, 5, -10], [0, 10, 20])
])
def test_compare_parametrized(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_single_element():
    assert compare([1], [2]) == [1]

@pytest.mark.xfail(raises=TypeError)
def test_compare_invalid_types():
    compare(['a'], [1])

@pytest.mark.xfail(raises=TypeError)
def test_compare_none_values():
    compare([None], [1])

@pytest.mark.xfail(raises=ValueError)
def test_compare_mismatched_lengths():
    compare([1, 2], [1, 2, 3])

def test_compare_large_numbers():
    assert compare([1000000, 2000000], [1000001, 1999999]) == [1, 1]

def test_compare_floating_point():
    result = compare([1.5, 2.7], [1.3, 2.9])
    assert math.isclose(result[0], 0.2, rel_tol=1e-9)
    assert math.isclose(result[1], 0.2, rel_tol=1e-9)