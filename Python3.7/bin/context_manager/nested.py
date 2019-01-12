import contextlib


@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield name
    print('Exiting', name)


if __name__ == "__main__":
    with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
        print('BODY')

    print('\n')

    with nest_test('outer') as n1:
        with nest_test('inner, nested in ' + n1):
            print('BODY')
