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

def do_algebra(operator, operand):
    if len(operand) < 2:
        raise ValueError("At least two operands are required")
    if len(operator) != len(operand) - 1:
        raise ValueError("Number of operators must be one less than number of operands")

    result = operand[0]
    for oprt, oprn in zip(operator, operand[1:]):
        if oprt == '+':
            result += oprn
        elif oprt == '-':
            result -= oprn
        elif oprt == '*':
            result *= oprn
        elif oprt == '//':
            result //= oprn
        elif oprt == '**':
            result **= oprn
    return result

def test_do_algebra_basic_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_do_algebra_multiple_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_subtraction():
    assert do_algebra(['-'], [10, 5]) == 5

def test_do_algebra_multiplication():
    assert do_algebra(['*'], [3, 4]) == 12

def test_do_algebra_floor_division():
    assert do_algebra(['//'], [10, 3]) == 3

def test_do_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_complex_expression():
    assert do_algebra(['+', '*', '**'], [2, 3, 4, 5]) == 29

@pytest.mark.parametrize("operators,operands,expected", [
    (['+'], [1, 2], 3),
    (['-'], [10, 5], 5),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    (['+', '*'], [2, 3, 4], 14),
    (['+', '-'], [10, 5, 3], 2),
])
def test_do_algebra_parametrized(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_single_operand_raises_error():
    with pytest.raises(ValueError):
        do_algebra(['+'], [5])

def test_do_algebra_empty_lists_raises_error():
    with pytest.raises(ValueError):
        do_algebra([], [])

def test_do_algebra_mismatched_lengths_raises_error():
    with pytest.raises(ValueError):
        do_algebra(['+', '-'], [1, 2, 3])