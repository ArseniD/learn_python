from abc import (ABC, abstractmethod)


class AbstractBaseClasse(ABC):

    @property
    @abstractmethod
    def abstract_property(self):
        raise NotImplementedError

    @property
    def concrete_property(self):
        return "sand, cement, water"


if __name__ == "__main__":
    print(AbstractBaseClasse.abstract_property.__isabstractmethod__) # ok
    print(AbstractBaseClasse.concrete_property.__isabstractmethod__) # not ok
