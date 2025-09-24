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

def test_do_algebra_basic():
    assert do_algebra(['+', '-'], [2, 3, 4]) == -5
    assert do_algebra(['*', '/'], [10, 2, 5]) == 1.0

def test_do_algebra_single_operand():
    assert do_algebra(['+'], [42]) == 42
    assert do_algebra(['-'], [100]) == -100

def test_do_algebra_empty_inputs():
    with pytest.raises(IndexError):
        do_algebra([], [])
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

@pytest.mark.parametrize("operators,operands,expected", [
    (['+', '-', '*'], [2, 3, 4, 5], 14),
    (['-', '*', '/'], [100, 10, 5, 2], 10.0),
    (['+', '*'], [1, 2, 3, 4, 5], 45),
    (['-', '/'], [100, 10, 5, 2, 1], 0.5)
])
def test_do_algebra_complex_expressions(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['/', '+'], [10, 0, 5])

def test_do_algebra_invalid_operator():
    with pytest.raises(TypeError):
        do_algebra(['%', '^'], [10, 5])