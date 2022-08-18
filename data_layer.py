"""
This module gets data from the csv database and returns it. Functions
ordered alphabetically.
"""


import csv


def append(name, game, year):
    character = [(name, game, year)]

    with open("smb_char_db.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(character)


def delete(name):
    rewrite_file = []
    with open("smb_char_db.csv", newline="") as file:
        for row in csv.reader(file):
            if name.lower() != row[0].lower():
                rewrite_file.append(row)

    with open("smb_char_db.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rewrite_file)


def read_all():
    all_data = []
    with open("smb_char_db.csv", newline="") as file:
        for row in csv.reader(file):
            all_data.append(row)
        return all_data


def read_existent(name):
    with open("smb_char_db.csv", newline="") as file:
        for row in csv.reader(file):
            if name.lower() == row[0].lower():
                return row


def read_search(query, index):
    """
    :param "query": User entered search value
    :param "index": Index of column in database
    """
    data = []
    with open("smb_char_db.csv", newline="") as file:
        for row in csv.reader(file):
            # Returns values that start with one-character "query"
            if len(query) == 1 and query.lower()[0] == row[index].lower()[0]:
                data.append(row)
            # Returns values containing entire "query" string
            elif len(query) > 1 and query.lower() in row[index].lower():
                data.append(row)
        return data
