from abc import ABCMeta


class Text(metaclass=ABCMeta):
    """
    Register a class as a virtual subclass,
    Base metaclass must be ABCMeta.
    """

    pass


if __name__ == "__main__":
    print(Text.register(str))       # Call register (sub) metamethod
    print(issubclass(str, Text))    # Call to register() returns its argument
    print(isinstance("some text", Text))

    # Can use @register as a class-decorator
    @Text.register
    class Prose:
        pass

    print(issubclass(Prose, Text))
