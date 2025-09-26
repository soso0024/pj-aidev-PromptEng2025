# Test cases for HumanEval/45
# Generated using Claude API



def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """

    return a * h / 2.0


# Generated test cases:
import pytest

def test_triangle_area_positive_values():
    assert triangle_area(5, 10) == 25.0
    assert triangle_area(3.5, 7.2) == 12.6

def test_triangle_area_zero_values():
    assert triangle_area(0, 10) == 0.0
    assert triangle_area(5, 0) == 0.0

def test_triangle_area_negative_values():
    with pytest.raises(ValueError):
        triangle_area(-5, 10)
    with pytest.raises(ValueError):
        triangle_area(5, -10)

@pytest.mark.parametrize("a, h, expected", [
    (5, 10, 25.0),
    (3.5, 7.2, 12.6),
    (0, 10, 0.0),
    (5, 0, 0.0),
    (-5, 10, pytest.raises(ValueError)),
    (5, -10, pytest.raises(ValueError))
])
def test_triangle_area_parametrized(a, h, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            triangle_area(a, h)
    else:
        assert triangle_area(a, h) == expected