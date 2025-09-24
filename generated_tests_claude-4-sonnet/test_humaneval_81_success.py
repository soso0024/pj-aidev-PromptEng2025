# Test cases for HumanEval/81
# Generated using Claude API


def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """


   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade


# Generated test cases:
import pytest

def numerical_letter_grade(grades):
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade

def test_empty_list():
    assert numerical_letter_grade([]) == []

def test_single_grade_a_plus():
    assert numerical_letter_grade([4.0]) == ["A+"]

def test_single_grade_a():
    assert numerical_letter_grade([3.8]) == ["A"]

def test_single_grade_a_minus():
    assert numerical_letter_grade([3.4]) == ["A-"]

def test_single_grade_b_plus():
    assert numerical_letter_grade([3.1]) == ["B+"]

def test_single_grade_b():
    assert numerical_letter_grade([2.8]) == ["B"]

def test_single_grade_b_minus():
    assert numerical_letter_grade([2.4]) == ["B-"]

def test_single_grade_c_plus():
    assert numerical_letter_grade([2.1]) == ["C+"]

def test_single_grade_c():
    assert numerical_letter_grade([1.8]) == ["C"]

def test_single_grade_c_minus():
    assert numerical_letter_grade([1.4]) == ["C-"]

def test_single_grade_d_plus():
    assert numerical_letter_grade([1.1]) == ["D+"]

def test_single_grade_d():
    assert numerical_letter_grade([0.8]) == ["D"]

def test_single_grade_d_minus():
    assert numerical_letter_grade([0.1]) == ["D-"]

def test_single_grade_e():
    assert numerical_letter_grade([0.0]) == ["E"]

def test_boundary_values():
    assert numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]) == ["A+", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

def test_just_above_boundaries():
    assert numerical_letter_grade([3.71, 3.31, 3.01, 2.71, 2.31, 2.01, 1.71, 1.31, 1.01, 0.71, 0.01]) == ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-"]

def test_negative_grade():
    assert numerical_letter_grade([-1.0]) == ["E"]

def test_multiple_negative_grades():
    assert numerical_letter_grade([-2.5, -0.5, -10.0]) == ["E", "E", "E"]

def test_mixed_grades():
    assert numerical_letter_grade([4.0, 2.5, 1.0, 0.0]) == ["A+", "B-", "D", "E"]

def test_all_same_grade():
    assert numerical_letter_grade([3.5, 3.5, 3.5]) == ["A-", "A-", "A-"]

def test_decimal_precision():
    assert numerical_letter_grade([3.999, 3.701, 3.301]) == ["A", "A", "A-"]

@pytest.mark.parametrize("gpa,expected", [
    (4.0, "A+"),
    (3.9, "A"),
    (3.8, "A"),
    (3.7, "A-"),
    (3.6, "A-"),
    (3.4, "A-"),
    (3.3, "B+"),
    (3.2, "B+"),
    (3.0, "B"),
    (2.9, "B"),
    (2.7, "B-"),
    (2.6, "B-"),
    (2.3, "C+"),
    (2.2, "C+"),
    (2.0, "C"),
    (1.9, "C"),
    (1.7, "C-"),
    (1.6, "C-"),
    (1.3, "D+"),
    (1.2, "D+"),
    (1.0, "D"),
    (0.9, "D"),
    (0.7, "D-"),
    (0.5, "D-"),
    (0.0, "E"),
    (-1.0, "E")
])
def test_individual_grades(gpa, expected):
    assert numerical_letter_grade([gpa]) == [expected]

def test_large_list():
    grades = [4.0] * 100 + [2.5] * 50 + [0.0] * 25
    expected = ["A+"] * 100 + ["B-"] * 50 + ["E"] * 25
    assert numerical_letter_grade(grades) == expected

def test_floating_point_edge_cases():
    assert numerical_letter_grade([3.7000001]) == ["A"]
    assert numerical_letter_grade([3.6999999]) == ["A-"]
