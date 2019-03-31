class Resistor:
    """
    Describe the type of electronic component called a resistor

    args:
        resistance_ohms: resistance in ohms
        tolerance_percent: a tolerance in percent
        power_watts: a power capability in watts
    """

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.resistance_ohms = resistance_ohms
        self.tolerance_percent = tolerance_percent
        self.power_watts = power_watts


class Resistor_with_slots:
    """
    Describe the type of electronic component called a resistor

    args:
        resistance_ohms: resistance in ohms
        tolerance_percent: a tolerance in percent
        power_watts: a power capability in watts
    """

    # A class attribute for reducing memory and increasing space performance
    # Take a list of a class arguments
    __slots__ = ['resistance_ohms', 'tolerance_percent', 'power_watts']

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.resistance_ohms = resistance_ohms
        self.tolerance_percent = tolerance_percent
        self.power_watts = power_watts

if __name__ == '__main__':

    import sys

    d = {}
    print(sys.getsizeof(d))  # even an empty Python dictionary is quite a hefty
    # object wheighing in at 288 bytes

    r21 = Resistor(12, 0.2, 0.25)

    print(sys.getsizeof(r21) + sys.getsizeof(r21.__dict__))

    # Python object being highly dynamic, dictionary-based objects
    # we can add attributes to them ar runtime and see if this is reflected
    # as an increased size.

    r21.cost_dollars = 0.02
    r21.a = 3.034324324
    r21.b = 5.0343232134324
    print(sys.getsizeof(r21) + sys.getsizeof(r21.__dict__))

    # The size of object will be much reduced by the __slots__
    # from 208 bytes to 64 as in C language
    # Now the object no longer contains __dict__ and cannot add attribute
    # dynamically
    r22 = Resistor_with_slots(12, 0.2, 0.25)

    print(sys.getsizeof(r22))

    # r22.cost_dollars = 0.02  # will raise the error, because no __dict__
    # r22.a = 3.034324324  # will raise the error, because no __dict__
    # r22.b = 5.0343232134324  # will raise the error, because no __dict__
