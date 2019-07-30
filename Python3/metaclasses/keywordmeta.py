class KeywordsOnlyMeta(type):
    """
    Overrides default class behavior of __call__() method
    """

    def __call__(cls, *args, **kwargs):
        if args:
            raise TypeError(
                "Constructor for class {!r} does \
                 not accept positional arguments.".format(cls))
        return super().__call__(cls, **kwargs)


class TestClass(metaclass=KeywordsOnlyMeta):

    def __init__(self, *args, **kwargs):
        print("args =", args)
        print("kwargs =", kwargs)


if __name__ == "__main__":
    # TypeError will be raised,
    # because positional arguments aren't permitted
    # t = TestClass(12, 13, 14, test="dsad")

    # keywords arguments permitted
    t = TestClass(test="abc", test2="cde")
