from fractions import Fraction


def mixed_numeral(vulgar):
    if not (hasattr(vulgar, 'numerator') and hasattr(vulgar, 'denominator')):
        raise TypeError("{} is not a rational number".format(vulgar))

    integer = vulgar.numerator // vulgar.denominator
    fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
                        vulgar.denominator)
    return integer, fraction

def mixed_numeral_2(vulgar):
    try:
        integer = vulgar.numerator // vulgar.denominator
        fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
                            vulgar.denominator)
        return integer, fraction
    except AttributeError as e:
        # more information what went wrong and why
        raise TypeError("{} is not a rational number".format(vulgar)) from e


if __name__ == "__main__":
    print(mixed_numeral(Fraction('11/10')))
    # print(1.6)  # will receive an error because of float format

    print(mixed_numeral_2(1.7))
