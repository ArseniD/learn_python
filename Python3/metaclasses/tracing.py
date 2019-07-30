class TracingMeta(type):

    """
    Our metaclass TracingMeta should be a subclass of an existing metaclass, so
    we'll subclass type.
    """

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        """
        we must explicitly decorate __prepare__ class-method with
        the appropriate decorator @classmethod
        __prepare__ must return a (usually empty) mapping
        Prepare the namespace of a class.
        This method is called before the class body is executed
        and it must return a dictionary-like object that's used
        as the local namespace for all the code from the class body

        args:
            mcs - metaclass, is a reference to itself (tracing.TracingMeta),
                  the first argument is analogous to the self-argument
                  passed to instance methods and the cls argument passed
                  to the class methods.
                  For metaclassed it's conventionally called mcs.

            name - class name as a string.
            base - tuple of base classes.
            kwargs - dictionary of keyword arguments (attrs/functions).

            return - return a namespace object.
        """

        print("TracingMeta.__prepare__(name, bases, **kwargs)")
        print(" mcs =", mcs)
        print(" name =", name)
        print(" bases =", bases)
        print(" kwargs =", kwargs)
        # Each of our overrides delegates with to the base class type method to
        # do the actual work required via a call to super.
        # Populates namespace by calling type.__prepare__().
        # Value is a dictionary of nascent class, including his body content.
        namespace = super().__prepare__(name, bases)
        print("<-- namespace =", namespace)
        print()
        return namespace

    def __new__(mcs, name, bases, namespace, **kwargs):
        """
        __new__ is implicitly a class-method
        __new__ must return a (usually newly allocated) class object


        args:
            mcs - metaclass, is a reference to itselfi (tracing.TracingMeta),
                  the first argument is analogous to the self-argument
                  passed to instance methods and the cls argument passed
                  to the class methods.
                  For metaclassed it's conventionally called mcs.

            name - class name as a string.

            base - tuple of base classes.

            namespace - namespace object returned from __prepare__().
                        The Python runtime has popoulated this dictionary
                        with several entries, as it has processed
                        the class definition of Widget with his methods
                        and attributes inside.

            kwargs - dictionary of keyword arguments (attrs/functions).

            return: a new class (Widget).
                    !!!Potentially modify namespace before calling __new__(),
                    as this is the point at which the class object is created.
                    To change the contents of the class namespace after this
                    call the class object must be manupulated directly.
        """

        print("TracingMeta.__new__(mcs, name, bases, namespace, **kwargs)")
        print(" mcs=", mcs)
        print(" name =", name)
        print(" bases =", bases)
        print(" namespace =", namespace)
        print(" kwargs =", kwargs)
        # Each of our overrides delegates with to the base class type method to
        # do the actual work required via a call to super
        # Within __new__() we deligate to the base class, type.__new__(), via
        # a call to super, forwarding mcs, name, bases, and namespace
        # arguments.
        cls = super().__new__(mcs, name, bases, namespace)
        print("<-- cls=", cls)
        print()
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        """
        The puprose of __init__() is to configure the newly created
        class object.
        __init__() here is an instance method of the metaclass,
        not an explicit class method like __prepare__ or an implicit
        class method like __new__().

        args:
            cls - regular class (is one level less meta than mcs,
                  in the same way that self is one level meta less than cls)

            name - class name as a string.

            base - tuple of base classes.

            namespace - namespace object returned from __prepare__().
                        The Python runtime has popoulated this dictionary
                        with several entries, as it has processed
                        the class definition of widget.

            kwargs - dictionary of keyword arguments (attrs/functions).

            return: doesn't return anything it's expected to modify
                    the existing class object that was handed to it.
                    Note that although the namespace object is passed
                    to __init__, it's content should already have been used
                    upstream by __new__ when allocating the class object.
                    Changing the namespace will be ineffectual, and any changes
                    to the class object must be affected by manipulating cls
                    directly.
                    The key here is that metaclasses give us the opportunity to
                    modify the dictionary of class attributes, which includes
                    methods, before the class  is instantiated. We also could
                    created an alternative list of base-classes (base) or
                    could allocate a different class entirely (cls)

        """
        print("TracingMeta.__init__(mcs, name, bases, namespace, **kwargs)")
        print(" mcs=", cls)
        print(" name =", name)
        print(" bases =", bases)
        print(" namespace =", namespace)
        print(" kwargs =", kwargs)
        # Each of our overrides delegates with to the base class type method to
        # do the actual work required via a call to super
        # Call type.__init__()
        super().__init__(name, bases, namespace)
        print()

    def metamethod(cls):
        print("TracingMeta.metamethod(cls)")
        print("cls =", cls)
        print()

    def __call__(cls, *args, **kwargs):
        """
        Calling the regular class invokes metaclass.__call__()
        __call__() method orchestrates the default class allocation and
        initialization behavior.

        w = Widget()

        metaclass.__call__() invokes regular class __new__() and __init__()

        The behavior of calling __new__ followed by __init__ when we call a
        constuctor is actually the responsobility of __call__ on the metaclass
        __call__() is a metamethod and therefor can be called like
        a class method, and that __call__() makes the object on which it is
        defined callable, like functions.
        This is a mechanism by which classes in Python become callable,
        and what we have been referring hither as a conctuctor call is,
        in fact, the __call__() metamethod.
        """

        print("TracingMeta.__call__(cls, *args, **kwargs)")
        print(" cls=", cls)
        print(" args =", args)
        print(" kwargs =", kwargs)
        print(" About to call type.__call__()")
        obj = super().__call__(*args, **kwargs)  # invoke type.__call__()
        print(" Returned from type.__call__()")
        print("<-- obj =", obj)
        print()
        return obj


class TracingClass(metaclass=TracingMeta):
    """
    Simple class which overrides methods __new__() and __init__() in order to
    test metaclass out
    """

    def __new__(cls, *args, **kwargs):
        print(" TracingClass.__new__(cls, args, kwargs)")
        print(" cls =", cls)
        print(" args =", args)
        print(" kwargs =", kwargs)
        obj = super().__new__(cls)
        print(" <-- obj =", obj)
        print()
        return obj

    def __init__(self, *args, **kwargs):
        print(" TracingClass.__init__(self, args, kwargs)")
        print(" self =", self)
        print(" args =", args)
        print(" kwargs =", kwargs)
        print()


if __name__ == "__main__":

    # We will see creation process when the class machinery is invoked
    class Widget(metaclass=TracingMeta):
        # namespace - namespace object returned from __prepare__().
        # The Python runtime has popoulated this dictionary with several
        # entries, as it has processed the class definition of widget.

        # namespace = {'__module__': '__main__', '__qualname__': 'Widget',
        # 'action': <function Widget.action at 0x7f99640ad598>, 'the_answer':
        # 42}

        # __module__ - map to a name of module in which class is defined
        # __qualname__ - contains the fully qualified name of the class,
        # including parent modules and packages.

        def action(self, message):
            print(message)
        the_answer = 42

    # call metaclassmethod directly as @classmethod
    Widget.metamethod()


    class Test(metaclass=TracingMeta, tension=432):
        """
        We are using Test class in order to show tension attribute in metaclass
        methods (as kwargs).
        """

        def test_method(self, word):
            print(word)
        cube = True


    # Test __call__() output of TracingClass instance.
    # Pay your attention that methods __init__() and __new__() will be called
    # from TracingClass not from metaclass.
    t = TracingClass(22, keyword="test")
