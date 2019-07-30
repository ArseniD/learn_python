class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Poing2D(x={}), y={})'.format(self.x, self.y)

    def __format__(self, f):
        if f == 'r':
            return '{}, {}'.format(self.y, self.x)
        else:
            return '{}, {}'.format(self.x, self.y)


if __name__ == "__main__":
    p = Point2D(3, 4)
    print(repr(p))
    print(str(p))

    p2 = Point2D(x=3, y=4)
    print(p2)  # by default 'print' function use 'str' string representation

    print('This is a point: {}'.format(Point2D(1, 2)))

    print('{}'.format(Point2D(1, 2)))  # refers to the __format__ method
    print('{:r}'.format(Point2D(1, 2)))  # refers to the __format__ method
    print('{!r}'.format(Point2D(1, 2)))  # !r refers to the __repr__ method
    print('{!s}'.format(Point2D(1, 2)))  # !s refers to the __str__ method

    import reprlib
    points = [Point2D(x, y) for x in range(1000) for y in range(1000)]
    print(len(points))
    print(reprlib.repr(points))  # will show only a few elements instead of all
