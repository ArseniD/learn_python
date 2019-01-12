if __name__ == "__main__":
    i = 4
    print(type(i))
    print(int)
    print(repr(int))
    print(type(i) is int)
    print(type(i)(45))
    print(type(type(i)))
    print(i.__class__)
    print(i.__class__.__class__)
    print(i.__class__.__class__.__class__)
    print(issubclass(type, object))
    print(type(object))
    print(isinstance(i, int))
