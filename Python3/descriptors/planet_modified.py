class Planet:
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
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        if not value:
            raise ValueError("Cannot set empty Planet.name")
        self._name = value

    def _get_radius_metres(self):
        return self._radius_metres

    def _set_radius_metres(self, value):
        if value <= 0:
            raise ValueError(
                "radius_metres value {} is not positive".format(value))
        self._radius_metres = value

    # use explicit way in order to set property of getter and setter
    # to the functions
    radius_metres = property(fget=_get_radius_metres,
                             fset=_set_radius_metres)

    def _get_mass_kilograms(self):
        return self._mass_kilograms

    def _set_mass_kilograms(self, value):
        if value <= 0:
            raise ValueError(
                "mass_kilograms value {} is not positive".format(value))
        self._mass_kilograms = value

    mass_kilograms = property(fget=_get_mass_kilograms,
                              fset=_set_mass_kilograms)

    def _get_orbital_period_seconds(self):
        return self._orbital_period_seconds

    def _set_orbital_period_seconds(self, value):
        if value <= 0:
            raise ValueError(
                "orbital_period_seconds value {} is not positive".format(value))

    orbital_period_seconds = property(fget=_get_orbital_period_seconds,
                                      fset=_set_orbital_period_seconds)

    def _get_surface_temperature_kelvin(self):
        return self._surface_temperature_kelvin

    def _set_surface_temperature_kelvin(self, value):
        if value <= 0:
            raise ValueError(
                "surface_temperature_kelvin value {} is not positive".format(value))
        self._surface_temperature_kelvin = value

    surface_temperature_kelvin = property(fget=_get_surface_temperature_kelvin,
                                          fset=_set_surface_temperature_kelvin)

if __name__ == '__main__':

    planet = Planet(name='X',
                    radius_metres=10e2,
                    mass_kilograms=1.305e22,
                    orbital_period_seconds=12321321,
                    surface_temperature_kelvin=100)
    print(planet.radius_metres)

    # Will raise the ValueError because of invalid parameter value
    planet.radius_metres = -1000
