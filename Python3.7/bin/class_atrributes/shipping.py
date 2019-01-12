import iso6346


class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code, serial=str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(
                    owner_code=owner_code,
                    serial=ShippingContainer._get_next_serial())

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    @property
    def volume_ft3(self):
        return self._calc_volume()


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6),
                                                                category='R')

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        super()._set_celsius(value)


if __name__ == "__main__":
    c = ShippingContainer("ESC", length_ft=20, contents="textile")
    print(c.bic)

    r = RefrigeratedShippingContainer("ESC", length_ft=20, contents='peas', celsius=3.0)
    print(r.bic)

    r2 = RefrigeratedShippingContainer.create_with_items('ESC', length_ft=20, items=['brocolli', ' tomato', 'carrots'], celsius=2.0)
    print(r2.contents)
    print(r2.celsius)

    # ValueError should be raised because of attribute setter restiction
    # r2.celsius = 6.0

    r3 = RefrigeratedShippingContainer.create_empty('YML', length_ft=20, celsius=-20)
    print(r3.celsius)
    print(r3.fahrenheit)
    r3.fahrenheit = 10
    print(r3.celsius)

    r4 = RefrigeratedShippingContainer.create_empty('YML', length_ft=20, celsius=-10)
    print(r4.volume_ft3)

    h1 = HeatedRefrigeratedShippingContainer.create_empty('ESC', length_ft=20, celsius=-19)
    print(h1.celsius)
    print(h1.fahrenheit)
    h1.fahrenheit = -14  # validation should works. Error arised.
