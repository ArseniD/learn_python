class MetaA(type):
    pass


class MetaB(type):
    pass


class MetaC(MetaA, MetaB):
    pass


class A(metaclass=MetaA):
    pass


class B(metaclass=MetaB):
    pass


class C(A, B, metaclass=MetaC):
    pass


if __name__ == "__main__":
    print(type(C))  # will show the metaclass C which combine 2 metaclasses
