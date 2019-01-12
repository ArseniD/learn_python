class Base1:
    def __init__(self):
        print('Base1.__init__')


class Base2:
    def __init__(self):
        print('Base2.__init__')


class Sub(Base1, Base2):
    pass


if __name__ == "__main__":
    s = Sub()  # only first init class will be printed

    from sorted_list import SortedIntList, IntList
    print(SortedIntList.__bases__)
    print(IntList.__bases__)

    print(SortedIntList.__mro__)
    print(SortedIntList.mro())

