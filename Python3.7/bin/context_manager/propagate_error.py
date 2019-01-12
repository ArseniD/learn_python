import contextlib


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        # <ENTER> __enter__()
        yield  # code from with block executes here
        # <NORMAL EXIT> __exit__()
        print(name, 'exited normally.')
    except Exception:
        # <EXCEPTIONAL EXIT> __exit__()
        print(name, 'received an exception!')
        # the following statement used in __exit__() to propagate
        # exception in nested context managers
        if propagate:  # If False => propagate exception if True => swallow
            raise  # propagate an exception - explicitly re-raise it


"""
PEP 343
IMPORTANT: if mgr.__exit__() returns a "true" value,
the exception is "swallowed". That is, if it returns "true",
execution continues at the next statement after the with-statement,
even if an exception happened inside the with-statement.
"""


if __name__ == "__main__":

    # The following outer will swallow the exception from inner
    # Exception will not be raised in outer with block
    with propagater('outer', True), propagater('inner', False):
        raise TypeError('Cannot convert lead into cold')

    print('\n')

    with propagater('outer', True):
        with propagater('inner', False):
            raise TypeError('Cannot convert lead into cold')

    print('\n')

    # The following outer will not swallow the exception from inner
    # Exception will be raised in outer as well in inner with blocks
    with propagater('outer', False), propagater('inner', True):
        raise TypeError('Cannot convert lead into cold')

    print('\n')

    with propagater('outer', False):
        with propagater('inner', True):
            raise TypeError('Cannot convert lead into cold')
