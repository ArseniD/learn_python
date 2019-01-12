import sys
from functools import wraps


def log_to(stream):

    def logging_decorator(func):

        @wraps(func)
        def logging_wrapper(*args, **kwargs):
            print(func.__name__ + " was called", file=stream)
            return func(*args, **kwargs)

        return logging_wrapper

    return logging_decorator


@log_to(sys.stderr)
def some_function(x):
    """A decorated function"""
    return x + x


if __name__ == "__main__":
    print(some_function(2))
    print(some_function.__name__)
    print(some_function.__doc__)
