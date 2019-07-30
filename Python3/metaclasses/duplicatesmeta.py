class OneShotClassNamespace(dict):
    """
    We can avoid method duplication by using a namespace dictionary
    which forbids re-assignment to existing keys (an error will be raise)

    args:
        dict - built-in type, which accepts many forms of arguments
    """
    def __init__(self, name, existing=None):
        """
        Loops over each entries which have been passed, inserting each key and
        value pair in turn by call to __setitem__

        args:
            name - a positional argument (for class name)
            existing - a duplcate method name
        """
        super().__init__()
        self._name = name
        if existing is not None:
            for k, v in existing:
                self[k] = v

    def __setitem__(self, key, value):
        """
        Check weither or not key is already in a dict, and if it is, will raise
        the TypeError with description (method name), otherwise add key
        with value to the dict.

        args:
            key - a method name
        """
        if key in self:
            raise TypeError(
                "Cannot reassign existing class \
                            attribute {!r} of {!r}".format(key, self._name))
        super().__setitem__(key, value)


class ProhibitDuplicatesMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases):
        """
        A simple metaclass which uses OneShotClassNamespace() for the namespace
        object.

        args:
            mcs - metaclass
            name - a class name
            bases - tuple of base classes

        return - an instance of our specialized dictionary.
        """
        return OneShotClassNamespace(name)


class Dodgy(metaclass=ProhibitDuplicatesMeta):
    """
    A simple class which contains duplicate methods and uses
    ProhibitDuplicatesMeta metaclass in order to check duplication
    """

    def method(self):
        return "first definition"

    def method(self):
        return "second definition"


if __name__ == "__main__":
    test = Dodgy()  # will raise the error of duplicate method
