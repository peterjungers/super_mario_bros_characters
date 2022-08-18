"""
This module links requests between options.py and data_layer.py
modules, creating class objects as needed. Static methods ordered
alphabetically.
"""


import data_layer


class Characters:

    def __init__(self, name, game, year):
        self._name = name
        self._game = game
        self._year = year

    @property
    def name(self):
        return self._name

    @property
    def game(self):
        return self._game

    @property
    def year(self):
        return self._year


    @staticmethod
    def add_character(name, game, year):
        data_layer.append(name, game, year)

    @staticmethod
    def delete_character(name):
        data_layer.delete(name)

    @staticmethod
    def get_all():
        character_list = []
        rows = data_layer.read_all()
        for row in rows:
            character = Characters(row[0], row[1], row[2])
            character_list.append(character)
        return character_list

    @staticmethod
    def get_search(name, index):
        character_list = []
        rows = data_layer.read_search(name, index)
        if rows:
            for row in rows:
                character = Characters(row[0], row[1], row[2])
                character_list.append(character)
            return character_list
        else:
            return None

    @staticmethod
    def is_existent(name):
        row = data_layer.read_existent(name)
        if row:
            character = Characters(row[0], row[1], row[2])
            return character
        else:
            return None
