def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def northen_city():
    return 'Minsk©'


if __name__ == "__main__":
    print(northen_city())
