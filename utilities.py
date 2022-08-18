"""
This module contains various utilities used by the program.
"""


import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def header(subheader):
    print("- " * 26)
    print("Super Mario Bros. character database".center(52))
    print("- " * 26)
    print()
    if subheader != None:
        print(subheader)
        print()
