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

@pytest.mark.parametrize("operators,operands,expected", [
    (['+', '-'], [1, 2, 3], 0),
    (['+', '+'], [1, 2, 3], 6),
    (['-', '-'], [10, 5, 3], 2),
    (['*', '//'], [4, 2, 2], 4),
    (['+', '*'], [2, 3, 4], 14),
    (['//', '*'], [12, 3, 2], 8),
    (['+'], [1, 2], 3),
    (['*', '+', '-'], [2, 3, 4, 5], 5),
    (['+', '+', '+'], [1, 1, 1, 1], 4),
    (['*', '*', '*'], [2, 2, 2, 2], 16)
])
def test_do_algebra_valid_cases(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators,operands", [
    ([], []),
    (['+'], []),
    (['+', '+'], [1])
])
def test_do_algebra_invalid_inputs(operators, operands):
    with pytest.raises((IndexError, ValueError)):
        do_algebra(operators, operands)

@pytest.mark.parametrize("operators,operands,expected", [
    (['+', '+'], [-1, -2, -3], -6),
    (['*', '*'], [-2, 3, -4], 24),
    (['-', '//'], [10, -5, 2], 13)
])
def test_do_algebra_negative_numbers(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators,operands,expected", [
    (['+', '//'], [1, 2, 2], 2),
    (['//', '//'], [8, 2, 2], 2),
    (['*', '//'], [2, 2, 2], 2)
])
def test_do_algebra_floating_point(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//', '+'], [1, 0, 1])

@pytest.mark.parametrize("operators,operands", [
    (['$', '+'], [1, 2, 3]),
    (['#', '*'], [1, 2, 3]),
    (['=', '//'], [1, 2, 3])
])
def test_do_algebra_invalid_operators(operators, operands):
    with pytest.raises((SyntaxError, NameError)):
        do_algebra(operators, operands)