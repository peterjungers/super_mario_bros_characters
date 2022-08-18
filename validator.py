"""
This module validates all user input. Functions are ordered
alphabetically.
"""


def enter_m(answer):
    while True:
        if answer == "" or answer.upper() == "M":
            return answer.upper()
        else:
            answer = input("Please press the Enter key or enter \"M\": ")


def is_year(value):
    while True:
        try:
            valid = int(value)
            if len(str(valid)) == 4 and valid > 1980:
                return str(valid)
            else:
                raise ValueError
        except ValueError:
            value = input("Please enter a valid year (Hint: the first Mario\n"
                          "game came out in 1981): ")


def menu(option, menu_name):
    while True:
        try:
            valid = int(option)
            if menu_name == "main" and valid > 0 and valid < 10:
                return valid
            elif menu_name == "web_search" and valid > 0 and valid < 4:
                return valid
            else:
                raise ValueError
        except ValueError:
            option = input("Please enter a valid menu number: ")


def not_blank(value, category):
    while True:
        if value != "":
            return value
        else:
            value = input(f"{category} cannot be blank. Please try again: ")


def y_n(answer):
    while True:
        if answer.upper() == "Y" or answer.upper() == "N":
            return answer.upper()
        else:
            answer = input("Please enter \"Y\" or \"N\": ")


def y_n_m(answer):
    while True:
        if answer.upper() == "Y" or answer.upper() == "N" \
                or answer.upper() == "M":
            return answer.upper()
        else:
            answer = input("Please enter \"Y\", \"N\", or \"M\": ")
