# List library
from __future__ import print_function

class ListBoolean:
    def __init__(self, boolean_exp):
        self.__value = boolean_exp

    def __bool__(self):
        return bool(self.__value)

    def __nonzero__(self):
        return bool(self.__value)

TRUE = ListBoolean(True)
FALSE = ListBoolean(False)


class ListList:
    def __init__(self, list_value):
        self._list = list_value

    def __getitem__(self, key):
        return self._list[key]

    def __setitem__(self, key, value):
        self._list[key] = value

    def __repr__(self):
        return self._list.__repr__()

    def __str__(self):
        return self._list.__str__()

    def __contains__(self, value):
        return value in self._list

    def __add__(self, value):
        return [
            self._list[i]
            if i > (len(value._list) - 1)
            else self._list[i] + value._list[i]
            for i in list(range(len(self._list)))
        ]

    def __mul__(self, value):
        if type(value) is not self.__class__:
            raise ValueError("Incompatible types")
        return self._list + value._list
