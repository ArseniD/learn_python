class SwordMeta(type):
    def __instancecheck__(cls, instance):
        """
        Delegates to __subclasscheck__() method which is called as a metamethod
        on the actual classs, cls.

        Place our call to instance produces a resuly consistent
        with the result from issubclass method.
        """
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, sub):
        """
        Returns true if a class contans swipe() and sharpen() methods
        """
        # Note: Does not perform check for subclassing by inheritance
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and hasattr(sub, 'sharpen') and callable(sub.sharpen))


class Sword(metaclass=SwordMeta):
    """
    Sword will be a virtual base class
    """

    def thrust(self):
        print("Thrusting...")


class BroadSword:
    """
    Implements both swipe() and sharpen()
    """

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shink!")


class SamuraiSword:
    """
    Implements both swipe() and sharpen()
    """

    def swipe(self):
        print("Slice!")

    def sharpen(self):
        print("Shink!")


class Rifle:
    """
    Implements neither swipe() nor sharpen()
    """

    def fire(self):
        print("Bam!")


if __name__ == "__main__":
    # Note: perfomr __subclasscheck__
    print(issubclass(BroadSword, Sword))  # ok
    print(issubclass(SamuraiSword, Sword))  # ok
    print(issubclass(Rifle, Sword))  # not ok

    broad_sword = BroadSword()
    samurai_sword = SamuraiSword()
    # Note: perform __instancecheck__
    print(isinstance(broad_sword, Sword))  # ok
    print(isinstance(samurai_sword, Sword))  # ok

    print(broad_sword.swipe())
    # print(broad_sword.thrust())  # raise the error, becasue it's not possible
    # to call virtual base class methods using super, which relies on searching
    # the MRO.
    print(BroadSword.__mro__)  # Sword not in MRO for BroadSword
