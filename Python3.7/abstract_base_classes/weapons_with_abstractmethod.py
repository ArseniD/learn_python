from abc import ABC, abstractmethod

# class ABC(metaclass=ABCMeta):
#     """Helper class that provides a standard wau to create an ABC using inheritance."""
#     pass


class Sword(ABC):  # ABCMeta knows nothing about Swords
    """Sword will be a virtual base class."""

    @classmethod
    def __subclasshook__(cls, sub):
        """Return true if a class contans swipe() and sharpen() methods."""
        # Note: Does not perform check for subclassing by inheritance
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'thrust') and callable(sub.thrust)
                and
                hasattr(sub, 'parry') and callable(sub.parry)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen)
                or NotImplemented)


    @abstractmethod
    def swipe(self):
        raise NotImplementedError

    @abstractmethod
    def thrust(self):
        print("Thrusting...")

    @abstractmethod
    def parry(self):
        raise NotImplementedError


class BroadSword(Sword):
    """Implements both swipe() and sharpen()."""

    def swipe(self):
        print("Swoosh!")

    def thrust(self):
        super().thrust()

    def parry(self):
        print("Parry!")

    def sharpen(self):
        print("Shink!")


@Sword.register
class LightSaber:

    def swipe(self):
        print("Fffkrrrsh..xx..xxx")


# SamuraiSword is a virtual subclass
# It's abstractness is not detected: thrust() and thrust()
class SamuraiSword:
    """Implements both swipe() and sharpen()."""

    def swipe(self):
        print("Slice!")

    def sharpen(self):
        print("Shink!")


class Rifle:
    """Implements neither swipe() nor sharpen()."""

    def fire(self):
        print("Bam!")


if __name__ == "__main__":
    # Note: perfomr __subclasscheck__
    print(issubclass(BroadSword, Sword))  # ok
    print(issubclass(SamuraiSword, Sword))  # ok
    print(issubclass(LightSaber, Sword))  # ok
    print(issubclass(Rifle, Sword))  # not ok

    broad_sword = BroadSword()
    samurai_sword = SamuraiSword() # SamuraiSword is a virtual subclass

    # Note: perform __instancecheck__
    print(isinstance(broad_sword, Sword))  # ok
    print(isinstance(samurai_sword, Sword))  # ok

    print(broad_sword.swipe())
    # print(broad_sword.thrust())  # raise the error, becasue it's not possible
    # to call virtual base class methods using super, which relies on searching
    # of the MRO.
    print(BroadSword.__mro__)  # Sword not in MRO for BroadSword
