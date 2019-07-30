def lookups():
    s = [1, 4, 6]
    try:
        item = s[5]
    except LookupError:
        print("Handled IndexError")

    d = dict(a=54, b=32, c=123)
    try:
        value = d['x']
    except LookupError:
        print("Handled KeyError")

if __name__ == "__main__":
    s = [1, 4, 6]
    # print(s[5])  # will gives us IndexError: list index out of range
    d = dict(a=54, b=32, c=123)
    # print(d['x'])  # will gives us KeyError: 'x'

    print(IndexError.mro())
    print(KeyError.mro())

    lookups()
