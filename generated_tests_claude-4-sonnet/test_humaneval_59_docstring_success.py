# Test cases for HumanEval/59
# Generated using Claude API



def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest


# Generated test cases:
import pytest

def largest_prime_factor(n: int):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

@pytest.mark.parametrize("n,expected", [
    (4, 2),
    (6, 3),
    (8, 2),
    (9, 3),
    (10, 5),
    (12, 3),
    (14, 7),
    (15, 5),
    (16, 2),
    (18, 3),
    (20, 5),
    (21, 7),
    (22, 11),
    (24, 3),
    (25, 5),
    (26, 13),
    (27, 3),
    (28, 7),
    (30, 5),
    (32, 2),
    (33, 11),
    (34, 17),
    (35, 7),
    (36, 3),
    (38, 19),
    (39, 13),
    (40, 5),
    (42, 7),
    (44, 11),
    (45, 5),
    (46, 23),
    (48, 3),
    (49, 7),
    (50, 5),
    (51, 17),
    (52, 13),
    (54, 3),
    (55, 11),
    (56, 7),
    (57, 19),
    (58, 29),
    (60, 5),
    (62, 31),
    (63, 7),
    (64, 2),
    (65, 13),
    (66, 11),
    (68, 17),
    (69, 23),
    (70, 7),
    (72, 3),
    (74, 37),
    (75, 5),
    (76, 19),
    (77, 11),
    (78, 13),
    (80, 5),
    (81, 3),
    (82, 41),
    (84, 7),
    (85, 17),
    (86, 43),
    (87, 29),
    (88, 11),
    (90, 5),
    (91, 13),
    (92, 23),
    (93, 31),
    (94, 47),
    (95, 19),
    (96, 3),
    (98, 7),
    (99, 11),
    (100, 5),
    (102, 17),
    (104, 13),
    (105, 7),
    (106, 53),
    (108, 3),
    (110, 11),
    (111, 37),
    (112, 7),
    (114, 19),
    (115, 23),
    (116, 29),
    (117, 13),
    (118, 59),
    (119, 17),
    (120, 5),
    (121, 11),
    (122, 61),
    (123, 41),
    (124, 31),
    (125, 5),
    (126, 7),
    (128, 2),
    (129, 43),
    (130, 13),
    (132, 11),
    (133, 19),
    (134, 67),
    (135, 5),
    (136, 17),
    (138, 23),
    (140, 7),
    (141, 47),
    (142, 71),
    (143, 13),
    (144, 3),
    (145, 29),
    (146, 73),
    (147, 7),
    (148, 37),
    (150, 5),
    (152, 19),
    (153, 17),
    (154, 11),
    (155, 31),
    (156, 13),
    (158, 79),
    (159, 53),
    (160, 5),
    (161, 23),
    (162, 3),
    (164, 41),
    (165, 11),
    (166, 83),
    (168, 7),
    (169, 13),
    (170, 17),
    (171, 19),
    (172, 43),
    (174, 29),
    (175, 7),
    (176, 11),
    (177, 59),
    (178, 89),
    (180, 5),
    (182, 13),
    (183, 61),
    (184, 23),
    (185, 37),
    (186, 31),
    (187, 17),
    (188, 47),
    (189, 7),
    (190, 19),
    (192, 3),
    (194, 97),
    (195, 13),
    (196, 7),
    (198, 11),
    (200, 5),
    (13195, 29),
    (2048, 2),
])
def test_largest_prime_factor_parametrized(n, expected):
    assert largest_prime_factor(n) == expected

def test_largest_prime_factor_small_composites():
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(6) == 3
    assert largest_prime_factor(8) == 2
    assert largest_prime_factor(9) == 3

def test_largest_prime_factor_powers_of_two():
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(8) == 2
    assert largest_prime_factor(16) == 2
    assert largest_prime_factor(32) == 2
    assert largest_prime_factor(64) == 2
    assert largest_prime_factor(128) == 2
    assert largest_prime_factor(256) == 2
    assert largest_prime_factor(512) == 2
    assert largest_prime_factor(1024) == 2
    assert largest_prime_factor(2048) == 2

def test_largest_prime_factor_powers_of_three():
    assert largest_prime_factor(9) == 3
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(81) == 3
    assert largest_prime_factor(243) == 3

def test_largest_prime_factor_semiprimes():
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(6) == 3
    assert largest_prime_factor(10) == 5
    assert largest_prime_factor(14) == 7
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(21) == 7
    assert largest_prime_factor(22) == 11
    assert largest_prime_factor(26) == 13
    assert largest_prime_factor(33) == 11
    assert largest_prime_factor(34) == 17
    assert largest_prime_factor(35) == 7
    assert largest_prime_factor(38) == 19
    assert largest_prime_factor(39) == 13

def test_largest_prime_factor_large_numbers():
    assert largest_prime_factor(1000) == 5
    assert largest_prime_factor(1001) == 13
    assert largest_prime_factor(1002) == 167
    assert largest_prime_factor(1003) == 59
    assert largest_prime_factor(1004) == 251