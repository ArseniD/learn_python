class A:
    def func(self):
        return 'A.func'


class B:
    def func(self):
        return 'B.func'


class C:
    def func(self):
        return 'C.func'


class D(B, C):
    pass


if __name__ == "__main__":
    print(D.mro())
    d = D()
    print(d.func())  # will call B, because B is the first class in order in D

    from sorted_list import SortedIntList
    print(SortedIntList.mro())
