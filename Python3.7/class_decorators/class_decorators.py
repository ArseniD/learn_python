def my_class_decorator(cls):
    """
    Print attributes of the class object (__dict__)
    """
    for name, attr in vars(cls).items():
        print(name)
    return cls

@my_class_decorator
class Temperature:

    def __init__(self, kelvin):
        self._kelvin = kelvin

    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, value):
        self._kelvin = value


if __name__ == "__main__":
    p = Temperature
    print(p)
