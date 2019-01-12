from sorted_list import *
from pprint import pprint as pp


if __name__ == "__main__":
    #  Class-bound proxy
    print(SortedIntList.mro())
    print(super(SortedList, SortedIntList))
    print(super(SortedList, SortedIntList).add)
    print(super(SortedIntList, SortedIntList)._validate(5))

    #  Instance-bound proxy
    pp(SortedIntList.mro())
    sil = SortedIntList([5, 15, 10])
    pp(sil)
    pp(super(SortedList, sil))
    super(SortedList, sil).add(6)
    pp(sil)  # SortedList is not sorted anymore
    super(SortedList, sil).add('ASd dsasd ')
    pp(sil)


