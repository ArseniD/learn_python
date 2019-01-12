import datetime


if __name__ == "__main__":
    i = iter(datetime.datetime.now, None)  # Will be never terminate - None
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

    with open('ending_file.txt', 'rt') as f:
        for line in iter(lambda: f.readline().strip(), 'END'):
            print(line)
