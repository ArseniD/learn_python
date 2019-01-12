class Base:
    def __init__(self):
        print('Base initializer')

    def f(self):
        print('Base.f()')


class Sub(Base):
    def __init__(self):
        super().__init__()  # call base class initializer
        print('Sub initializer')

    def f(self):
        print('Sub.f()')


if __name__ == "__main__":
    s = Sub()
