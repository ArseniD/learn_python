import contextlib
import sys


class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'You are in a with-block!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__:'
                  'normal exit detected')
        else:
            print('LoggingContextManager.__exit__:'
                  'Exception detected!'
                  'type={}, value={}, traceback={}'.format(
                exc_type, exc_val, exc_tb))


@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield 'You are in a with-block!'
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit', sys.exc_info())


if __name__ == "__main__":
    # with LoggingContextManager() as x:
    #     print(x)

    with LoggingContextManager():
        pass

    # with LoggingContextManager() as x:
    #     raise ValueError('Something has gone wrong!')
    #     print(x)

    try:
        with LoggingContextManager():
            raise ValueError('The system is down!')
    except ValueError:
        print('*** ValueError detected ***')


    with logging_context_manager() as x:
        print(x)

    with logging_context_manager() as x:
        raise ValueError('Something went wrong!')
