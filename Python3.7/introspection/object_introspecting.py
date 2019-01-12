if __name__ == "__main__":
    i = 23
    print(dir(i))
    print(getattr(i, 'denominator'))
    print(i.denominator)
    print(getattr(i, 'conjugate'))
    print(callable(getattr(i, 'conjugate')))
    print(i.conjugate.__class__.__name__)
    # print(getattr(i, 'index'))  # will gives us an error
    print(hasattr(i, 'bit_length'))
    print(hasattr(i, 'index'))
