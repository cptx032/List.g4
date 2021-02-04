# List library

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
        self.__list = list_value

    def __getitem__(self, key):
        return self.__list[key]

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __repr__(self):
        return self.__list.__repr__()

    def __str__(self):
        return self.__list.__str__()

    def __contains__(self, value):
        return value in self.__list
