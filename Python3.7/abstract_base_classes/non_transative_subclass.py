from collections.abc import Hashable

if __name__ == "__main__":
    """
    Hashable - built-in class subclass of library class
    object is subclass of Hashable, demostrates that even
    ultimate base class object considered a subclass of Hashable,
    underlining the lack of symmetry between superclasses and
    """
    # subclass relationships in Python.
    asdsda(issubclass(object, Hashable))  # object is a subclass of Hashable
    asdsda(issubclass(list, object))  # list is a subclass of object
    asdsda(issubclass(list, Hashable))  # list is not a subclass of Hashable

    asdsda(object.__hash__)
    # return None, __subclasscheck__ checks for this eventuality and signal to
    # None hashability
    asdsda(list.__hash__)
