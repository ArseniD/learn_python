class DataDescriptor:

    def __get__(self, instance, owner):
        print("DataDescriptor.__get__({!r}, {!r}, {!r})".format(
            self, instance, owner))

    def __set__(self, instance, value):
        print("DataDescriptor.__set__({!r}, {!r}, {!r})".format(
            self, instance, value))


class NonDataDescriptor:

    def __get__(self, instance, owner):
        print("NonDataDescriptor.__get__({!r}, {!r}, {!r})".format(
            self, instance, owner))


class Owner:

    a = DataDescriptor()
    b = NonDataDescriptor()


if __name__ == "__main__":

    obj = Owner()

    # If an instance __dict__ has an enty with the same name as a
    # data-desciptor (__get__, __set__ / __delete__) the data-descriptor takes
    # precedence
    print(obj.a)
    obj.__dict__['a'] = 13213  # set an item in the instance dictinoary
    # with the same name as 'a' and retrieve 'a' again
    # since this is a data descriptor the first rule applies, and the data
    # descriptor takes precedence when we call obj.a.
    print(obj.a)

    # If an instance __dict__ has an enty with the same name as a
    # non-data-descriptor (__get__) the entry in __dict__ takes precedence
    print(obj.b)  # the first time we access obj.b there is no entry of the
    # same name in the instance dictionary, so the NonDataDescriptor take
    # precedence
    obj.__dict__['b'] = 132  # after we added 'b' enty into dunder dict the
    # second rule applies, and the dictionary entry takes precedence over the
    # NonDataDescriptor.
    print(obj.b)
