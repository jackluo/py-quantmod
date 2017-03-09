"""Refactored Jorge Santos (@jorgesantos) date_tools module."""

import datetime as dt


def get_date_from_today(delta, strfmt='%Y%m%d'):
    """ Returns a string that represents a date n numbers of days from today.
    Parameters:
    -----------
            delta : int
                    number of days
            strfmt : string
                    format in which the date will be represented

    """
    return (dt.date.today() + dt.timedelta(delta)).strftime(strfmt)


def string_to_date(string_date, strfmt='%Y%m%d'):
    """ Converts a string format date into datetime.
    Parameters:
    -----------
            stringDate : string
                    date in string format
            strfmt : string
                    format in which the input date is represented

    """
    return dt.datetime.strptime(string_date, strfmt).date()


def int_to_date(int_date):
    """ Converts an int format date into datetime.
    Parameters:
    -----------
            intDate : int
                    date in int format
    Example:
            intDate(20151023)

    """
    return string_to_date(str(int_date))


def date_to_int(date, strfmt='%Y%m%d'):
    """ Converts a datetime date into int.
    Parameters:
    -----------
            date : datetime
                    date in datetime format
            strfmt : string
                    format in which the int date will be generated
    Example:
            dateToInt(dt.date(2015,10,23),'%Y')

    """
    return int(date.strftime(strfmt))
