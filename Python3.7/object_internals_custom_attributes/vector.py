class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{} ({}, {})".format(self.__class__.__name__, self.x, self.y)


if __name__ == '__main__':
    v = Vector(6, 3)
    print(v)

    print(dir(v))
    print(v.__dict__)
    print(type(v.__dict__))
    print(v.__dict__['x'])

    # change attribute
    v.__dict__['x'] = 18
    print(v.x)

    # remove attribute entirely
    del v.__dict__['x']
    # print(v.x) # will raise the attribute error
    print('x' in v.__dict__)
    print('y' in v.__dict__)
    # add new attribute to the dictiunary
    v.__dict__['z'] = 14
    print(v.z)

    # More preferable way to use Python built-in functions
    print(getattr(v, 'y'))
    print(hasattr(v, 'x'))
    delattr(v, 'z')
    setattr(v, 'x', 9)
    print(v.x)

