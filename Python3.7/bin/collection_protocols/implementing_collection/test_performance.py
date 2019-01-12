from sorted_set import SortedSet
from random import randrange
from timeit import timeit


s = SortedSet(randrange(1000) for _ in range(2000))


def main():
    result = timeit(
              setup='from __main__ import s',
              stmt='[s.count(i) for i in range(1000)]',
              number=100)
    print(result)


if __name__ == "__main__":
    print(s)
    print(len(s))
    main()
