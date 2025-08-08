# Test cases for HumanEval/124
# Generated using Claude API


def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """

    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True


# Generated test cases:
import pytest

@pytest.mark.parametrize("date,expected", [
    ("03-11-2000", True),    # Valid date
    ("15-01-2012", False),   # Invalid month
    ("04-0-2040", False),    # Invalid day
    ("06-04-2020", True),    # Valid date
    ("06/04/2020", False),   # Wrong separator
    ("", False),             # Empty string
    ("13-01-2020", False),   # Month > 12
    ("00-01-2020", False),   # Month < 1
    ("01-32-2020", False),   # Day > 31 for January
    ("04-31-2020", False),   # Day > 30 for April
    ("02-30-2020", False),   # Day > 29 for February
    ("02-29-2020", True),    # Valid leap year date
    ("02-01-2020", True),    # Valid February date
    ("12-31-2020", True),    # Valid December date
    ("04-30-2020", True),    # Valid April date
    ("abc-01-2020", False),  # Invalid month format
    ("01-abc-2020", False),  # Invalid day format
    ("01-01-abcd", False),   # Invalid year format
    ("01-01-2020-", False),  # Extra separator
    ("01--01-2020", False),  # Double separator
    (" 01-01-2020 ", True),  # Spaces around valid date
    ("01-1-2020", True),     # Single digit day is valid
    ("1-01-2020", True),     # Single digit month is valid
])
def test_valid_date_parametrized(date, expected):
    assert valid_date(date) == expected

def test_valid_date_none_input():
    assert valid_date(None) == False

def test_valid_date_non_string_input():
    assert valid_date(12345) == False
    assert valid_date(1.234) == False
    assert valid_date([]) == False
    assert valid_date({}) == False