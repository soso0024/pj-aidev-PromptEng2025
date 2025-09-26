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
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)

def test_basic_addition():
    assert do_algebra(['+'], [2, 3]) == 5

def test_basic_subtraction():
    assert do_algebra(['-'], [5, 3]) == 2

def test_basic_multiplication():
    assert do_algebra(['*'], [4, 3]) == 12

def test_basic_floor_division():
    assert do_algebra(['//'], [10, 3]) == 3

def test_basic_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_example_case():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_multiple_additions():
    assert do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

def test_multiple_multiplications():
    assert do_algebra(['*', '*', '*'], [2, 3, 4, 5]) == 120

def test_mixed_operations():
    assert do_algebra(['+', '-', '*'], [10, 5, 3, 2]) == 9

def test_exponentiation_priority():
    assert do_algebra(['**', '+'], [2, 3, 1]) == 9

def test_multiplication_priority():
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

def test_floor_division_with_remainder():
    assert do_algebra(['//', '+'], [17, 5, 2]) == 5

def test_zero_operand():
    assert do_algebra(['+'], [0, 5]) == 5

def test_zero_in_multiplication():
    assert do_algebra(['*', '+'], [0, 5, 10]) == 10

def test_zero_in_exponentiation():
    assert do_algebra(['**'], [0, 5]) == 0

def test_one_in_exponentiation():
    assert do_algebra(['**'], [1, 100]) == 1

def test_large_numbers():
    assert do_algebra(['+'], [999999, 1]) == 1000000

def test_complex_expression():
    assert do_algebra(['**', '*', '+', '-'], [2, 3, 4, 5, 10]) == 27

def test_subtraction_to_negative():
    assert do_algebra(['-'], [3, 5]) == -2

def test_floor_division_by_one():
    assert do_algebra(['//'], [42, 1]) == 42

def test_single_digit_operations():
    assert do_algebra(['+', '-', '*', '//'], [9, 1, 2, 3, 2]) == 7

def test_order_of_operations_complex():
    assert do_algebra(['*', '+', '**'], [2, 3, 4, 2]) == 22

def test_minimum_case():
    assert do_algebra(['+'], [1, 1]) == 2

def test_all_zeros_except_last():
    assert do_algebra(['+', '+', '*'], [0, 0, 0, 5]) == 0

def test_exponentiation_zero():
    assert do_algebra(['**'], [5, 0]) == 1