from abc import (ABC, abstractmethod)
import functools


def invariant(predicate):
    """
    Create a class decorator which checks a class invariant.

    Args:
        predicate: A callable to which, after every method invocation,
        the object on which the method was called will be passed.
        The predicate should evaluate to True if the class invariant
        has been maintained, or False if it has been violated.

    Returns:
        A class decorator for checking the class invariant tested by the
        supplied predicate function.
    """
    def invaruant_checking_class_decorator(cls):
        """
        A class decorator for checking invariants.
        """
        # a list of methods names by identifying the callable attribute
        # Filter class attributes for callables
        method_names = [name for name, attr in vars(
            cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_with_invariant_checking_proxy(cls, name, predicate)

        property_names = [name for name, attr in vars(
            cls).items() if isinstance(attr, PropertyDataDescriptor)]
        for name in property_names:
            _wrap_property_with_invariant_checking_proxy(cls, name, predicate)

        return cls
    return invaruant_checking_class_decorator


def _wrap_method_with_invariant_checking_proxy(cls, name, predicate):
    """
    Process each class method
    """
    method = getattr(cls, name)
    assert callable(method)

    @functools.wraps(method)
    # A function decorator
    def invariant_checking_method_decorator(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not predicate(self):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(
                predicate.__doc__, self))
        return result
    # Use setattr to modify/update cls.__dict__
    setattr(cls, name, invariant_checking_method_decorator)


def _wrap_property_with_invariant_checking_proxy(cls, name, predicate):
    """
    Process each class property
    """
    prop = getattr(cls, name)
    assert isinstance(prop, property)

    invariant_checking_proxy = InvariantCheckingPropertyProxy(prop, predicate)

    setattr(cls, name, invariant_checking_proxy)


class PropertyDataDescriptor(ABC):

    @abstractmethod
    def __get__(self, instance, owner):
        raise NotImplementedError

    @abstractmethod
    def __set__(self, instance, value):
        raise NotImplementedError

    @abstractmethod
    def __delete__(self, instance):
        raise NotImplementedError

    @property
    @abstractmethod
    def __isabstractmethod__(self):
        raise NotImplementedError


# define a virtual subclass
PropertyDataDescriptor.register(property)


# define a real subclass
class InvariantCheckingPropertyProxy(PropertyDataDescriptor):
    """
    A class descriptor

    __init__ - stores the reference to the referent property and
               the predicate function


    __get__, __set__ and __delete__ - forward to the underlying referent
                                      property, and then check that class
                                      invariant of the instance remains
                                      unviolated.
    """

    def __init__(self, referent, predicate):
        self._referent = referent
        self._predicate = predicate

    def __get__(self, instance, owner):
        if instance is None:
            return self._referent
        result = self._referent.__get__(instance, owner)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(
                self._predicate.__doc__, instance))
        return result

    def __set__(self, instance, value):
        result = self._referent.__set__(instance, value)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(
                self._predicate.__doc__, instance))
        return result

    def __delete__(self, instance):
        result = self._referent.__delete__(instance)
        if not self._predicate(instance):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(
                self._predicate.__doc__, instance))
        return result

    def __isabstractmethod__(self):
        return self._referent.__isabstractmethod__


def not_below_absolute_zero(temperature):
    """
    Temperature not below absolute zero
    """
    return temperature._kelvin >= 0


def below_absolute_hot(temperature):
    """
    Temperature below absolute hot
    """
    return temperature._kelvin <= 1.416785e32


# Accepts predicate function as argument
@invariant(below_absolute_hot)  # Second fails to find already wrapped props
@invariant(not_below_absolute_zero)  # First successfully wraps property attrs
class Temperature:

    def __init__(self, kelvin):
        self._kelvin = kelvin

    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, value):
        self._kelvin = value

    @property
    # Binds the getter to descriptor method celius.__get__()
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    # Binds the setter to descriptor method celius.__set__()
    def celsius(self, value):
        self._kelvin = value + 273.15

    @property
    # Binds the getter to descriptor method fahrenheit.__get__()
    def fahrenheit(self):
        return self._kelvin * 9/5 - 459.67

    @fahrenheit.setter
    # Binds the setter to descriptor method fahrenheit.__set__()
    def fahrenheit(self, value):
        self._kelvin = (value + 459.67) * 5/9


if __name__ == "__main__":
    from pprint import pprint as pp

    t = Temperature(42)
    t.celsius = -300  # fails as designed, through celsius setter
    t.celsius = 1e34  # fails as designed as well
