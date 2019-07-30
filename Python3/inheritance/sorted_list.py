class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer value.')

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList({!r})".format(list(self))


class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


if __name__ == "__main__":
    sl = SortedList([4,3,123,55])
    print(sl)
    print(len(sl))
    sl.add(-42)
    print(sl)
    sl.add(7)
    print(sl)

    print(isinstance(3, int))
    print(isinstance('hello!', str))
    print(isinstance(4.234, bytes))
    print(isinstance(sl, SortedList))
    print(isinstance(sl, SimpleList))
    x = []
    print(isinstance(x, (float, dict, list)))

    il = IntList([1, 2, 3, 4])
    il.add(19)
    print(il)
    # il.add('5')  # error should be raised

    print(issubclass(IntList, SimpleList))
    print(issubclass(SortedList, SimpleList))
    print(issubclass(SortedList, IntList))

    sil = SortedIntList([42, 23, 2])
    print(sil)
    # print(SortedIntList([3, 2, '1']))  # error should be raised
    sil.add(-1234)
    print(sil)
    # sil.add('123')  # error should be raised
