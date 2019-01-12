from decimal import Decimal
from fractions import Fraction


if __name__ == "__main__":
    print(abs(-5))
    print(abs(-5.0))
    print(abs(Decimal(-5)))
    print(abs(Fraction(-5, 1)))
    print(abs(complex(0, -5)))

    print(round(0.2812, 3))
    print(round(0.625, 1))
    print(round(1.5))
    print(round(2.5))
    print(round(Decimal('3.25'), 1))
    print(round(Fraction(57, 100), 2))
    print(round(Fraction(57, 100), 1))
    print(round(Fraction(57, 100), 0))

    print(round(2.675, 2))  # round() show suprising behaviour with float format
