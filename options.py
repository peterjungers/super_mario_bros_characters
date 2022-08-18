"""
This module contains functions called from the main module,
super_mario_bros_characters.py, which are responsible for getting
character data objects.
"""


import webbrowser

from logic_layer import Characters
import utilities
import validator


# Menu options 1, 2, or 3
def find_search(index):
    if index == 0:
        search = "character"
    elif index == 1:
        search = "game"
    elif index == 2:
        search = "year"

    subheader = f"- Search by {search} -"
    utilities.header(subheader)

    query = input(f"Enter {search}: ")
    if index == 0 or index == 1:
        query = validator.not_blank(query, search.title())
    elif index == 2:
        query = validator.is_year(query)
    print()
    character_list = Characters.get_search(query, index)
    if character_list != None:
        navigation = display_multiple(subheader, character_list)
        if navigation == "M":
            return
    elif character_list == None:
        print(f"That {search} is not in the database.")
        print()

    y_n = validator.y_n(input("Would you like to search for another "
                              f"{search}? (Y/N) "))
    print()
    if y_n == "Y":
        utilities.clear_terminal()
        find_search(index)
        return
    elif y_n == "N":
        return


# Menu option 4
def find_all():
    character_list = Characters.get_all()
    navigation = display_multiple(None, character_list)

    if navigation == "M":
        return
    else:
        input("Press Enter to return to the main menu.")
        return


# Retrieves multiple rows for menu options 2 and 3 (as needed), and
# menu option 4 (always needed)
def display_multiple(subheader, character_list):
    begin = 0
    end = 10
    length = len(character_list)

    while length > 0:
        utilities.clear_terminal()
        utilities.header(subheader)
        print(f"{'Name':17}{'Game':30}{'Year':10}")
        print("- " * 26)
        # Sort mixes lowercase and uppercase data values
        # (if applicable)
        character_list.sort(key=lambda x: x.name.lower())
        for character in character_list[begin:end]:
            print(f"{character.name[0:15]:17}{character.game[0:28]:30}"
                  f"{character.year:10}")
        begin = end
        end = end + 10
        length -= 10
        if length > 0:
            print("- " * 26)
            print(f"({begin - 9}–{end - 10} of {len(character_list)} "
                  "results, sorted alphabetically by\n"
                  "character)")
            print()
            enter_m = validator.enter_m(input("Press Enter to display more "
                                              "results.\n"
                                              "Press \"M\" to return to the "
                                              "main menu. ")
                                        )
            if enter_m == "":
                utilities.clear_terminal()
            elif enter_m == "M":
                return enter_m
        elif length <= 0:
            blank_rows = abs(length)
            print("\n" * (blank_rows - 1))
            print("- " * 26)
            print(f"({begin - 9}–{len(character_list)} of "
                  f"{len(character_list)} results, sorted alphabetically by\n"
                  "character)")
            print()


# Menu option 5
def add_character(show_header):
    if show_header == True:
        subheader = "- Add character -"
        utilities.header(subheader)

    name = validator.not_blank(input("Name: "), "Name")
    existent = Characters.is_existent(name)
    if existent != None:
        y_n = validator.y_n(input("That character is already in the "
                                  "database. Would\n"
                                  "you like to add a different character? "
                                  "(Y/N) ")
                            )
        print()
        if y_n == "Y":
            add_character(False)
            return
        elif y_n == "N":
            return
    game = validator.not_blank(input("Game: "), "Game")
    year = validator.is_year(input("Year: "))
    print()

    print("You entered:\n"
          f"Name: {name}\n"
          f"Game: {game}\n"
          f"Year: {year}")
    y_n_m = validator.y_n_m(input("Is this correct? (Y/N) Or type \"M\" to "
                                  "return to\n"
                                  "the main menu without saving: ")
                            )
    print()
    if y_n_m == "Y":
        Characters.add_character(name, game, year)
        print(f"{name} has been entered into the database.")
        y_n = validator.y_n(input("Would you like to add another character? "
                                  "(Y/N) ")
                            )
        print()
        if y_n == "Y":
            add_character(False)
            return
        elif y_n == "N":
            return
    elif y_n_m == "N":
        add_character(False)
        return
    elif y_n_m == "M":
        return


# Menu option 6
def edit_character(show_header):
    if show_header == True:
        subheader = "- Edit character -"
        utilities.header(subheader)

    name = input("Name of character to edit: ")
    print()
    original_data = Characters.is_existent(name)
    if original_data != None:
        print(f"Current name listed in database is {original_data.name}")
        y_n = validator.y_n(input("Do you need to edit this? (Y/N) "))
        if y_n == "Y":
            name = validator.not_blank(input("Edit name: "), "Name")
            edit = 1
        elif y_n == "N":
            edit = 0
            name = original_data.name
        print()
        print(f"Current game for {name} is {original_data.game}")
        y_n = validator.y_n(input("Do you need to edit this? (Y/N) "))
        if y_n == "Y":
            game = validator.not_blank(input("Edit game: "), "Game")
            edit += 1
        elif y_n == "N":
            edit += 0
            game = original_data.game
        print()
        print(f"Current year for {game} is {original_data.year}")
        y_n = validator.y_n(input("Do you need to edit this? (Y/N) "))
        if y_n == "Y":
            year = validator.is_year(input("Edit year: "))
            edit += 1
        elif y_n == "N":
            edit += 0
            year = original_data.year
        print()
        if edit > 0:
            print("Here is the updated character listing:\n"
                  f"Name: {name}\n"
                  f"Game: {game}\n"
                  f"Year: {year}")
            y_n_m = validator.y_n_m(input("Is this correct? (Y/N) Or type "
                                          "\"M\" to return to\n"
                                          "the main menu without saving: "))
            print()
            if y_n_m == "Y":
                Characters.delete_character(original_data.name)
                Characters.add_character(name, game, year)
                print((f"{name} has been successfully edited."))
            elif y_n_m == "N":
                edit_character(False)
                return
            elif y_n_m == "M":
                return
        elif edit == 0:
            print("No changes were made to the database.")
            print()
    elif original_data == None:
        y_n = validator.y_n(input("That character is not in the database. Would "
                                  "you\n"
                                  "like to add them? (Y/N) "))
        print()
        if y_n == "Y":
            utilities.clear_terminal()
            add_character(True)
            return
        elif y_n == "N":
            return

    y_n = validator.y_n(input("Would you like to edit another character? "
                              "(Y/N) "))
    print()
    if y_n == "Y":
        edit_character(False)
        return
    elif y_n == "N":
        return


# Menu option 7
def delete_character(show_header):
    if show_header == True:
        subheader = "- Delete character -"
        utilities.header(subheader)

    name = input("Name of character to delete: ")
    existent = Characters.is_existent(name)
    if existent != None:
        y_n = validator.y_n(input(f"Are you sure you want to delete {name}? "
                                  "(Y/N) "))
        if y_n == "Y":
            Characters.delete_character(name)
            print(f"{name} has been deleted.")
    elif existent == None:
        print("That character is not in the database.")
    print()

    y_n = validator.y_n(input("Would you like to delete another character? "
                              "(Y/N) "))
    print()
    if y_n == "Y":
        delete_character(False)
        return
    elif y_n == "N":
        return


# Menu option 8
def web_resource():
    while True:
        utilities.clear_terminal()
        subheader = None
        utilities.header(subheader)

        print("The \"Super Mario Wiki\" website is a resource\n"
              "containing information from Super Mario games about\n"
              "characters, games, and much more. You can use the\n"
              "site to double-check your database here, or use it\n"
              "to find characters you might have forgotten or\n"
              "never even heard of. The site will open in a\n"
              "browser window.")
        print()
        print(f"{'Super Mario Wiki:':>28}\n"
              f"{'1. Search by character name':>38}\n"
              f"{'2. View entire character list':>40}\n"
              f"{'3. Return to main menu':>33}")
        print()
        print("- " * 26)
        print()

        option = validator.menu(input("Please choose an option: "),
                                "web_search")
        print()
        if option == 1:
            search = validator.not_blank(input("Please enter character "
                                               "name: "), "Name")
            webbrowser.open(f"https://www.mariowiki.com/{search}")
        elif option == 2:
            webbrowser.open("https://www.mariowiki.com/List_of_characters")
        elif option == 3:
            return
