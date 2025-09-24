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

def compare(game, guess):
    return [abs(x-y) for x,y in zip(game,guess)]

def test_compare_exact_matches():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_no_matches():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed_results():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_second_example():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_empty_arrays():
    assert compare([], []) == []

def test_compare_single_element_match():
    assert compare([5], [5]) == [0]

def test_compare_single_element_no_match():
    assert compare([5], [3]) == [2]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -5, 0]) == [0, 3, 3]

def test_compare_mixed_positive_negative():
    assert compare([1, -2, 3], [-1, 2, -3]) == [2, 4, 6]

def test_compare_zeros():
    assert compare([0, 0, 0], [0, 1, -1]) == [0, 1, 1]

def test_compare_large_numbers():
    assert compare([100, 200], [150, 180]) == [50, 20]

def test_compare_floating_point():
    result = compare([1.5, 2.7], [1.2, 3.0])
    expected = [0.3, 0.3]
    assert len(result) == len(expected)
    for i in range(len(result)):
        assert abs(result[i] - expected[i]) < 1e-10

@pytest.mark.parametrize("game,guess,expected", [
    ([1], [1], [0]),
    ([5], [2], [3]),
    ([0], [0], [0]),
    ([-5], [5], [10]),
    ([10, 20], [15, 25], [5, 5])
])
def test_compare_parametrized(game, guess, expected):
    assert compare(game, guess) == expected