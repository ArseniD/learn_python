from sorted_list import *


class NoBaseClass: pass


if __name__ == "__main__":
    #  Observe object class
    print(SortedIntList.mro())
    print(list.mro())
    print(int.mro())

    print(NoBaseClass.__bases__)
    print(dir(object))
