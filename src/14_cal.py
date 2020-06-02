"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

'''
Understand:
The goal is to implement a function that prints, or displays a calendar from the built in library.
This function can take up to two arguments (along with calling the file).
If no arguments are called it returns the current month and years calendar.
What if more than two arguments are called?
Should I limit the years this function should go to?
What if the year input is more than four digits long?
What if the month input is less than 1 or more than 2 digits long?
What if there are zeros in the incorrect spaces of the arguments?
What do I need from sys sys.args? -> shows arguments from command line
                    calendar calendar.month(year, month) <- does not like months with one digit to have a zero in front 06
                    datetime datetime.today() can I get the year and month from this?

How do I create errors in Python?

arguments: file, [month] [year]
'''

# Planning:

# write function that takes in two arguments, month, year
# month and year should be defaulted to current -> datetime library?


'''
Prints out calendar in console.
parameter: {int} - |optional| month, must be 1-12
parameter: {int} - |optional| year, must be a valid 4 digit that is greater than 0
'''


def print_calendar(month=datetime.now().month, year=datetime.now().year):
    sys_arg_len = len(sys.argv)
    # if sys arguments are greater than three
    if sys_arg_len > 3:
        # return an error, (value error?)
        print(
            'You have more than 3 arguments.\nPlease enter arguments as follows:\npython3 14_cal.py [month 1 - 12] [year 1 - 9999]')
        return

    # value error statement
    general_error = 'Please enter valid arguments:\npython3 14_cal.py [month 1 - 12] [year 1 - 9999]'
    # set args if recieved to corseponding arguments
    if sys_arg_len >= 2:
        month = sys.argv[1]
        # if month or year is not a number
        # return an error
        try:
            # check if month is between 1 - 12
            if 1 <= int(month) < 12:
                month = int(month)
        except ValueError:
            print(general_error)
            return
    if sys_arg_len is 3:
        year = sys.argv[2]
        try:
            # check if month is between 1 - 9999
            if 1 <= int(year) < 9999:
                year = int(year)
        except ValueError:
            print(general_error)
            return

    # print calendar
    print(calendar.month(year, month))


if __name__ == '__main__':
    print_calendar()
