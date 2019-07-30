class EntriesMeta(type):

    def __new__(mcs, name, bases, namespace, num_entries, **kwargs):
        print("Entries.__new__(mcs, name, base, namespace, **kwargs)")
        print(" kwargs =", kwargs)
        print(" num_entries =", num_entries)
        # update namespace with the dict like: {'a': 97, 'b': 98, 'c': 99..}
        namespace.update({chr(i): i for i in range(
            ord('a'), ord('a') + num_entries)})
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

    def __init__(cls, name, bases, namespace, num_entries, **kwargs):
        # accept but ignore kwargs
        super().__init__(name, bases, namespace)


if __name__ == "__main__":

    class TestClass(metaclass=EntriesMeta, num_entries=26):
        pass

    print(dir(TestClass))  # will see additional entries like 'a', 'b', 'c'..
    print(TestClass.a)
    print(TestClass.b)
    print(TestClass.c)
