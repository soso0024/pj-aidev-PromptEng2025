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

def test_do_algebra_addition():
    assert do_algebra(['+'], [2, 3]) == 5
    assert do_algebra(['+'], [10, 5]) == 15

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [10, 3]) == 7
    assert do_algebra(['-'], [20, 10]) == 10

def test_do_algebra_multiplication():
    assert do_algebra(['*'], [2, 3]) == 6
    assert do_algebra(['*'], [5, 4]) == 20

def test_do_algebra_division():
    assert do_algebra(['/', 2], [10]) == 5.0
    assert do_algebra(['/', 4], [20]) == 5.0

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '-', '*', '/'], [2, 3, 4, 2]) == 3.0
    assert do_algebra(['-', '*', '+', '/'], [10, 2, 3, 6]) == 7.0

def test_do_algebra_empty_input():
    with pytest.raises(IndexError):
        do_algebra([], [])

def test_do_algebra_invalid_operator():
    with pytest.raises(TypeError):
        do_algebra(['%'], [10, 2])

@pytest.mark.parametrize("operator,operand,expected", [
    (['+'], [2.5, 3.7], 6.2),
    (['-'], [15.0, 7.5], 7.5),
    ['*'], [3.14, 2.0], 6.28),
    (['/'], [10.0, 2.0], 5.0)
])
def test_do_algebra_float_inputs(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

def do_algebra(operator, operand):
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression += oprt + str(oprn)
    return eval(expression)