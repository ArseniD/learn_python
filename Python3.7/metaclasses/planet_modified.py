from weakref import WeakKeyDictionary
from tracing import TracingMeta


class Named():
    """
    A simple class with the `name` attribute
    """

    def __init__(self, name=None):
        self.name = name


class Positive(Named):
    """
    Desctiptor which wraps three functions, comprise the descriptor protocol;
    __get__(), __set__(), and __delete__(), which a called when we get
    a value from descriptor, set a value through a descriptor, or delete
    a value through a descriptor respectively.
    """

    def __init__(self, name=None):
        """
        Configure a new instances of the descriptor and store them in a
        special kind of the dict for references.
        """
        super().__init__(name)
        self._instance_data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            # in order to avoid TypeError: cannot create weak refence to
            # 'NoneType' object error we return descriptor object itself
            # when instance is None, otherwise add it to the dict.
            # It allows us to call Planet.radius_metres directly and etc..
            return self  # we can also return self.owner -> Planet class
        return self._instance_data[instance]

    def __set__(self, instance, value):
        """
        Raise the error if we setting up a nonpositive value
        """
        if value <= 0:
            raise ValueError(
                "Attribute value {} {} is not positive".format(self.name, value))
        self._instance_data[instance] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute {}".format(self.name))


class DescriptorNamingMeta(type):
    """
    A metaclass which detects the presence of descriptors which are named,
    and assign the class atrribute names to them.
    """
    def __new__(mcs, name, bases, namespace):
        """
        Iterates over the names and attributes in the namespace dictionary,
        and if the attribute is an instance of `Named` we assign the name
        of the current item to its public name attribute.

        return - allocated the new class object
        """
        for name, attr in namespace.items():
            if isinstance(attr, Named):
                attr.name = name
        return super().__new__(mcs, name, bases, namespace)


class TracingDescriptorNamingMeta(TracingMeta, DescriptorNamingMeta):
    """
    Just combine two metaclasses into one with multiple inheritance
    """
    pass


class Planet(metaclass=TracingDescriptorNamingMeta):
    """
    Describe the planet parameters

    args:
        name: a name of the planet
        radius_metres: a radius in metres
        mass_kilograms: mass in kilograms
        orbital_period_seconds: orbital period in seconds
        surface_temperature_kelvin: a surface temperature in kelvin
    """

    def __init__(self,
                 name,
                 radius_metres,
                 mass_kilograms,
                 orbital_period_seconds,
                 surface_temperature_kelvin):
        # Assigning attributes, which set through descriptor
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty Planet.name")
        self._name = value

    # Positive descriptor allows Planet class to shrink by a huge amount of a
    # code dublicates and cache a data.
    # Call in the body of the class is binding an instance of a Positive()
    # descriptor to a class attribute of the Planet.
    # radius_metres, mass_kilograms, orbital_period_seconds and
    # surface_temperature_kelvin will pass to Positive() descriptor

    # Bind descriptor instance Positive() to the class attributes
    # Aggregates data in a four separate WeakDictionaries - 4 descriptors
    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()


def makes_planet():
    """
    Creates Planet  objects

    return - 3 Planet instances
    """
    sun = Planet(name='Sun',
                 radius_metres=10e222,
                 mass_kilograms=1.432e22,
                 orbital_period_seconds=124324321321,
                 surface_temperature_kelvin=100)

    earth = Planet(name='Earth',
                   radius_metres=10e22,
                   mass_kilograms=1.123e22,
                   orbital_period_seconds=1232134321,
                   surface_temperature_kelvin=100)

    pluto = Planet(name='Pluto',
                   radius_metres=10e3,
                   mass_kilograms=1.305e22,
                   orbital_period_seconds=123213,
                   surface_temperature_kelvin=100)

    return sun, earth, pluto


if __name__ == '__main__':

    sun, earth, pluto = makes_planet()
    # When we call radius_metres on planet,
    # the Positive.__get__(self, sun, Planet) method is called
    # sun - instance,
    # Planet - owner
    p = sun.radius_metres
    print(p)

    # Will call Positive.__set__(self, sun, p)
    sun.radius_metres = p

    # Will raise informative (attribute name mentioned in diagnostic message)
    # the ValueError because of nonpositive new attribute value.
    sun.radius_metres = -1000
