class ChessCoordinate:

    def __new__(cls, *args, **kwargs):
        """
        def new(cls, *args, **kwargs) - appears implicitly is a class method,
        it accepts cls as it's first argument rather than self.
        In fact new is especially cased static method that happens
        to take the type of the class as its first argument (cls) - the type of
        the object to be created.
        Secondly it accepts any addition that we pass to the constructor.
        Puprose of __new__ is to allocate a new object.
        """
        print("args =", repr(args))
        print("kwargs =", repr(kwargs))
        # All object allocation must be done by the __new__ implementation
        # on the ultimate base class object - cls
        # Call via super() more maintainable. Newly allocated ChessCoordinate
        obj = super().__new__(cls)  # ultimate allocator: object.__new__(cls)
        print("id(obj) =", id(obj))  # check object id
        return obj  # returned obj will pass to self in __init__ method

    def __init__(self, file, rank):

        # Returned object from __new__ we pass to the self in __init__, we can
        # easily check it by printing id of the object in __init__
        print("id(self) =", id(self))

        if len(file) != 1:
            raise ValueError("{} component file {!r} does not have a length of one.".format(
                self.__class__.__name__, file))

        if file not in 'abcdefgh':
            raise ValueError("{} component file {!r} is out of range.".format(
                self.__class__.__name__, file))

        if rank not in range(1, 9):
            raise ValueError("{} component rank {!r} is out of range.".format(
                self.__class__.__name__, rank))

        self._file = file
        self._rank = rank  # __init__ does not return anything.
        # It simply mutates the instance it has been given
        # behind the scenes, object  __setattr__ is been called.

    @property
    def file(self):
        return self._file

    @property
    def rank(self):
        return self._rank

    def __repr__(self):
        return "{}(file={}, rank={})".format(
            self.__class__.__name__, self.file, self.rank)

    def __str__(self):
        return '{}{}'.format(self.file, self.rank)


def main():
    white_queen = ChessCoordinate('d', 4)
    print(white_queen)


if __name__ == '__main__':
    main()

    # Inherited __new__() allocates the object which is passed to __init__()
    # as self, __new__ is responsible for allocating (creation) an instance
    print(ChessCoordinate.__new__)
    # shows that ChessCoordinate __new__ is the very same method as
    # object.__new__
    print(ChessCoordinate.__new__ is object.__new__)
