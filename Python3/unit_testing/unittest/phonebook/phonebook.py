from itertools import chain


class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        """
        Check whether dict values contain dublicated prefix or not

        return: True or False
        """
        result = list(map(lambda x: x[:3], list(self.entries.values())))
        return len(set(result)) == len(result)

    def get_names(self):
        """
        Convert all keys and values in a single list
        """
        return list(chain.from_iterable(self.entries.items()))
