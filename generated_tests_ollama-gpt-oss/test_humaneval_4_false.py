# Test cases for HumanEval/4
# Generated using Claude API

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


# Generated test cases:
import os
import importlib.util
import pytest
from typing import List

# Dynamically load the solution module from the parent directory
solution_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'solution.py'))
spec = importlib.util.spec_from_file_location('solution', solution_path)
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)
mean_absolute_deviation = solution.mean_absolute_deviation

@pytest.mark.parametrize(
    "numbers,expected",
    [
        ([1, 3], 1.0),
        ([-1, -3], 1.0),
        ([1.5, 2.5, 3.5], 2/3),
        ([1, 2, 4], 10/9),
        ([1e-3, 1e-2, 1e-1], 0.04111111111111111),
    ]
)
def test_mean_absolute_deviation(numbers: List[float], expected: float):
    assert mean_absolute_deviation(numbers) == pytest.approx(expected)