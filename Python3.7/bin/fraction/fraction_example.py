from fractions import Fraction


if __name__ == "__main__":
    two_thirds = Fraction(2, 3)
    four_fifth = Fraction(4, 5)
    #  exception_zero = Fraction(5, 0)
    arbitary_value = Fraction(23423454354666543543)
    float_value = Fraction(0.5)
    float_value_2 = Fraction(0.1)
    float_decimal = Fraction('0.1')
    float_str = Fraction('22/7')

    print(two_thirds)
    print(four_fifth)
    print(arbitary_value)
    print(float_value)
    print(float_value_2)
    print(float_decimal)
    print(float_str)

    print(Fraction(2, 3) + Fraction(4, 5))
    print(Fraction(2, 3) - Fraction(4, 5))
    print(Fraction(2, 3) * Fraction(4, 5))
    print(Fraction(2, 3) / Fraction(4, 5))
    print(Fraction(2, 3) // Fraction(4, 5))

    from math import floor
    print(floor(Fraction('4/3')))
