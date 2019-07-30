class Vector:

    def __init__(self, **coords):
        """
        coords - accept a key and value of the coordinates (dict)
        private_coords - make coords private by adding '_' at the beginning
        The update() method adds coords element(s) to the dictionary
        if the key is not in the dictionary.
        """
        private_coords = {'_' + k: v for k, v in coords.items()}
        # update the entries in dunder dict
        # self.__dict__.update(private_coords)
        # more pythonic way to access __dict__
        vars(self).update(private_coords)

    def __getattr__(self, name):
        """
        Retrieve the underlying attribute for us.
        Use try block in order to avoid infinite loop search if
        privae_name does not exist
        """
        private_name = '_' + name
        try:
            # return self.__dict__[private_name]
            return vars(self)[private_name]
        except KeyError:
            raise AttributeError('{!r} object has no attribute {!r}'.format(
                self.__class__, name))

    def __setattr__(self, name, value):
        """
        Not allowed to set attributes on immutable objects of this class,
        prevent writing on any attribute
        """
        raise AttributeError("Can't set attribute {!r}".format(name))

    def __delattr__(self, name):
        """
        Deleteion of an attribute should be forbidden for client
        """
        raise AttributeError("Can't delete attribute {!r}".format(name))

    def __repr__(self):
        """
        Print out the class name and key, value of an instance dict attribute
        """
        # changing vector, so it stores it's components in a dedicated
        # dictionary
        # separate from dunder dict, athough of course, this dictionary itself
        # will need to be stored in dunder dict
        # replace all keys that started with '_' in __dict__
        modified_dict = {k.replace('_', ''): v for (
            k, v) in vars(self).items()}
        # self.__dict__.update(new_dict)
        return "{} ({})".format(self.__class__.__name__,
                                ', '.join("{k}={v}".format(
                                    # strip the underscore '_' by using slicing
                                    # to emit the first character
                                    k=k, v=modified_dict[k])
                                    # Note that dictionary is unsorted, so we
                                    # need to sort it out in order to get the
                                    # coordinates in specified as function
                                    # arguments
                                    for k in sorted(modified_dict.keys())))

    # def __repr__(self):
    #     return "{}({})".format(self.__class__.__name__,
    #                            ', '.join("{k}={v}".format(k=k[1:], v=self.__dict__[k])
    # for k in sorted(self.__dict__.keys())))


class ColoredVector(Vector):

    COLOR_INDEXES = ('red', 'green', 'blue')

    def __init__(self, red, green, blue, **coords):
        super().__init__(**coords)
        # self.__dict__['color'] = [red, green, blue]
        # more pythonic way to access __dict__
        vars(self)['color'] = [red, green, blue]

    def __getattr__(self, name):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            return super().__getattr__(name)
        else:
            # return self.__dict__['color'][channel]
            return vars(self)['color'][channel]

    def __setattr__(self, name, value):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            # # setattr(object, attribute, value)
            # object. __setattr__(self, name, value)
            # target.name = value
            return super().__setattr__(name, value)
        else:
            # self.__dict__['color'][channel] = value
            vars(self)['color'][channel] = value

    def __repr__(self):
        keys = set(self.__dict__.keys())
        keys.discard('color')
        coords = ', '.join("{k}={v}".format(k=k[1:], v=self.__dict__[k])
                           for k in sorted(keys))

        return "{cls}(red={red}, green={green}, blue={blue} {coords})".format(
            cls=self.__class__.__name__,
            red=self.red,
            green=self.green,
            blue=self.blue,
            coords=coords)


if __name__ == '__main__':
    v = Vector(p=6, q=3)
    print(v)

    print(dir(v))  # '_p' and '_q' will be at the end of list
    print(v.p)  # we cannot access 'p' directly because now it private attribute
    # v.p = 14  # will raise the error
    # v.x  # will raise the error
    # del v.x  # will raise the error

    print(v.__dict__)
    print(type(v.__dict__))
    # print(v.__dict__['x'])

    # # change attribute
    v.__dict__['x'] = 18
    print(v.x)

    # # remove attribute entirely
    del v.__dict__['x']
    # print(v.x) # will raise the attribute error
    print('x' in v.__dict__)
    print('y' in v.__dict__)
    # # add new attribute to the dictiunary
    v.__dict__['z'] = 14
    print(v.z)

    print(v.__dict__)  # see the attributes
    print(v.__class__)  # see the type of the Vector object
    print(v.__class__.__dict__)  # an object of type mappinxproxy
    print(v.__class__.__dict__['__repr__'](v))  # retrieve the callable object
    # and pass that instance to it taking the place what is normallty the
    # self-argument to a method

    setattr(v.__class__, 'a_vector_class_attribute', 342)  # set new attribute
    # to a class
    print(dir(v))  # will see 'a_vector_class_attribute' in attributes list
    # The machinery of the setattr knows how to insert attributes into the
    # class dictionary
    print(Vector.a_vector_class_attribute)  # will return the value of 342
    print(v.__class__.mro())

    # # More preferable way to use Python built-in functions
    # print(getattr(v, 'y'))
    # print(hasattr(v, 'x'))
    # delattr(v, 'z')
    # setattr(v, 'x', 9)
    # print(v.x)

    cv = ColoredVector(red=22, green=43, blue=123, p=4, q=12)
    print(cv.red)    # stored in a list at __dict__['color']
    print(cv.green)  # stored in a list at __dict__['color']
    print(cv.blue)   # stored in a list at __dict__['color']

    cv.red = 777
    print(cv.red)

    print(cv.p)  # stored directly in dict
    print(cv.q)  # stored directly in dict

    print(dir(cv))  # will see _p and _q attribute for Vector components
    # and 'color' for color component

    print(cv)
    print(cv.__dict__)
