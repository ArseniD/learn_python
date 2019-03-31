class LogginProxy:
    """
    Implements loggingproxy which logs every attribute retrieval made against
    the target  objects supplied to the constuctor.
    """

    def __init__(self, target):
        # Inherit from the object super class to do our work and set up a new
        # attribute 'target'
        # setattr(object, attribute, value)
        # in python3+ you we can omit the arguments to super:
        # super().__setattr__(name, value)
        super().__setattr__('target', target)  # call the original __setattr__

    def __getattribute__(self, name):
        # __getattribute__ will intercept EVERY attribute lookup, doesn’t
        # matter if the attribute exists or not.
        # Try to get 'target' attribute from object, store the reference to the
        # target class
        # target stores an instance object
        target = super().__getattribute__('target')

        try:
            # __getattr__ is only invoked if the attribute wasn't found the
            # usual ways
            # we try to get specified attribute 'name' from object by
            # deligating to target reference
            # getattr(obj, name)
            # obj - object, where we are looking for an attribute
            # name - the name of the attribute we wanna to get
            # value will call target.name
            value = getattr(target, name)
        except AttributeError as e:
            # if attribute 'name' don’t exist in our object, we raise the error
            # with the informative message
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        # Else if attribute exists we will print it out
        print("Retrieved attribute {!r} = {!r} from {!r}".format(
            name, value, target))
        return value

    def __setattr__(self, name, value):
        # call the original implementation of __getattribute__
        # target stores an instance object
        target = super().__getattribute__('target')

        try:
            # setattr(object, attribute, value)
            # object. __setattr__(self, name, value)
            # target.name = value
            setattr(target, name, value)
        except AttributeError as e:
            # re-raise AttributeError error in more informative way
            raise AttributeError("{} could not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        print("Set attribute {!r} = {!r} on {!r}".format(name, value, target))

    def __repr__(self):
        # get proxy object reference
        target = super().__getattribute__('target')
        # call __repr__ method of a proxy object
        repr_callable = getattr(target, '__repr__')
        # call repr_callable as function
        return repr_callable()  # handy fo debugging


if __name__ == '__main__':
    from vector_modified import *

    cv = ColoredVector(red=22, green=233, blue=123, p=9, q=123)
    print(cv)
    cw = LogginProxy(cv)
    cw.p  # reads invoke LoggingProxy.__getattribute__
    # cw.p = 23  # raise an error
    cw.red
    cw.blue
    cw.green
    # cw.black  # will raise an error because this attribute does not exist in
    # cv instance
    # cw.p = 10  # writes invoke object.__setattr__ on LoggingProxy
    # p and q are immutable object, error should be raised
    cw.red = 888
    cw.green = 999
    cw.__repr__  # the call is routed via the proxy, and is dispatched
    # successfully on the target, returning the repr for ColoredVector
    repr(cw)  # will call default built-in function 'repr' of the LogginProxy,
    # this prove that __getattribute__() only invoked for dot lookups directly

