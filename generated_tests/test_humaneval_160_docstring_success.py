# Test cases for HumanEval/160
# Generated using Claude API


def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


# Generated test cases:
import pytest

@pytest.mark.parametrize("operator,operand,expected", [
    (["+", "*", "-"], [2, 3, 4, 5], 9),
    (["+"], [1, 2], 3),
    (["*"], [5, 2], 10),
    (["-"], [10, 5], 5),
    (["//"], [10, 2], 5),
    (["**"], [2, 3], 8),
    (["+", "+"], [1, 2, 3], 6),
    (["*", "*"], [2, 3, 4], 24),
    (["+", "*"], [2, 3, 4], 14),
    (["**", "//"], [2, 3, 2], 4),
    (["+", "-", "*", "//"], [5, 3, 2, 4, 2], 4),
    (["*", "*", "*"], [1, 2, 3, 4], 24),
    (["+", "+", "+"], [1, 1, 1, 1], 4),
    (["**", "**"], [2, 2, 2], 16),
])
def test_do_algebra_valid_cases(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

def test_do_algebra_single_operation():
    assert do_algebra(["+"], [1, 1]) == 2

def test_do_algebra_complex_expression():
    assert do_algebra(["+", "*", "**", "//"], [2, 3, 4, 2, 3]) == 18

@pytest.mark.parametrize("operator,operand", [
    (["+"], []),
    (None, None),
])
def test_do_algebra_invalid_inputs(operator, operand):
    with pytest.raises((IndexError, TypeError)):
        do_algebra(operator, operand)

@pytest.mark.parametrize("operator,operand", [
    (["/"], [1, 0]),
    (["//"], [1, 0]),
])
def test_do_algebra_division_by_zero(operator, operand):
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_do_algebra_large_numbers():
    assert do_algebra(["*", "*"], [999, 999, 999]) == 997002999

def test_do_algebra_zero_operands():
    assert do_algebra(["+", "*"], [0, 0, 5]) == 0

def test_do_algebra_same_operators():
    assert do_algebra(["+", "+", "+"], [1, 2, 3, 4]) == 10