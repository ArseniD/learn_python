from pprint import pprint as pp


sunday = [12, 13, 15, 22, 23, 21, 11, 14]
monday = [14, 11, 14, 24, 21, 17, 16, 15]
tuesday = [2, 2, 4, 5, 11, 12, 13, 14, 14]
daily = [sunday, monday, tuesday]


if __name__ == "__main__":
    ''' zip function accepting an argument of start iterables,
        any number of iterables as positional arguments'''

    for item in zip(sunday, monday):
        print(item)

    for item in zip(sunday, monday, tuesday):
        print(item)

    pp(daily)

    for item in zip(daily[0], daily[1], daily[2]):
        print(item)

    for item in zip(*daily):
        print(item)

    # converting columns into rows and rows into columns - transposition
    transposed = list(zip(*daily))
    pp(transposed)
