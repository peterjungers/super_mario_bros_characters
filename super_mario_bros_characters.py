# ****************************************************************************
# Author:           Peter Jungers
# Program name:     Super Mario Bros. character database
# Version:          1.0
# Date:             June, July 2022
# Description:      Program allows user to construct database of characters
#                   from Nintendo's Super Mario Bros. games. Database
#                   includes: character name, game in which that character
#                   first made an appearance, year that game was released.
# Main module:      super_mario_bros_characters.py
# Other modules:    data_layer.py, logic_layer.py, options.py, utilities.py,
#                   validator.py
# ****************************************************************************

"""
This is the main module. It contains messages and the main menu.
"""


import time

import options
import utilities
import validator


def welcome():
    subheader = None
    utilities.header(subheader)
    print("This program allows you to create your own database\n"
          "of characters from Nintendo’s Super Mario games. It\n"
          "allows you to enter character names, the game in\n"
          "which each character first appeared, as well as the\n"
          "year in which the game was released. The program\n"
          "was built by Peter Jungers, Summer of 2022.")
    print()
    input("Press Enter for menu options.")
    menu()


def menu():
    option = 0
    while option != 9:
        utilities.clear_terminal()
        subheader = None
        utilities.header(subheader)
        print(f"{'Search menu:':>15}{'Editing menu:':>27}\n"
              f"{'1. Search by character':>25}{'5. Add character':>20}\n"
              f"{'2. Search by game':>20}{'6. Edit character':>26}\n"
              f"{'3. Search by year':>20}{'7. Delete character':>28}\n"
              f"{'4. View all characters':>25}\n"
              "\n"
              f"{'More options:':>16}\n"
              f"{'8. Check web resource':>24}{'9. Quit program':>20}")
        print()
        print("- " * 26)
        print()
        option = validator.menu(input("Please choose an option: "), "main")
        print()
        utilities.clear_terminal()
        if option == 1 or option == 2 or option == 3:
            # Menu option number corresponds to column index in
            # database, hence the "option - 1"
            options.find_search(option - 1)
        elif option == 4:
            options.find_all()
        elif option == 5:
            options.add_character(True)
        elif option == 6:
            options.edit_character(True)
        elif option == 7:
            options.delete_character(True)
        elif option == 8:
            options.web_resource()
        elif option == 9:
            goodbye()


def goodbye():
    subheader = None
    utilities.header(subheader)
    print("Thank you for using the Super Mario Bros. character\n"
          "database.")
    time.sleep(3)


if __name__ == "__main__":
    welcome()
