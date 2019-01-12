import decimal


if __name__ == "__main__":
    print(decimal.getcontext())
    print(decimal.Decimal(5))
    print(decimal.Decimal('0.7') - decimal.Decimal('0.6'))
    print(decimal.Decimal(0.7) - decimal.Decimal(0.6))
    print(decimal.Decimal(0.7) > decimal.Decimal('0.5'))
    print(decimal.Decimal(0.7) > 0.5)
    print(decimal.Decimal('0.8') > 0.7)
    print((-7) % 3)
    print(decimal.Decimal(-7) % decimal.Decimal(3))

    def is_odd(n):
        return n % 2 != 0

    print(is_odd(decimal.Decimal(-3)))
