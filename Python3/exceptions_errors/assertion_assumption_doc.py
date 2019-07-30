def modulus_three(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:
        assert r == 2, "Remainder is not 2"
        print("Remainder 2")


def module_four(n):
    r = n % 4
    if r == 0:
        print("Multiple of 4")
    elif r == 1:
        print("Remainder 1")
    elif r == 2:
        print("Reaminder 2")
    elif r == 3:
        print("Remainder 3")
    else:
        assert False, "This should never happen"


if __name__ == "__main__":
    modulus_three(1)
    modulus_three(2)
    modulus_three(3)
    modulus_three(4)

    module_four(1)
    module_four(2)
    module_four(3)
    module_four(4)
    module_four(21312321321.123213)  # error should be raised







