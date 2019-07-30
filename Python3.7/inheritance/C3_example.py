class A: pass


class B(A): pass


class C(A): pass


class D(B, A, C): pass  # Error should be raised because of MRO order


if __name__ == "__main__":
    d = D()
