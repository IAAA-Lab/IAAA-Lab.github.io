"""Provides several functions to work with dates.

In particular, it provides the functions needed for getting the date following
a given particular date.

Types:
    Date

Functions:

    is_leap_year(year: int) -> bool
    days_in_month(month: int, year: int) -> int
    next_day_as_date(date: Date) -> Date
    standardize_separators(date: str) -> str
    from_string(date: str) -> Date
    to_string(date: Date) -> str
    next_day(date: str) -> str

Constants:
    GREGORIAN_START_YEAR

Examples of use:
>>> next_day('1-7-2024')
'2-7-2024'

>>> next_day('28-7-2024')
'29-7-2024'
>>> next_day('29-7-2024')
'30-7-2024'
>>> next_day('30-7-2024')
'31-7-2024'
>>> next_day('31-7-2024')
'1-8-2024'

>>> next_day('28-9-2024')
'29-9-2024'
>>> next_day('29-9-2024')
'30-9-2024'
>>> next_day('30-9-2024')
'1-10-2024'

>>> next_day('28-2-2024')
'29-2-2024'
>>> next_day('29-2-2024')
'1-3-2024'

>>> next_day('28-2-2025')
'1-3-2025'

>>> next_day('31-12-2024')
'1-1-2025'

>>> next_day('0-7-2024')
Traceback (most recent call last):
...
ValueError: Day must be between 1 and 31.

>>> next_day('32-7-2024')
Traceback (most recent call last):
...
ValueError: Day must be between 1 and 31.
>>> next_day('31-9-2024')
Traceback (most recent call last):
...
ValueError: Day must be between 1 and 30.
>>> next_day('30-2-2024')
Traceback (most recent call last):
...
ValueError: Day must be between 1 and 29.
>>> next_day('29-2-2025')
Traceback (most recent call last):
...
ValueError: Day must be between 1 and 28.

>>> next_day('30-0-2024')
Traceback (most recent call last):
...
ValueError: Month must be between 1 and 12.
>>> next_day('30-13-2024')
Traceback (most recent call last):
...
ValueError: Month must be between 1 and 12.

>>> next_day('1-7-1582')
Traceback (most recent call last):
...
ValueError: Year must be greater than 1582.

>>> next_day('1-7-2024-12-00-00')
Traceback (most recent call last):
...
ValueError: Wrong format
>>> next_day('1-7')
Traceback (most recent call last):
...
ValueError: Wrong format

>>> next_day('1/7/2024')
'2-7-2024'
>>> next_day('1.7.2024')
'2-7-2024'
"""

from typing import Callable, Final, NamedTuple

GREGORIAN_START_YEAR: Final = 1582
ERROR_MSG_DAY: Final = "Day must be between 1 and"
ERROR_MSG_MONTH: Final = "Month must be between 1 and 12."
ERROR_MSG_YEAR: Final = f"Year must be greater than {GREGORIAN_START_YEAR}."
ERROR_MSG_FORMAT: Final = "Wrong format"
SEP_STD: Final = "-"
SEP_ALT_1: Final = "/"
SEP_ALT_2: Final = "."


class Date(NamedTuple):
    day: int
    month: int
    year: int


def is_leap_year(year: int) -> bool:
    """Return whether the argument is a leap year.

    Args:
        year: a year posterior to the adoption of the Gregorian calendar (1582)

    Returns:
        True if the year is leap according to the Gregorian calendar,
        False otherwise.
    """

    multiple_of_4 = year % 4 == 0
    multiple_of_100 = year % 100 == 0
    multiple_of_400 = year % 400 == 0
    return multiple_of_400 or (multiple_of_4 and not multiple_of_100)


def days_in_month(month: int, year: int) -> int:
    """Return the number of days of a month in a certain year.

    Args:
        month: the month we are interested in. Must be in the interval [1, 12].
        year: the year of the month. Must be posterior to 1582.

    Returns:
        the number of days that provided month has in the provided year.
    """
    if month == 2:
        # Febrero: el número de día depende del año
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in (4, 6, 9, 11):
        # Abril, junio, septiembre o noviembre
        return 30
    else:
        # Resto de meses
        return 31


def next_day_as_date(date: Date) -> Date:
    """Return a Date representing one day after the argument date.

    Args:
        date: a Date representing a date in the form (day, month, year).
        The date must be valid.

    Returns:
        A Date representing one day after the argument date.
        For example:
        >>> next_day_as_date(Date(1, 7, 2024))
        Date(day=2, month=7, year=2024)
    """

    day, month, year = date
    day += 1
    if day > days_in_month(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return Date(day, month, year)


def previous_day_as_date(date: Date) -> Date:
    """Return a Date representing one day before the argument date.

    Args:
        date: a Date representing a date in the form (day, month, year).
        The date must be valid.

    Returns:
        A Date representing one day before the argument date.
        For example:
        >>> previous_day_as_date(Date(1, 7, 2024))
        Date(day=30, month=6, year=2024)
        >>> previous_day_as_date(Date(1, 1, 2024))
        Date(day=31, month=12, year=2023)
        >>> previous_day_as_date(Date(1, 3, 2024))
        Date(day=29, month=2, year=2024)
    """

    day, month, year = date
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            year -= 1
            month = 12
        day = days_in_month(month, year)
    return Date(day, month, year)


def standardize_separators(date: str) -> str:
    """Return a date with standard separators one

    Args:
        date: a string date in the format 'day-month-year' that may use
        '/' or '.' as alternative item separators.

    Returns:
        A date with items separated only with the standard separator '-'
    """

    return date.replace(SEP_ALT_1, SEP_STD).replace(SEP_ALT_2, SEP_STD)


def from_string(date: str) -> Date:
    """Return an equivalent Date of the given string that represents a date.

    Given a string representing a date, if it is correct returns an
    equivalent Date. Otherwise, raises a ValueError

    Args:
        date: a string date in the format 'day-month-year'

    Returns:
        An equivalent Date (day, month, year)

    Raises:
        ValueError when the string does not represent a valid date
    """

    tokens = standardize_separators(date).split(SEP_STD)
    if len(tokens) != 3:
        raise ValueError(ERROR_MSG_FORMAT)

    day = int(tokens[0])
    month = int(tokens[1])
    year = int(tokens[2])
    if month < 1 or month > 12:
        raise ValueError(ERROR_MSG_MONTH)
    if year <= GREGORIAN_START_YEAR:
        raise ValueError(ERROR_MSG_YEAR)
    if day < 1 or day > days_in_month(month, year):
        raise ValueError(f"{ERROR_MSG_DAY} {days_in_month(month, year)}.")

    return Date(day, month, year)


def to_string(date: Date) -> str:
    """Return a string representing the given date

    Args:
        date: a Date

    Returns:
        A string representing the given date in 'day-month-year' format.
    """

    return f"{date.day}{SEP_STD}{date.month}{SEP_STD}{date.year}"


def transform_day(date: str, transform: Callable[[Date], Date]) -> str:
    """Return a string representing a transformation on the argument date.

    Args:
        date: a string representing a date in the form 'day-month-year'
        transform: a callable transforming Dates

    Returns:
        A string representing the transformed date
    """

    return to_string(transform(from_string(date)))


def next_day(date: str) -> str:
    """Return a string representing one day after the argument date.

    Args:
        date: a string representing a date in the form 'day-month-year'

    Returns:
        A string representing one day after the given date
    """
    return transform_day(date, next_day_as_date)


def previous_day(date: str) -> str:
    """Return a string representing one day before the argument date.

    Args:
        date: a string representing a date in the form 'day-month-year'

    Returns:
        A string representing one day before the given date
    """
    return transform_day(date, previous_day_as_date)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
