from collections.abc import MutableSequence


if __name__ == "__main__":
    """MutableSequence is subclass of list

    if hasattr(type(MutableSequence), '__subclasscheck__')
        return type(MutableSequence).__subclasscheck__(list)
    """
    print(issubclass(list, MutableSequence))
    print(list.__mro__)
    # ms = MutableSequence()  # raise the error
