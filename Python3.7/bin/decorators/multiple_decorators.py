def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()


@tracer
@escape_unicode
def my_city(name):
    return name + '©'


class CityMaker:
    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_city(self, name):
        return name + ' ' + self.suffix


if __name__ == "__main__":
    print(my_city('Minsk'))
    print(my_city('Minsk'))
    print(my_city('Minsk'))

    cm = CityMaker('City')
    print(cm.make_city('Minsk'))

    tracer.enabled = False

    print(my_city('Minsk'))
    print(my_city('Minsk'))
    print(my_city('Minsk'))

    print(cm.make_city('Minsk'))
