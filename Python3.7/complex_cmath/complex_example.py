if __name__ == "__main__":
    c = 3 + 5j
    print(c.real)
    print(c.imag)
    print(c.conjugate())

    import math
    # print(math.sqrt(-1))

    import cmath
    print(cmath.sqrt(-1))

    print(cmath.phase(1+1j))  # value in radiant
    print(abs(1+1j))  # gives the distance from zero
    print(cmath.polar(1+1j))  # polar co-ordinate
    modulus, phase = cmath.polar(1+1j)
    print(cmath.rect(modulus, phase))


    def inductive(ohms):
        return complex(0.0, ohms)

    def capacitive(ohms):
        return complex(0.0, -ohms)

    def resistive(ohms):
        return complex(ohms)

    def impedance(components):
        z = sum(components)
        return z

    result = impedance([inductive(10), resistive(10), capacitive(5)])
    in_radiant = cmath.phase(result)  # radiant
    print(math.degrees(in_radiant))  # degree

