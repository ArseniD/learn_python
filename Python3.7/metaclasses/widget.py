class Widget:
    """
    Class definition

    class Widget(object, metaclass=type):
        '''
        The base class is implicitly object, the metaclass is implicitly type.
        object - default base class
        type - default metaclass
        '''
        pass


    1) Metaclass creates namespace dictionary
    2) Runtime populates namespace from class block
    3) Metaclass allocates class object
    4) we get Widget class

    When we write 'class Widget' the following is happening:

    name='Widget'
    metaclass=type
    bases=()
    kwargs={}

    # creates a new namespace object, which behaves like a dictionary.
    # Behind the scenes the Python populates the namespace dictionary while
    # reading the contents of the class block.

    namespace=metaclass.__prepare__(name, bases, **kwargs)

    # the metaclasses __new__() method is called to allocate the class object

    Widget=metaclass.__new__(metaclass, name, bases, namespace, **kwargs)

    # the metaclasses __init__() is called to initialize the class object

    metaclass.__init__(Widget, name, bases, namespace, **kwargs)

    # The name, bases, and namespace arguments contain the information
    # collected during execution of the class definition normally the class
    # attributes and method definitions inside the class block, although in our
    # case, the class block is logically empty = pass.
    # By providing metaclass we can customize these behaviors
    """
    pass


if __name__ == '__main__':
    w = Widget()
    print(w)
    print(type(w))
    print(type(Widget))  # type of a class Widget is type.
    # Type is the metaclass

    a = list("A list")
    print(type(a))  # type of a is list

    print(type(type))  # type is its own metaclass

    print(w.__class__)
    print(w.__class__.__class__)  # type

    # return type, which is the base of the recursion
    print(w.__class__.__class__.__class__)
